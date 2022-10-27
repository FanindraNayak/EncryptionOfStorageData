# from CeasseEncrypt import *
# from CeaserDecrypt import *
import imp
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
AESCipherKey = b"C&F)H@McQfTjWnZr"
CeaserCipherKey = len(VignerCipherKey)//3
print(CeaserCipherKey)

# From NIS py File
# Ceaser Cipher encrypt
# print("Shift pattern : " + str(CeaserCipherKey))
# print("Cipher: " + CeaserEncrypt(text,CeaserCipherKey))

CeaserEncryptedText =  CeaserEncrypt(PlainText,CeaserCipherKey)
# print("E :- "+CeaserEncryptedText)

# Fromm CeaserCipherDecrypt Py file
CeaserDecryptedText = CeaserCipherDecrypt(CeaserEncryptedText,CeaserCipherKey)

print("D :- "+ CeaserDecryptedText)

# Vigner

dec=vigenere_encrypt(PlainText,VignerCipherKey)
# print(dec)
dectxt=vigenere_decrypt(dec,VignerCipherKey)
# print(dectxt)



# AES
AesEncrypttedText=AESEncryption(CeaserEncryptedText.encode(),AESCipherKey)
print(AesEncrypttedText)

AesDecrypttedText = AESDEcryption(AesEncrypttedText[1],AESCipherKey,AesEncrypttedText[0])
print(CeaserEncryptedText)

CeaserDecryptedText = CeaserCipherDecrypt(AesDecrypttedText,CeaserCipherKey)
print(CeaserDecryptedText)
