import pyotp
import argparse
import json

SECRET_STORAGE_FILE = "secret.json"


def generate_totp(secret_key, algorithm='SHA1', digits=6, interval=30):
    totp = pyotp.TOTP(secret_key, digits=digits,
                      interval=interval, digest=algorithm)
    return totp.now()


def verify_totp(secret_key, code, algorithm='SHA1', digits=6, interval=30, window=1):
    totp = pyotp.TOTP(secret_key, digits=digits,
                      interval=interval, digest=algorithm)
    return totp.verify(code, valid_window=window)


def save_secret(secret_key, filename):
    data = {'secret_key': secret_key}
    with open(filename, 'w') as file:
        json.dump(data, file)
    return f'Secret key saved to {filename}'


def load_secret(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            return data['secret_key']
    except FileNotFoundError:
        print(f'Secret key file "{filename}" not found.')
        return None


def main():
    parser = argparse.ArgumentParser(
        description='Multi-Factor Authentication (MFA) Generator')
    parser.add_argument('--generate', action='store_true',
                        help='Generate a TOTP code')
    parser.add_argument('--verify', help='Verify a TOTP code')
    parser.add_argument(
        '--algorithm', choices=['SHA1', 'SHA256', 'SHA512'], default='SHA1', help='Hash algorithm for TOTP')
    parser.add_argument(
        '--digits', type=int, choices=[6, 8], default=6, help='Number of digits in TOTP code')
    parser.add_argument('--interval', type=int, default=30,
                        help='Time interval for TOTP code generation')
    parser.add_argument('--window', type=int, default=1,
                        help='Verification window for TOTP codes')
    parser.add_argument('--save', help='Save secret key to a file')
    parser.add_argument('--load', action='store_true',
                        help='Load secret key from a file')
    args = parser.parse_args()

    if args.load:
        secret_key = load_secret(SECRET_STORAGE_FILE)
        if secret_key is None:
            return
    elif args.generate or args.verify:
        secret_key = input('Enter your secret key: ').strip()
        if args.save:
            save_result = save_secret(secret_key, args.save)
            print(save_result)
    else:
        print('Please specify either --generate or --verify.')
        return

    if args.generate:
        code = generate_totp(secret_key, args.algorithm,
                             args.digits, args.interval)
        print(f'Generated TOTP code: {code}')

    if args.verify:
        code_to_verify = args.verify
        result = verify_totp(secret_key, code_to_verify,
                             args.algorithm, args.digits, args.interval, args.window)
        if result:
            print('TOTP code is valid.')
        else:
            print('TOTP code is NOT valid.')


if __name__ == '__main__':
    main()
