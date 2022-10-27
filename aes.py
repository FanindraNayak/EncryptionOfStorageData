# importing AES
# installing pycryptodome
from Crypto.Cipher import AES

# encryption key
key = b'Sixteen byte key'
text =  b'hello from other side'
# # create new instance of cipher
# cipher = AES.new(key, AES.MODE_EAX)

# # data to be encrypted
# # data = "Welcome to copyassignment.com!".encode()


# # encrypt the data
# ciphertext = cipher.encrypt(text)

# # print the encrypted data
# print("Cipher text:", ciphertext)

# generate new instance with the key and nonce same as encryption cipher
# cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
# nonce = cipher.nonce
# cipher =  AES.new(key, AES.MODE_EAX, nonce)
# # decrypt the data
# plaintext = cipher.decrypt(ciphertext)
# print("Plain text:", plaintext.decode())

def enc(text,key):
    cipher = AES.new(key, AES.MODE_EAX)

    # data to be encrypted
    # data = "Welcome to copyassignment.com!".encode()


    # encrypt the data
    ciphertext = cipher.encrypt(text)

    # print the encrypted data
    print("Cipher text:", ciphertext)

    return cipher,ciphertext

datec=enc(text,key)

def dec(ctext,key,cipher):
    nonce = cipher.nonce
    cipher =  AES.new(key, AES.MODE_EAX, nonce)
    # decrypt the data
    plaintext = cipher.decrypt(ctext)
    print("Plain text:", plaintext.decode())

dec(datec[1],key,datec[0])