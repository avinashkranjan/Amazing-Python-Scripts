# IPTV Link Tester - Comprehensive Edition

A robust Python tool for testing and validating IPTV M3U stream links using multiple verification methods.

## Features

- **Multiple Testing Methods**: Uses 5 different approaches to verify stream availability
  - HTTP HEAD requests
  - HTTP GET with partial content
  - HTTP streaming test
  - Socket connection verification
  - FFmpeg/FFprobe analysis (optional)
  
- **Retry Logic**: Tests each link 5 times per method for reliability
- **Detailed Reporting**: Shows real-time progress and success rates
- **Automatic Sorting**: Separates working and broken links into different files
- **Success Rate Tracking**: Records the percentage of successful tests for each link

## Requirements

- Python 3.6 or higher
- FFmpeg/FFprobe (optional, but recommended for better accuracy)

## Installation

1. Clone or download this repository

2. Install required Python packages:
```bash
pip install -r requirements.txt
```

3. (Optional) Install FFmpeg for enhanced testing:
   - **Windows**: Download from [ffmpeg.org](https://ffmpeg.org/download.html)
   - **macOS**: `brew install ffmpeg`
   - **Linux**: `sudo apt-get install ffmpeg` or `sudo yum install ffmpeg`

## Usage

1. Create a file named `iptv_links.txt` in the same directory as the script

2. Add your IPTV links (one per line):
```
http://example.com:8080/live/stream1/index.m3u8
http://example.com:8080/live/stream2/index.m3u8
http://example.com:8080/live/stream3/index.m3u8
```

3. Run the script:
```bash
python iptv_tester.py
```

4. Wait for the testing to complete. The script will:
   - Test each link thoroughly with multiple methods
   - Show real-time progress and results
   - Save working links to `working_links.txt`
   - Save broken links to `broken_links.txt`

## Configuration

You can customize the testing parameters by modifying the `IPTVLinkTester` class initialization:

```python
tester = IPTVLinkTester(
    input_file='iptv_links.txt',    # Input file with links
    working_file='working_links.txt', # Output file for working links
    broken_file='broken_links.txt'    # Output file for broken links
)

# Modify these attributes:
tester.timeout = 20     # Timeout per request (seconds)
tester.attempts = 5     # Number of attempts per test method
```

## Output Files

### working_links.txt
Contains all links that passed at least one test, along with their success rate:
```
http://example.com/stream1.m3u8 # Success rate: 85.0%
http://example.com/stream2.m3u8 # Success rate: 92.0%
```

### broken_links.txt
Contains links that failed all tests:
```
http://example.com/dead_stream.m3u8 # All tests failed
```

## Testing Process

For each link, the script performs:
- 5 attempts × 5 test methods = 25 total tests per link
- Automatic delays between attempts to avoid rate limiting
- A link is marked as "working" if ANY test succeeds

### Test Methods Explained

1. **HTTP HEAD Request**: Quick check if the server responds
2. **HTTP GET Partial**: Downloads first 1KB to verify data availability
3. **HTTP Streaming**: Attempts to stream multiple chunks of data
4. **Socket Connection**: Verifies basic network connectivity
5. **FFmpeg Probe**: Uses FFmpeg to analyze stream metadata (if available)

## Estimated Time

- Testing time depends on:
  - Number of links
  - Network speed
  - Server response times
  
- Approximate calculation: `(Number of links × 5 methods × 5 attempts × 3 seconds) / 60 minutes`
- Example: 10 links ≈ 12-15 minutes

## Troubleshooting

### All links showing as broken
- Check your internet connection
- Verify the links are valid and currently active
- Some IPTV providers may block automated testing
- Try reducing the number of attempts or increasing timeout

### Script running very slowly
- This is normal due to thorough testing
- You can reduce `attempts` or `timeout` for faster results (less accurate)
- Some servers may have rate limiting

### FFmpeg tests always fail
- FFmpeg is not installed or not in PATH
- This is optional; other methods can still validate links

## Notes

- Some IPTV providers implement anti-scraping measures
- Links may work for real players but fail automated tests
- False positives/negatives are possible
- Always respect the terms of service of IPTV providers
- This tool is for personal use and legitimate testing only

## License

Free to use for personal and educational purposes.

## Disclaimer

This tool is intended for testing your own IPTV subscriptions and legally obtained streams. Users are responsible for ensuring they have the right to access and test the streams they provide to this tool.
