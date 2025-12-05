"""
IPTV Link Tester - Comprehensive Edition
Tests M3U/IPTV links using multiple verification methods
"""

import shutil
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

    def __init__(
        self,
        input_file='iptv_links.txt',
        working_file='working_links.txt',
        broken_file='broken_links.txt'
    ):
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
            'User-Agent': (
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                'AppleWebKit/537.36'
            ),
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
        except requests.Timeout:
            return False
        except requests.ConnectionError:
            return False
        except requests.RequestException:
            return False
        except Exception as e:
            print(f"  Unexpected error in HTTP HEAD: "
                  f"{type(e).__name__}")
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
        except requests.Timeout:
            return False
        except requests.ConnectionError:
            return False
        except requests.RequestException:
            return False
        except Exception as e:
            print(f"  Unexpected error in HTTP GET Partial: "
                  f"{type(e).__name__}")
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
                        if chunk_count >= 3:
                            # Successfully read 3 chunks
                            return True
                return chunk_count > 0
            return False
        except requests.Timeout:
            return False
        except requests.ConnectionError:
            return False
        except requests.RequestException:
            return False
        except Exception as e:
            print(f"  Unexpected error in HTTP Streaming: "
                  f"{type(e).__name__}")
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
            port = parsed.port or (
                443 if parsed.scheme == 'https' else 80
            )

            if not host:
                return False

            # Use context manager for proper resource cleanup
            with socket.socket(
                socket.AF_INET,
                socket.SOCK_STREAM
            ) as sock:
                sock.settimeout(self.timeout)
                result = sock.connect_ex((host, port))
                return result == 0
        except socket.timeout:
            return False
        except socket.gaierror:
            # DNS resolution failed
            return False
        except socket.error:
            return False
        except Exception as e:
            print(f"  Unexpected error in Socket Connection: "
                  f"{type(e).__name__}")
            return False

    def test_with_ffmpeg(self, url):
        """
        Test using ffmpeg/ffprobe if available

        Args:
            url: The URL to test

        Returns:
            bool: True if ffprobe can read the stream
        """
        # Check if ffprobe is available in PATH
        ffprobe_path = shutil.which('ffprobe')
        if not ffprobe_path:
            return False

        try:
            result = subprocess.run(
                [
                    ffprobe_path,
                    '-v', 'error',
                    '-show_entries', 'format=duration',
                    '-of', 'default=noprint_wrappers=1:nokey=1',
                    url
                ],
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
        except PermissionError:
            # No permission to execute ffprobe
            return False
        except Exception as e:
            print(f"  Unexpected error in FFmpeg: "
                  f"{type(e).__name__}")
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
            attempt_num = attempt + 1
            print(f"  Attempt {attempt_num}/{self.attempts}...",
                  end=' ', flush=True)
            try:
                result = test_func(url)
                method_results.append(result)
                print('✓ PASS' if result else '✗ FAIL')

                # Delay between attempts to avoid rate limiting
                time.sleep(2 if result else 3)
            except KeyboardInterrupt:
                print("\n\nTesting interrupted by user")
                raise
            except Exception as e:
                print(f"✗ ERROR: {str(e)[:50]}")
                method_results.append(False)
                time.sleep(3)

        if method_results:
            success_count = sum(method_results)
            success_rate = (success_count / len(method_results)) * 100
            print(f"  Success rate: {success_rate:.1f}%")
        else:
            print("  Success rate: 0.0%")

        return method_results

    def _display_test_header(self, url, link_number, total_links):
        """Display test header information"""
        separator = '=' * 70
        print(f"\n{separator}")
        print(f"Testing link {link_number}/{total_links}")
        truncated_url = url[:80]
        if len(url) > 80:
            truncated_url += '...'
        print(f"URL: {truncated_url}")
        print(separator)

    def _display_test_results(
        self,
        successful_tests,
        total_tests,
        success_percentage
    ):
        """Display test results summary"""
        separator = '─' * 70
        print(f"\n{separator}")
        print(f"OVERALL RESULT: {successful_tests}/{total_tests} "
              f"tests passed ({success_percentage:.1f}%)")

        # If ANY test passed even once, consider it potentially working
        is_working = successful_tests > 0

        if is_working:
            status = (f"✓ WORKING (at least {successful_tests} "
                     f"test(s) succeeded)")
        else:
            status = "✗ BROKEN (all tests failed)"

        print(f"Status: {status}")
        print(f"{'=' * 70}\n")

        return is_working

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
        self._display_test_header(url, link_number, total_links)

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
            method_results = self._run_test_attempts(
                method_name,
                test_func,
                url
            )
            all_results.extend(method_results)

        # Calculate overall statistics
        total_tests = len(all_results)
        successful_tests = sum(all_results)

        if total_tests > 0:
            success_percentage = (successful_tests / total_tests) * 100
        else:
            success_percentage = 0.0

        # Display results
        is_working = self._display_test_results(
            successful_tests,
            total_tests,
            success_percentage
        )

        return is_working, success_percentage

    def _read_links_from_file(self):
        """
        Read links from input file

        Returns:
            list: List of links, or None if error occurred
        """
        try:
            with open(self.input_file, 'r', encoding='utf-8') as f:
                links = [line.strip() for line in f if line.strip()]
            return links
        except FileNotFoundError:
            print(f"Error: {self.input_file} not found!")
            print(f"Please create {self.input_file} with one IPTV "
                  f"link per line.")
            return None
        except PermissionError:
            print(f"Error: Permission denied reading "
                  f"{self.input_file}")
            return None
        except UnicodeDecodeError:
            print(f"Error: Unable to decode {self.input_file}. "
                  f"Please ensure it's UTF-8 encoded.")
            return None
        except IOError as e:
            print(f"Error reading {self.input_file}: {e}")
            return None

    def _write_results_to_file(self, filename, links):
        """
        Write results to output file

        Args:
            filename: Output filename
            links: List of formatted link strings to write

        Returns:
            bool: True if successful, False otherwise
        """
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.writelines(links)
            return True
        except PermissionError:
            print(f"Error: Permission denied writing to {filename}")
            return False
        except IOError as e:
            print(f"Error writing to {filename}: {e}")
            return False

    def _display_testing_plan(self, link_count):
        """Display the testing plan information"""
        estimated_time = (link_count * self.attempts * 5 * 3) / 60
        print(f"Found {link_count} links to test")
        print(f"Each link will be tested {self.attempts} times "
              f"per method")
        print(f"Timeout per request: {self.timeout} seconds")
        print(f"Estimated time: {estimated_time:.1f} minutes\n")

    def _display_final_summary(
        self,
        total_links,
        working_count,
        broken_count
    ):
        """Display final testing summary"""
        separator = '=' * 70
        print(f"\n{separator}")
        print("TESTING COMPLETE!")
        print(separator)
        print(f"Total links tested: {total_links}")
        print(f"Working links: {working_count} "
              f"(saved to {self.working_file})")
        print(f"Broken links: {broken_count} "
              f"(saved to {self.broken_file})")
        print(separator)

    def process_links(self):
        """
        Process all links from input file and categorize as
        working or broken
        """
        # Read all links from input file
        links = self._read_links_from_file()
        if links is None:
            return

        if not links:
            print("No links found in the input file!")
            return

        # Display testing plan
        self._display_testing_plan(len(links))

        working_links = []
        broken_links = []

        # Test each link
        try:
            for idx, link in enumerate(links, 1):
                is_working, success_rate = self.test_link_comprehensive(
                    link, idx, len(links)
                )

                result_line = (
                    f"{link} # Success rate: {success_rate:.1f}%\n"
                )
                if is_working:
                    working_links.append(result_line)
                else:
                    broken_links.append(
                        f"{link} # All tests failed\n"
                    )

                # Delay between links to avoid rate limiting
                if idx < len(links):
                    print("Waiting 5 seconds before next link...\n")
                    time.sleep(5)
        except KeyboardInterrupt:
            print("\n\nTesting interrupted by user. "
                  "Saving partial results...")

        # Write results to files
        if not self._write_results_to_file(
            self.working_file,
            working_links
        ):
            return

        if not self._write_results_to_file(
            self.broken_file,
            broken_links
        ):
            return

        # Display summary
        self._display_final_summary(
            len(links),
            len(working_links),
            len(broken_links)
        )


def main():
    """Main entry point for the IPTV link tester"""
    print("IPTV Link Tester - Comprehensive Edition")
    print("=" * 70)

    try:
        tester = IPTVLinkTester()
        tester.process_links()
    except KeyboardInterrupt:
        print("\n\nProgram terminated by user")
    except Exception as e:
        print(f"\n\nUnexpected error: {type(e).__name__}: {e}")
        print("Please report this issue with the full error message")


if __name__ == "__main__":
    main()
