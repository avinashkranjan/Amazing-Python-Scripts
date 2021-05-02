from Algos.Encrypt import Encrypt
from Algos.Decrypt import Decrypt

"""
   [NOTE] Here we demostrate an use of the Encrypt and Decrypt algorithms 
   We also play the audio file as well.
"""
# You can try with Forest.wav as well
message_path = input("Enter path of Audio file: ")
secret_path = input("Enter path of Secret message file")

# Using Encrypt
en = Encrypt(message_path, secret_path)
en.play_audio()
res, status = en.encrypt_using_lsb("Encrypted", "encrypted.wav")

if status:
    print(res)

# Using Decrypt
dec = Decrypt("Encrypted\encrypted.wav")
dec.play_audio()
res, status = dec.decrypt_audio("Decrypted", "decrypted.txt")

if status:
    print(res)
