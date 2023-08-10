# Multi-Factor Authentication (MFA) Generator Script

This is a Python script that provides a command-line interface for generating and verifying Time-Based One-Time Passwords (TOTPs) for Multi-Factor Authentication (MFA). The script uses the `pyotp` library for TOTP calculations.

## Features

- Generate TOTP codes using different hash algorithms, code lengths, and time intervals.
- Verify TOTP codes and set a verification window for code validity.
- Save and load secret keys from JSON files for easier management.

## Prerequisites

Before using the script, make sure you have Python installed. You can install the required `pyotp` library using the following command:

```bash
pip install pyotp
```

## Usage

1. Generate TOTP Code

To generate a TOTP code, run:

```bash
python multi_factor_auth.py --generate --algorithm SHA1 --digits 6 --interval 30
```

2. Verify TOTP Code

To verify a TOTP code, run:

```bash
python multi_factor_auth.py --verify CODE_TO_VERIFY --algorithm SHA1 --digits 6 --interval 30 --window 1
```

Replace CODE_TO_VERIFY with the TOTP code you want to verify.

3. Save and Load Secret Keys

To save a secret key to a JSON file, run:

```bash
python multi_factor_auth.py --save secret.json
```

To load a secret key from a JSON file, run:
```bash
python multi_factor_auth.py --load
```

## Options

- --generate: Generate a TOTP code.
- --verify: Verify a TOTP code.
- --algorithm: Choose hash algorithm (SHA1, SHA256, SHA512).
- --digits: Set number of digits in TOTP code (6 or 8).
- --interval: Set time interval for TOTP code generation.
- --window: Set verification window for TOTP codes.
- --save: Save secret key to a JSON file.
- --load: Load secret key from a JSON file.

## Example

Generate a TOTP code:

```bash
python multi_factor_auth.py --generate --algorithm SHA256 --digits 8 --interval 60
```

Verify a TOTP code:

```bash
python multi_factor_auth.py --verify 123456 --algorithm SHA256 --digits 8 --interval 60 --window 2
```

## Note

This script is provided for educational purposes. When using it for real-world applications, make sure to follow security best practices and ensure proper handling of secret keys.

## Contributing

If you have any ideas, improvements, or bug fixes, feel free to open an issue or submit a pull request. We appreciate your contributions!
