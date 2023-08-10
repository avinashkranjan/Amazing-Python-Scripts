import re

def filter_text(text, pattern):
    filtered_text = re.findall(pattern, text)
    return filtered_text

def main():
    sample_text = """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit.
    Phone numbers: +1 (123) 456-7890, 555-1234, 9876543210
    Emails: john.doe@example.com, jane_smith@gmail.com
    """

    # Filter phone numbers
    phone_pattern = r'\+?1? ?\(\d{3}\) ?\d{3}-\d{4}|\d{10}'
    phone_numbers = filter_text(sample_text, phone_pattern)
    print("Phone numbers found:")
    print(phone_numbers)

    # Filter emails
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = filter_text(sample_text, email_pattern)
    print("\nEmail addresses found:")
    print(emails)

if __name__ == "__main__":
    main()