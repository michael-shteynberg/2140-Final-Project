from crypto import *
from GUI import *







window.mainloop()








"""


def start():
    choice = input("Would you like to encrypt or decrypt (e/d)?")
    if choice == "e":
        encrypt()
    elif choice == "d":
        decrypt()
    else:
        start()


def encrypt():
    
    data = input("Enter text to encrypt: ")
    password = input("Enter password to encrypt text: ")
    key = deriveKey(password, 32, salt)
    token = sym_encrypt(data, key)
    #print("Key:", key)
    print("Encrypted text:", token)

def decrypt():
    token = input("Enter encrypted text: ")
    password = input("Enter password: ")
    key = deriveKey(password, 32, salt)
    data = sym_decrypt(token, key)

    print(data)

start()
"""