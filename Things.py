# from CeasseEncrypt import *
# from CeaserDecrypt import *
import imp
from pydoc import plain
from CeaserCipher import *
from Vigenère import *
from AESAlgo import *
from DESAlgo import *

# PlainText = input("Enter the plain Text: ")
# CeaserCipherKey = input("Enter the CeaserCipherKey: ")
# VignerCipherKey = input("Enter the CeaserCipherKey: ")
# DesCipherKey = input("Enter the CeaserCipherKey: ")
# AESCipherKey = input("Enter the Key: ")


PlainText = "I wandered lonely as a cloud That floats on."

VignerCipherKey = "asdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasd"
DesCipherKey = b'hello123'
AESCipherKey = b'Sixteen byte key'
CeaserCipherKey = len(VignerCipherKey)//3

# Key of ceaser cipher
# print("Ceaser Cipher key " + str(CeaserCipherKey))

# Step 1 
# Ceaser Cipher encryption

CeaserEncryptedText =  CeaserEncrypt(PlainText,CeaserCipherKey)
print("Step 1 Ceaser Cipher encryption :- "+CeaserEncryptedText)


# Step 2 AES encryption

AesEncrypttedText=AESEncryption(CeaserEncryptedText.encode(),AESCipherKey)
print("Step 2 AES encryption :- ")
print(AesEncrypttedText[1])
print("\n")

# Step 3 
# Decrypting received Plain text using AE

AesDecrypttedText = AESDEcryption(AesEncrypttedText[1],AESCipherKey,AesEncrypttedText[0])

print("Step 3 Decrypting received Plain text using AES")
print(AesDecrypttedText)
print("\n")

# Step 4 
# Decrypting output of AES with ceaser

CeaserDecryptedText = CeaserCipherDecrypt(AesDecrypttedText,CeaserCipherKey)
print("Step 4 Decrypting output of AES with ceaser")
print(CeaserDecryptedText)

print("\n\n")


# Key
# Step 1 for key 
# Encryption using Vigenere

# Vigner Cipher

dec=vigenere_encrypt(AESCipherKey.decode(),VignerCipherKey)
print("Step 1 for key Encryption using Vigenere :- "+dec)
# dectxt=vigenere_decrypt(dec,VignerCipherKey)
# print(dectxt)



# Step 2 for key 
# Encryption using DES

print("Step 2 for key Encryption using DES")
dest =DesEncrryption(dec.encode(),DesCipherKey)
print(dest)


# Step 3 for key
# Decrypt using DES

print("Step 3 for key Decrypt using DES")
dest1 =DesDecryption(dest,DesCipherKey)
print(dest1)

# Step 4 for key 
# Decryption of output of DES with vigenere

print("Step 4 for key Decryption of output of DES with vigenere")

dectxt=vigenere_decrypt(dest1.decode(),VignerCipherKey)
print(dectxt)

# For secret input
# from getpass import getpass
# password = getpass()