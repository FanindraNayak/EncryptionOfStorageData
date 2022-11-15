# from CeasseEncrypt import *
# from CeaserDecrypt import *
# import imp
# from pydoc import plain
# from getpass import getpass


from Ceaser import *
from Vigenère import *
from AES import *
from DES import *

from tkinter import *
from tkinter import filedialog

def func(PlainText,VignerCipherKey,c,d):
    
    # PlainText = "I wandered lonely as a cloud That floats on."

    # VignerCipherKey = "asdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasd"

    # DesCipherKey = b'hello123'

    # AESCipherKey = b'Sixteen byte key'
    PlainText = "I wandered lonely as a cloud That floats on."

    VignerCipherKey = "asdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasd"

    DesCipherKey = c.encode()

    AESCipherKey = d.encode()

    CeaserCipherKey = len(VignerCipherKey)//3

    def enc(PlainText,CeaserCipherKey,AESCipherKey,VignerCipherKey,DesCipherKey):
        # Step 1 Ceaser Cipher encryption

        CeaserEncryptedText =  CeaserEncrypt(PlainText,CeaserCipherKey)
        print("\n")
        print("---------------  ENCRYPTION  ---------------")
        print("\n")
        print("Plain Text after Ceaser Cipher Encryption : \n")
        print(CeaserEncryptedText)
        print("\n")
        
        # Step 2 AES encryption

        AesEncrypttedText=AESEncryption(CeaserEncryptedText.encode(),AESCipherKey)
        print("Encrypted Plain Text obatined after AES encryption : \n")
        print(AesEncrypttedText[1])
        print("\n")
        
        # Step 3 for key Encryption using Vigenere

        dec=vigenere_encrypt(AESCipherKey.decode(),VignerCipherKey)
        print("Key after Vigenere Encryption: \n")
        print(dec)
        print("\n")

        # Step 4 for key Encryption using DES

        dest =DesEncrryption(dec.encode(),DesCipherKey)
        print("Key obtained from DES Encryption: \n")
        print(dest)
        print("\n")

        return dest,AesEncrypttedText


    def dec(AesEncrypttedText,CeaserCipherKey,DesCipherKey,dest,VignerCipherKey):
        print("---------------  DECRYPTION  ---------------")
        print("\n")

        # Step 1 Decrypting received Plain text using AES

        AesDecrypttedText = AESDEcryption(AesEncrypttedText[1],AESCipherKey,AesEncrypttedText[0])

        print("Decrypting received Plain text using AES: \n")
        print(AesDecrypttedText)
        print("\n")

        # Step 2 Decrypting output of AES with ceaser

        CeaserDecryptedText = CeaserCipherDecrypt(AesDecrypttedText,CeaserCipherKey)
        print("Original Plain Text: \n")
        print(CeaserDecryptedText)
        print("\n")

        # Step 3 for key Decrypt using DES

        print("Decrypting Key using DES: \n")
        dest1 =DesDecryption(dest,DesCipherKey)
        print(dest1)
        print("\n")

        # Step 4 for key Decryption of output of DES with vigenere

        print("Secret Key: \n")
        dectxt=vigenere_decrypt(dest1.decode(),VignerCipherKey)
        print(dectxt)

        return dest1


    dest=enc(PlainText,CeaserCipherKey,AESCipherKey,VignerCipherKey,DesCipherKey)


    dec(dest[1],CeaserCipherKey,DesCipherKey,dest[0],VignerCipherKey)


def openFile():
    tf = filedialog.askopenfilename(
        initialdir="C:/Users/MainFrame/Desktop/", 
        title="Open Text file", 
        filetypes=(("Text Files", "*.txt"),)
        )
    pathh.insert(END, tf)
    tf = open(tf)  # or tf = open(tf, 'r')
    data = tf.read().splitlines()
    print(data)
    func(data[0],data[1],data[2],data[3])
    tf.close()
    return data

ws = Tk()
ws.title("PythonGuides")
ws.geometry("400x450")
ws['bg']='#fb0'


pathh = Entry(ws)
pathh.pack(side=LEFT, expand=True, fill=X, padx=20)



Button(
    ws, 
    text="Open File", 
    command=openFile
    ).pack(side=RIGHT, expand=True, fill=X, padx=20)


ws.mainloop()


# PlainText = input("Enter the plain Text: ")
# VignerCipherKey = input("Enter the VignerCipherKey: ")
# DesCipherKey1 = input("Enter the DesCipherKey: ")
# AESCipherKey2 = input("Enter the AESCipherKey: ")
# DesCipherKey=DesCipherKey1.encode()
# AESCipherKey=AESCipherKey2.encode()

# Sample Inpute

PlainText = "I wandered lonely as a cloud That floats on."

VignerCipherKey = "asdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasd"

DesCipherKey = b'hello123'

AESCipherKey = b'Sixteen byte key'

CeaserCipherKey = len(VignerCipherKey)//3

def enc(PlainText,CeaserCipherKey,AESCipherKey,VignerCipherKey,DesCipherKey):
    # Step 1 Ceaser Cipher encryption

    CeaserEncryptedText =  CeaserEncrypt(PlainText,CeaserCipherKey)
    print("\n")
    print("---------------  ENCRYPTION  ---------------")
    print("\n")
    print("Plain Text after Ceaser Cipher Encryption : \n")
    print(CeaserEncryptedText)
    print("\n")
    
    # Step 2 AES encryption

    AesEncrypttedText=AESEncryption(CeaserEncryptedText.encode(),AESCipherKey)
    print("Encrypted Plain Text obatined after AES encryption : \n")
    print(AesEncrypttedText[1])
    print("\n")
    
    # Step 3 for key Encryption using Vigenere

    dec=vigenere_encrypt(AESCipherKey.decode(),VignerCipherKey)
    print("Key after Vigenere Encryption: \n")
    print(dec)
    print("\n")

    # Step 4 for key Encryption using DES

    dest =DesEncrryption(dec.encode(),DesCipherKey)
    print("Key obtained from DES Encryption: \n")
    print(dest)
    print("\n")

    return dest,AesEncrypttedText


def dec(AesEncrypttedText,CeaserCipherKey,DesCipherKey,dest,VignerCipherKey):
    print("---------------  DECRYPTION  ---------------")
    print("\n")

    # Step 1 Decrypting received Plain text using AES

    AesDecrypttedText = AESDEcryption(AesEncrypttedText[1],AESCipherKey,AesEncrypttedText[0])

    print("Decrypting received Plain text using AES: \n")
    print(AesDecrypttedText)
    print("\n")

    # Step 2 Decrypting output of AES with ceaser

    CeaserDecryptedText = CeaserCipherDecrypt(AesDecrypttedText,CeaserCipherKey)
    print("Original Plain Text: \n")
    print(CeaserDecryptedText)
    print("\n")

    # Step 3 for key Decrypt using DES

    print("Decrypting Key using DES: \n")
    dest1 =DesDecryption(dest,DesCipherKey)
    print(dest1)
    print("\n")

    # Step 4 for key Decryption of output of DES with vigenere

    print("Secret Key: \n")
    dectxt=vigenere_decrypt(dest1.decode(),VignerCipherKey)
    print(dectxt)

    return dest1


dest=enc(PlainText,CeaserCipherKey,AESCipherKey,VignerCipherKey,DesCipherKey)


dec(dest[1],CeaserCipherKey,DesCipherKey,dest[0],VignerCipherKey)


