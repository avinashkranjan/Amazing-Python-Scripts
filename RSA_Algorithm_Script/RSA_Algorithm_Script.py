def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def multiplicative_inverse(a, b):
    s1, s2, m = 1, 0, b
    while b != 0:
        q, r = divmod(a, b)
        a, b = b, r
        s1, s2 = s2, s1 - q * s2
    return s1 % m


def powermod(x, y, p):
    res = 1
    x = x % p
    while y > 0:
        if y % 2 == 1:
            res = (res * x) % p
        y //= 2
        x = (x * x) % p
    return res


def main():
    while True:
        res = input(
            'Do you want to enter prime numbers (y) or let the algorithm do it for you (n) or exit (e)? (y/n/e): ')
        if res == 'y':
            while True:
                p = int(input('Enter a prime number: '))
                if is_prime(p):
                    break
                else:
                    print(p, 'is not a prime number')

            while True:
                q = int(input('Enter a different prime number: '))
                if is_prime(q) and p * q > 26:
                    break
                else:
                    print(
                        'Both prime numbers are the same or the product is less than 26!')

            n = p * q
            phi_n = (p - 1) * (q - 1)

            while True:
                a = int(
                    input(f'Enter a number such that Greatest Common Divisor with {phi_n} is 1: '))
                if gcd(a, phi_n) != 1:
                    continue
                else:
                    break

            b = multiplicative_inverse(a, phi_n)
            message = input(
                'Enter the message to be encrypted (lower case): ').lower()

            encrypted_string = ""
            encrypted_num = []

            for ch in message:
                if ch != ' ':
                    m = ord(ch) - 97
                    e = powermod(m, a, n)
                    encrypted_num.append(e)
                    encrypted_string += chr(e % 26 + 97)
                else:
                    encrypted_string += ' '

            print('Encrypted message is:', encrypted_string)
            res = input("Do you want to decrypt it too? (y/n): ")
            if res == 'y':
                decrypted = ''
                j = 0
                for ch in encrypted_string:
                    if ch != ' ':
                        e = encrypted_num[j]
                        m = powermod(e, b, n)
                        ch = chr(m + 97)
                        decrypted += ch
                        j += 1
                    else:
                        decrypted += ' '

                print("Decrypted message is:", decrypted)
            else:
                ans = input("Do you want to continue? (y/n): ")
                if ans == 'y':
                    continue
                else:
                    break
        elif res == 'n':
            p, q, a, b = 13, 17, 5, 77
            n = p * q
            message = input(
                'Enter the message to be encrypted (lower case): ').lower()

            encrypted_string = ""
            encrypted_num = []

            for ch in message:
                if ch != ' ':
                    m = ord(ch) - 97
                    e = powermod(m, a, n)
                    encrypted_num.append(e)
                    encrypted_string += chr(e % 26 + 97)
                else:
                    encrypted_string += ' '

            print('Encrypted message is:', encrypted_string)
            res = input("Do you want to decrypt it too? (y/n): ")
            if res == 'y':
                decrypted = ''
                j = 0
                for ch in encrypted_string:
                    if ch != ' ':
                        e = encrypted_num[j]
                        m = powermod(e, b, n)
                        ch = chr(m + 97)
                        decrypted += ch
                        j += 1
                    else:
                        decrypted += ' '

                print("Decrypted message is:", decrypted)
            else:
                ans = input("Do you want to continue? (y/n): ")
                if ans == 'y':
                    continue
                else:
                    break
        elif res == 'e':
            break
        else:
            print('Invalid command!')
            continue


if __name__ == '__main__':
    main()
