# from CeasseEncrypt import *
# from CeaserDecrypt import *
# import imp
# from pydoc import plain
# from getpass import getpass

import time

timestamp1 = time.time()
timestamp = int(timestamp1)
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
        arr = []

        CeaserEncryptedText =  CeaserEncrypt(PlainText,CeaserCipherKey)
        print("\n")
        print("---------------  ENCRYPTION  ---------------",timestamp)
        print("\n")
        print("Plain Text after Ceaser Cipher Encryption : \n",timestamp)
        print(CeaserEncryptedText)
        print("\n")
        arr.append("---------------  ENCRYPTION  ---------------")
        arr.append(timestamp)
        arr.append("Plain Text after Ceaser Cipher Encryption : \n")
        arr.append(timestamp)
        arr.append("\n")
        arr.append(CeaserEncryptedText)
        
        # Step 2 AES encryption

        AesEncrypttedText=AESEncryption(CeaserEncryptedText.encode(),AESCipherKey)
        print("Encrypted Plain Text obatined after AES encryption : \n")
        print(AesEncrypttedText[1])
        print("\n")
        arr.append("\n\n")
        arr.append("Encrypted Plain Text obatined after AES encryption : \n")
        arr.append(timestamp)
        arr.append("\n")
        strg=str(AesEncrypttedText[1])
        arr.append(strg)
        
        
        # Step 3 for key Encryption using Vigenere

        dec=vigenere_encrypt(AESCipherKey.decode(),VignerCipherKey)
        print("Key after Vigenere Encryption: \n")
        print(dec)
        print("\n")
        arr.append("\n\n")
        arr.append("Key after Vigenere Encryption: \n")
        arr.append(timestamp)
        arr.append("\n")
        arr.append(dec)

        # Step 4 for key Encryption using DES

        dest =DesEncrryption(dec.encode(),DesCipherKey)
        print("Key obtained from DES Encryption: \n")
        print(dest)
        print("\n")
        arr.append("\n\n")
        arr.append("Key obtained from DES Encryption: \n")
        arr.append("\n")
        arr.append(timestamp)
        strg1=str(dest)
        arr.append("\n")
        arr.append(strg1)
        # print(arr)
        return dest,AesEncrypttedText,arr


    def dec(AesEncrypttedText,CeaserCipherKey,DesCipherKey,dest,VignerCipherKey):
        arrD = []
        print("---------------  DECRYPTION  ---------------")
        print("\n")
        arrD.append("---------------  DECRYPTION  ---------------\n")
        # Step 1 Decrypting received Plain text using AES

        AesDecrypttedText = AESDEcryption(AesEncrypttedText[1],AESCipherKey,AesEncrypttedText[0])

        print("Decrypting received Plain text using AES: \n")
        print(AesDecrypttedText)
        print("\n")
        arrD.append("Decrypting received Plain text using AES: \n")
        arrD.append(timestamp)
        arrD.append("\n")
        arrD.append(AesDecrypttedText)

        # Step 2 Decrypting output of AES with ceaser

        CeaserDecryptedText = CeaserCipherDecrypt(AesDecrypttedText,CeaserCipherKey)
        print("Original Plain Text: \n")
        print(CeaserDecryptedText)
        print("\n")
        arrD.append("Original Plain Text: \n")
        arrD.append(timestamp)
        arrD.append("\n")
        arrD.append(CeaserDecryptedText)

        # Step 3 for key Decrypt using DES

        print("Decrypting Key using DES: \n")
        dest1 =DesDecryption(dest,DesCipherKey)
        print(dest1)
        print("\n")
        arrD.append("Decrypting Key using DES: \n")
        arrD.append(timestamp)
        arrD.append("\n")
        strG =str(dest1)
        arrD.append(strG)

        # Step 4 for key Decryption of output of DES with vigenere

        print("Secret Key: \n")
        dectxt=vigenere_decrypt(dest1.decode(),VignerCipherKey)
        print(dectxt)

        arrD.append("Secret Key: \n")
        arrD.append(timestamp)
        arrD.append("\n")
        arrD.append(dectxt)

        return dest1,arrD


    dest=enc(PlainText,CeaserCipherKey,AESCipherKey,VignerCipherKey,DesCipherKey)


    deDest=dec(dest[1],CeaserCipherKey,DesCipherKey,dest[0],VignerCipherKey)

    return dest[2],deDest[1]


def openFile():
    tf = filedialog.askopenfilename(
        initialdir="C:/Users/MainFrame/Desktop/", 
        title="Open Text file", 
        filetypes=(("Text Files", "*.txt"),)
        )
    pathh.insert(END, tf)
    tf = open(tf)  # or tf = open(tf, 'r')
    data = tf.read().splitlines()
    data1 = tf.read()
    print(data)
    newDAta=func(data[0],data[1],data[2],data[3])
    # newData1 = newDAta[0].split(",")
    things_To_add = newDAta[0]+newDAta[1]
    print(things_To_add)
    print(newDAta[0])
    txtarea.insert(END, things_To_add)
    tf.close()
    return data


def saveFile():
    tf = filedialog.asksaveasfile(
        mode='w',

        title ="Save file",
        defaultextension=".txt"
        )
    # tf.config(mode='w')

    # pathh.insert(END, tf)
    if tf is None:
        return

    data = str(txtarea.get(1.0, END))
    tf.write(data)
   
    tf.close()


ws = Tk()
ws.title("PythonGuides")
ws.geometry("400x450")
ws['bg']='#fb0'
# adding frame
frame = Frame(ws)
frame.pack(pady=20)

# adding scrollbars 
ver_sb = Scrollbar(frame, orient=VERTICAL )
ver_sb.pack(side=RIGHT, fill=BOTH)

hor_sb = Scrollbar(frame, orient=HORIZONTAL)
hor_sb.pack(side=BOTTOM, fill=BOTH)

# adding writing space
txtarea = Text(frame, width=40, height=20)
txtarea.pack(side=LEFT)

# binding scrollbar with text area
txtarea.config(yscrollcommand=ver_sb.set)
ver_sb.config(command=txtarea.yview)

txtarea.config(xscrollcommand=hor_sb.set)
hor_sb.config(command=txtarea.xview)

pathh = Entry(ws)
pathh.pack(side=LEFT, expand=True, fill=X, padx=20)



Button(
    ws, 
    text="Open File", 
    command=openFile
    ).pack(side=RIGHT, expand=True, fill=X, padx=20)

Button(
    ws, 
    text="Save File", 
    command=saveFile
    ).pack(side=LEFT, expand=True, fill=X, padx=20)

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


