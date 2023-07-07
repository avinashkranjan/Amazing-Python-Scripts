# For caeser cipher the key size is fixed as: key = 3

import string

key = 3
# store all the alphabets in upper and lowercase in a String variable
all_letters = string.ascii_letters

# taking inputs
plain_txt = input("Enter the text you want to Encrypt: \n")
cipher_txt = []

# create a dictionary which maps the alphabets with respective substitution as per key size
dict1 = {}
for i in range(len(all_letters)):
    dict1[all_letters[i]] = all_letters[(i + key) % len(all_letters)]

# iterate through the plaintext characters and do necessary substittion
for char in plain_txt:
    if char in all_letters:
        temp = dict1[char]
        cipher_txt.append(temp)
    else:
        temp = char
        cipher_txt.append(temp)

# concatenate all the list elements
cipher_txt = "".join(cipher_txt)

# create a dictionary for reverse mapping
dict2 = {}
for i in range(len(all_letters)):
    dict2[all_letters[i]] = all_letters[(i - key) % (len(all_letters))]
decrypt_txt = []

for char in cipher_txt:
    if char in all_letters:
        temp = dict2[char]
        decrypt_txt.append(temp)
    else:
        temp = char
        decrypt_txt.append(temp)
decrypt_txt = "".join(decrypt_txt)

# display the Cipher Text and Recovered Plain Text
print("\nCipher Text is: ", cipher_txt)
print("Recovered plain text: ", decrypt_txt)
