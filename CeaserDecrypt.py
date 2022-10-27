import string

alphabet = string.ascii_lowercase # "abcdefghijklmnopqrstuvwxyz"

def CeaserCipherDecrypt(text,k):
    
    # print("Welcome to Caesar Cipher Decryption.\n")
    # encrypted_message = input("Enter the message you would like to decrypt: ").strip()
    # print()
    # key = int(input("Enter key to decrypt: "))
    
    decrypted_message = ""

    for c in text:

        if c in alphabet:
            position = alphabet.find(c)
            new_position = (position - k) % 26
            new_character = alphabet[new_position]
            decrypted_message += new_character
        else:
            decrypted_message += c

    print("Your decrypted message is:\n")
    print(decrypted_message)
    return decrypted_message
