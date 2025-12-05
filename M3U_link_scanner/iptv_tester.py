"""
IPTV Link Tester - Comprehensive Edition
Tests M3U/IPTV links using multiple verification methods
"""

import requests
import time
from urllib.parse import urlparse
import socket
import subprocess


class IPTVLinkTester:
    """Test IPTV/M3U links for availability using multiple methods"""
    
    # HTTP status codes that indicate a working link
    SUCCESS_STATUS_CODES = {200, 206, 301, 302, 307, 308}
    STREAMING_STATUS_CODES = {200, 206}
    
    def __init__(self, input_file='iptv_links.txt', 
                 working_file='working_links.txt', 
                 broken_file='broken_links.txt'):
        """
        Initialize the IPTV link tester
        
        Args:
            input_file: Path to file containing IPTV links (one per line)
            working_file: Path to output file for working links
            broken_file: Path to output file for broken links
        """
        self.input_file = input_file
        self.working_file = working_file
        self.broken_file = broken_file
        self.timeout = 20
        self.attempts = 5
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept': '*/*',
            'Accept-Encoding': 'identity;q=1, *;q=0',
            'Range': 'bytes=0-',
        }

    def test_http_head(self, url):
        """
        Test using HTTP HEAD request
        
        Args:
            url: The URL to test
            
        Returns:
            bool: True if the link responds with a success status code
        """
        try:
            response = requests.head(
                url, 
                headers=self.headers, 
                timeout=self.timeout, 
                allow_redirects=True
            )
            return response.status_code in self.SUCCESS_STATUS_CODES
        except (requests.RequestException, requests.Timeout, 
                requests.ConnectionError) as e:
            return False

    def test_http_get_partial(self, url):
        """
        Test using HTTP GET with range request for first 1KB
        
        Args:
            url: The URL to test
            
        Returns:
            bool: True if data can be retrieved
        """
        try:
            headers = self.headers.copy()
            headers['Range'] = 'bytes=0-1024'
            response = requests.get(
                url, 
                headers=headers, 
                timeout=self.timeout, 
                stream=True, 
                allow_redirects=True
            )
            
            if response.status_code in self.STREAMING_STATUS_CODES:
                # Try to read a small chunk
                chunk = next(response.iter_content(1024), None)
                return chunk is not None and len(chunk) > 0
            return False
        except (requests.RequestException, requests.Timeout, 
                requests.ConnectionError):
            return False

    def test_http_streaming(self, url):
        """
        Test streaming capability by reading multiple chunks
        
        Args:
            url: The URL to test
            
        Returns:
            bool: True if multiple chunks can be streamed
        """
        try:
            response = requests.get(
                url, 
                headers=self.headers, 
                timeout=self.timeout, 
                stream=True, 
                allow_redirects=True
            )
            
            if response.status_code in self.STREAMING_STATUS_CODES:
                # Try to read multiple chunks
                chunk_count = 0
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        chunk_count += 1
                        if chunk_count >= 3:  # Successfully read 3 chunks
                            return True
                return chunk_count > 0
            return False
        except (requests.RequestException, requests.Timeout, 
                requests.ConnectionError):
            return False

    def test_socket_connection(self, url):
        """
        Test basic socket connection to the host
        
        Args:
            url: The URL to test
            
        Returns:
            bool: True if socket connection succeeds
        """
        try:
            parsed = urlparse(url)
            host = parsed.hostname
            port = parsed.port or (443 if parsed.scheme == 'https' else 80)
            
            if not host:
                return False
            
            # Use context manager for proper resource cleanup
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(self.timeout)
                result = sock.connect_ex((host, port))
                return result == 0
                
        except (socket.error, socket.timeout, OSError):
            return False

    def test_with_ffmpeg(self, url):
        """
        Test using ffmpeg/ffprobe if available
        
        Args:
            url: The URL to test
            
        Returns:
            bool: True if ffprobe can read the stream
        """
        try:
            result = subprocess.run(
                ['ffprobe', '-v', 'error', '-show_entries', 
                 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1', url],
                capture_output=True,
                timeout=self.timeout,
                text=True,
                check=False
            )
            return result.returncode == 0
        except subprocess.TimeoutExpired:
            return False
        except FileNotFoundError:
            # ffprobe not installed
            return False
        except Exception as e:
            # Catch any other unexpected errors
            print(f"  Unexpected error in ffprobe: {type(e).__name__}")
            return False

    def _run_test_attempts(self, method_name, test_func, url):
        """
        Run multiple test attempts for a single test method
        
        Args:
            method_name: Name of the test method for display
            test_func: The test function to call
            url: The URL to test
            
        Returns:
            list: List of boolean results for each attempt
        """
        print(f"\n{method_name}:")
        method_results = []
        
        for attempt in range(self.attempts):
            print(f"  Attempt {attempt + 1}/{self.attempts}...", end=' ', flush=True)
            try:
                result = test_func(url)
                method_results.append(result)
                print('✓ PASS' if result else '✗ FAIL')
                
                # Delay between attempts to avoid rate limiting
                time.sleep(2 if result else 3)
                    
            except Exception as e:
                print(f"✗ ERROR: {str(e)[:50]}")
                method_results.append(False)
                time.sleep(3)
        
        success_rate = (sum(method_results) / len(method_results)) * 100
        print(f"  Success rate: {success_rate:.1f}%")
        
        return method_results

    def test_link_comprehensive(self, url, link_number, total_links):
        """
        Perform comprehensive testing on a single link
        
        Args:
            url: The URL to test
            link_number: Current link number being tested
            total_links: Total number of links to test
            
        Returns:
            tuple: (is_working, success_percentage)
        """
        separator = '=' * 70
        print(f"\n{separator}")
        print(f"Testing link {link_number}/{total_links}")
        print(f"URL: {url[:80]}{'...' if len(url) > 80 else ''}")
        print(separator)
        
        test_methods = [
            ("HTTP HEAD Request", self.test_http_head),
            ("HTTP GET Partial", self.test_http_get_partial),
            ("HTTP Streaming", self.test_http_streaming),
            ("Socket Connection", self.test_socket_connection),
            ("FFmpeg Probe", self.test_with_ffmpeg)
        ]
        
        # Collect all test results
        all_results = []
        for method_name, test_func in test_methods:
            method_results = self._run_test_attempts(method_name, test_func, url)
            all_results.extend(method_results)
        
        # Calculate overall statistics
        total_tests = len(all_results)
        successful_tests = sum(all_results)
        success_percentage = (successful_tests / total_tests) * 100
        
        # Display results
        print(f"\n{'─' * 70}")
        print(f"OVERALL RESULT: {successful_tests}/{total_tests} tests passed "
              f"({success_percentage:.1f}%)")
        
        # If ANY test passed even once, consider it potentially working
        is_working = successful_tests > 0
        
        status = (f"✓ WORKING (at least {successful_tests} test(s) succeeded)" 
                 if is_working else "✗ BROKEN (all tests failed)")
        print(f"Status: {status}")
        print(f"{separator}\n")
        
        return is_working, success_percentage

    def process_links(self):
        """Process all links from input file and categorize as working or broken"""
        # Read all links from input file
        try:
            with open(self.input_file, 'r', encoding='utf-8') as f:
                links = [line.strip() for line in f if line.strip()]
        except FileNotFoundError:
            print(f"Error: {self.input_file} not found!")
            print(f"Please create {self.input_file} with one IPTV link per line.")
            return
        except IOError as e:
            print(f"Error reading {self.input_file}: {e}")
            return
        
        if not links:
            print("No links found in the input file!")
            return
        
        # Display testing plan
        estimated_time = (len(links) * self.attempts * 5 * 3) / 60
        print(f"Found {len(links)} links to test")
        print(f"Each link will be tested {self.attempts} times per method")
        print(f"Timeout per request: {self.timeout} seconds")
        print(f"Estimated time: {estimated_time:.1f} minutes\n")
        
        working_links = []
        broken_links = []
        
        # Test each link
        for idx, link in enumerate(links, 1):
            is_working, success_rate = self.test_link_comprehensive(
                link, idx, len(links)
            )
            
            if is_working:
                working_links.append(f"{link} # Success rate: {success_rate:.1f}%\n")
            else:
                broken_links.append(f"{link} # All tests failed\n")
            
            # Delay between links to avoid rate limiting
            if idx < len(links):
                print("Waiting 5 seconds before next link...\n")
                time.sleep(5)
        
        # Write results to files
        try:
            with open(self.working_file, 'w', encoding='utf-8') as f:
                f.writelines(working_links)
            
            with open(self.broken_file, 'w', encoding='utf-8') as f:
                f.writelines(broken_links)
        except IOError as e:
            print(f"Error writing output files: {e}")
            return
        
        # Display summary
        separator = '=' * 70
        print(f"\n{separator}")
        print("TESTING COMPLETE!")
        print(separator)
        print(f"Total links tested: {len(links)}")
        print(f"Working links: {len(working_links)} (saved to {self.working_file})")
        print(f"Broken links: {len(broken_links)} (saved to {self.broken_file})")
        print(separator)


def main():
    """Main entry point for the IPTV link tester"""
    print("IPTV Link Tester - Comprehensive Edition")
    print("=" * 70)
    
    tester = IPTVLinkTester()
    tester.process_links()


if __name__ == "__main__":
    main()
