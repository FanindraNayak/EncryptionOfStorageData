import hashlib
m = hashlib.sha512()
#plain text goes into this m.update command
def sha(txt):
    enTxt=txt.encode()
    print(enTxt)
    m.update(enTxt)
    # m.update(b" the spammish repetition")
    return m.digest()

# sha("the spammish repetition")