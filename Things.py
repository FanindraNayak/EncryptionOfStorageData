# from CeasseEncrypt import *
# from CeaserDecrypt import *
import imp
from pydoc import plain
from CeaserCipher import *
from Vigenère import *


from AESAlgo import *

# text = "dasdasdasdasdasdasdasdasdasda"
# s = 4

# PlainText = input("Enter the plain Text: ")
# CeaserCipherKey = input("Enter the CeaserCipherKey: ")
# VignerCipherKey = input("Enter the CeaserCipherKey: ")
# DesCipherKey = input("Enter the CeaserCipherKey: ")
# AESCipherKey = input("Enter the Key: ")


PlainText = "I wandered lonely as a cloud That floats on."

VignerCipherKey = "asdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasd"
DesCipherKey = "\0\0\0\0\0\0\0\0"
AESCipherKey = b'Sixteen byte key'
CeaserCipherKey = len(VignerCipherKey)//3
# Key of ceaser cipher
print("Ceaser Cipher key " + str(CeaserCipherKey))

# From NIS py File
# Ceaser Cipher encrypt
# print("Shift pattern : " + str(CeaserCipherKey))
# print("Cipher: " + CeaserEncrypt(text,CeaserCipherKey))

CeaserEncryptedText =  CeaserEncrypt(PlainText,CeaserCipherKey)
# print("E :- "+CeaserEncryptedText)

# Fromm CeaserCipherDecrypt Py file
CeaserDecryptedText = CeaserCipherDecrypt(CeaserEncryptedText,CeaserCipherKey)


# Vigner Cipher

dec=vigenere_encrypt(PlainText,VignerCipherKey)
# print(dec)
dectxt=vigenere_decrypt(dec,VignerCipherKey)
# print(dectxt)



# AES
AesEncrypttedText=AESEncryption(CeaserEncryptedText.encode(),AESCipherKey)
print("Aes encrypted text")
print(AesEncrypttedText[1])
print("\n")

AesDecrypttedText = AESDEcryption(AesEncrypttedText[1],AESCipherKey,AesEncrypttedText[0])
# print(CeaserEncryptedText)
print("Aes decrypted text")
print(AesDecrypttedText)
print("\n")
CeaserDecryptedText = CeaserCipherDecrypt(AesDecrypttedText,CeaserCipherKey)
print(CeaserDecryptedText)
