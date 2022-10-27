from CeasseEncrypt import *
from CeaserDecrypt import *

text = "CEASER CIPHER DEMO"
s = 4

# PlainText = input("Enter the plain Text: ")
# CeaserCipherKey = input("Enter the CeaserCipherKey: ")
# VignerCipherKey = input("Enter the CeaserCipherKey: ")
# DesCipherKey = input("Enter the CeaserCipherKey: ")
# AESCipherKey = input("Enter the Key: ")


PlainText = "asd"
VignerCipherKey = "asdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasd"
DesCipherKey = "asd"
AESCipherKey = "asd"
CeaserCipherKey = len(VignerCipherKey)//3
print(CeaserCipherKey)

# From NIS py File
# Ceaser Cipher encrypt
print("Shift pattern : " + str(CeaserCipherKey))
print("Cipher: " + CeaserEncrypt(text,CeaserCipherKey))

# Fromm CeaserCipherDecrypt Py file
CeaserCipherDecrypt(text,CeaserCipherKey)

