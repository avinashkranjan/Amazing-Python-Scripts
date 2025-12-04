import requests
import time
import concurrent.futures
from urllib.parse import urlparse
import socket
import subprocess
import os

class IPTVLinkTester:
    def __init__(self, input_file='iptv_links.txt', working_file='working_links.txt', broken_file='broken_links.txt'):
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
        """Test using HTTP HEAD request"""
        try:
            response = requests.head(url, headers=self.headers, timeout=self.timeout, allow_redirects=True)
            return response.status_code in [200, 206, 301, 302, 307, 308]
        except:
            return False

    def test_http_get_partial(self, url):
        """Test using HTTP GET with range request"""
        try:
            headers = self.headers.copy()
            headers['Range'] = 'bytes=0-1024'
            response = requests.get(url, headers=headers, timeout=self.timeout, stream=True, allow_redirects=True)
            if response.status_code in [200, 206]:
                # Try to read a small chunk
                chunk = next(response.iter_content(1024), None)
                return chunk is not None and len(chunk) > 0
            return False
        except:
            return False

    def test_http_streaming(self, url):
        """Test streaming capability"""
        try:
            response = requests.get(url, headers=self.headers, timeout=self.timeout, stream=True, allow_redirects=True)
            if response.status_code in [200, 206]:
                # Try to read multiple chunks
                chunk_count = 0
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        chunk_count += 1
                        if chunk_count >= 3:  # Successfully read 3 chunks
                            return True
                return chunk_count > 0
            return False
        except:
            return False

    def test_socket_connection(self, url):
        """Test basic socket connection"""
        try:
            parsed = urlparse(url)
            host = parsed.hostname
            port = parsed.port or (443 if parsed.scheme == 'https' else 80)
            
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(self.timeout)
            result = sock.connect_ex((host, port))
            sock.close()
            return result == 0
        except:
            return False

    def test_with_ffmpeg(self, url):
        """Test using ffmpeg/ffprobe if available"""
        try:
            # Check if ffprobe is available
            result = subprocess.run(
                ['ffprobe', '-v', 'error', '-show_entries', 
                 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1', url],
                capture_output=True,
                timeout=self.timeout,
                text=True
            )
            return result.returncode == 0
        except (subprocess.TimeoutExpired, FileNotFoundError, Exception):
            return False

    def test_link_comprehensive(self, url, link_number, total_links):
        """Perform comprehensive testing on a single link"""
        print(f"\n{'='*70}")
        print(f"Testing link {link_number}/{total_links}")
        print(f"URL: {url[:80]}{'...' if len(url) > 80 else ''}")
        print(f"{'='*70}")
        
        results = []
        test_methods = [
            ("HTTP HEAD Request", self.test_http_head),
            ("HTTP GET Partial", self.test_http_get_partial),
            ("HTTP Streaming", self.test_http_streaming),
            ("Socket Connection", self.test_socket_connection),
            ("FFmpeg Probe", self.test_with_ffmpeg)
        ]
        
        # Perform multiple attempts for each test method
        for method_name, test_func in test_methods:
            print(f"\n{method_name}:")
            method_results = []
            
            for attempt in range(self.attempts):
                print(f"  Attempt {attempt + 1}/{self.attempts}...", end=' ', flush=True)
                try:
                    result = test_func(url)
                    method_results.append(result)
                    print(f"{'✓ PASS' if result else '✗ FAIL'}")
                    
                    if result:
                        time.sleep(2)  # Short delay on success
                    else:
                        time.sleep(3)  # Slightly longer delay on failure
                        
                except Exception as e:
                    print(f"✗ ERROR: {str(e)[:50]}")
                    method_results.append(False)
                    time.sleep(3)
            
            success_rate = sum(method_results) / len(method_results) * 100
            print(f"  Success rate: {success_rate:.1f}%")
            results.extend(method_results)
        
        # Determine if link is working
        total_tests = len(results)
        successful_tests = sum(results)
        success_percentage = (successful_tests / total_tests) * 100
        
        print(f"\n{'─'*70}")
        print(f"OVERALL RESULT: {successful_tests}/{total_tests} tests passed ({success_percentage:.1f}%)")
        
        # If ANY test passed even once, consider it potentially working
        is_working = successful_tests > 0
        
        if is_working:
            print(f"Status: ✓ WORKING (at least {successful_tests} test(s) succeeded)")
        else:
            print(f"Status: ✗ BROKEN (all tests failed)")
        
        print(f"{'='*70}\n")
        
        return is_working, success_percentage

    def process_links(self):
        """Process all links from input file"""
        # Read all links
        try:
            with open(self.input_file, 'r', encoding='utf-8') as f:
                links = [line.strip() for line in f if line.strip()]
        except FileNotFoundError:
            print(f"Error: {self.input_file} not found!")
            return
        
        if not links:
            print("No links found in the input file!")
            return
        
        print(f"Found {len(links)} links to test")
        print(f"Each link will be tested {self.attempts} times per method")
        print(f"Timeout per request: {self.timeout} seconds")
        print(f"This will take approximately {len(links) * self.attempts * 5 * 3 / 60:.1f} minutes\n")
        
        working_links = []
        broken_links = []
        
        # Test each link
        for idx, link in enumerate(links, 1):
            is_working, success_rate = self.test_link_comprehensive(link, idx, len(links))
            
            if is_working:
                working_links.append(f"{link} # Success rate: {success_rate:.1f}%\n")
            else:
                broken_links.append(f"{link} # All tests failed\n")
            
            # Small delay between links
            if idx < len(links):
                print("Waiting 5 seconds before next link...\n")
                time.sleep(5)
        
        # Write results
        with open(self.working_file, 'w', encoding='utf-8') as f:
            f.writelines(working_links)
        
        with open(self.broken_file, 'w', encoding='utf-8') as f:
            f.writelines(broken_links)
        
        # Summary
        print("\n" + "="*70)
        print("TESTING COMPLETE!")
        print("="*70)
        print(f"Total links tested: {len(links)}")
        print(f"Working links: {len(working_links)} (saved to {self.working_file})")
        print(f"Broken links: {len(broken_links)} (saved to {self.broken_file})")
        print("="*70)

def main():
    print("IPTV Link Tester - Comprehensive Edition")
    print("="*70)
    
    tester = IPTVLinkTester()
    tester.process_links()

if __name__ == "__main__":
    main()
