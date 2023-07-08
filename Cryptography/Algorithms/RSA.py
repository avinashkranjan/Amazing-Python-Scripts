import math
import random


# Arguments provide range to generate two prime numbers
def primenumbers(srt, n):
    primenos = []
    prime = [True for i in range(n + 2 - srt)]
    prime[0] = False
    prime[1] = False
    for p in range(srt, int(math.sqrt(n)) + 1):
        if prime[p] == True:
            for i in range(p * p, n + 1, p):
                prime[i] = False
    for p in range(srt, n + 1):
        if prime[p]:
            primenos.append(p)
    P = random.choice(primenos)
    primenos.remove(P)
    Q = random.choice(primenos)
    return (P, Q)


# RSA Algorithm Implementation:
print("RSA Implementation starts for the connection")
for c in range(5):
    print("------")

p, q = primenumbers(1, 30)
N = p * q
f = (p - 1) * (q - 1)


# Generate Public Key for Encryption
def publickey():
    for i in range(2, f):
        if math.gcd(f, i) == 1:
            E = i
            break
    return E


E = publickey()


def privatekey():
    for j in range(1, N):
        if math.fmod((E * j), (f)) == 1:
            # if (E * j) % (f) == 1:
            D = j
            break
    return D


D = privatekey()
print("Generated Public Key for Encryption E: ", E)
print("Generated Private Key for Decryption D: ", D)
Plain_text = float(input("Enter Plain text in numerical data type: \n"))

x = math.pow(Plain_text, E)
Cipher_text = math.fmod(x, N)
print("Generated Cipher Text using Public Key: ", Cipher_text)

D_user = int(input("Enter your private key for Decryption \n"))
if D_user == D:
    y = math.pow(Cipher_text, D)
    Decrypted_text = math.fmod(y, N)
    print("The Cipher Text has been decrypted: ", Plain_text)
else:
    print("ENTERED WRONG PRIVATE KEY")
