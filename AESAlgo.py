from Crypto.Cipher import AES
def AESEncryption(text,key):
    cipher = AES.new(key, AES.MODE_EAX)

    # data to be encrypted
    # data = "Welcome to copyassignment.com!".encode()


    # encrypt the data
    ciphertext = cipher.encrypt(text)

    # print the encrypted data
    # print("Cipher text:", ciphertext)

    return cipher,ciphertext

# datec=enc(text,key)

def AESDEcryption(ctext,key,cipher):
    nonce = cipher.nonce
    cipher =  AES.new(key, AES.MODE_EAX, nonce)
    # decrypt the data
    plaintext = cipher.decrypt(ctext)
    print("Plain text:", plaintext.decode())

# dec(datec[1],key,datec[0])