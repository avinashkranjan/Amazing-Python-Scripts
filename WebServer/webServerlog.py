import re
from collections import Counter

# Regular expressions for parsing the Apache Combined Log Format
log_pattern = r'^(\S+) (\S+) (\S+) \[([\w:/]+\s[+\-]\d{4})\] "(\S+)\s?(\S+)?\s?(\S+)?" (\d{3}) (\d+|-)'


def parse_log(log_file_path):
    with open(log_file_path, 'r') as log_file:
        for line in log_file:
            match = re.match(log_pattern, line)
            if match:
                yield match.groups()


def analyze_logs(log_file_path):
    # Initialize counters and sets to store information
    total_requests = 0
    unique_visitors = set()
    page_visits = Counter()
    status_codes = Counter()
    potential_threats = set()

    for ip, _, _, _, _, _, url, status_code, _ in parse_log(log_file_path):
        total_requests += 1
        unique_visitors.add(ip)
        page_visits[url] += 1
        status_codes[status_code] += 1

        # Detect potential security threats (e.g., 404 errors from the same IP)
        if status_code.startswith('4'):
            potential_threats.add((ip, url))

    return total_requests, len(unique_visitors), page_visits, status_codes, potential_threats


if __name__ == "__main__":
    log_file_path = "path/to/your/log/file.log"

    total_requests, unique_visitors, page_visits, status_codes, potential_threats = analyze_logs(
        log_file_path)

    print(f"Total Requests: {total_requests}")
    print(f"Unique Visitors: {unique_visitors}")
    print("\nPopular Pages:")
    for page, count in page_visits.most_common(10):
        print(f"{page}: {count} visits")

    print("\nStatus Codes:")
    for code, count in status_codes.items():
        print(f"Status Code {code}: {count} occurrences")

    print("\nPotential Security Threats:")
    for ip, url in potential_threats:
        print(f"IP: {ip}, URL: {url}")
