import string

alphabet = string.ascii_lowercase # "abcdefghijklmnopqrstuvwxyz"

def CeaserCipherDecrypt(text,k):
    
    decrypted_message = ""

    for c in text:

        if c in alphabet:
            position = alphabet.find(c)
            new_position = (position - k) % 26
            new_character = alphabet[new_position]
            decrypted_message += new_character
        else:
            decrypted_message += c

    # print("Your decrypted message is:\n")
    # print(decrypted_message)
    return decrypted_message
