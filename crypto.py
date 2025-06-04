import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

salt = b"thesalt"

class symCrypt:

    def encrypt(self, data, password):
        key = deriveKey(password, 32, salt)
        token = sym_encrypt(data, key)
        return token

    def decrypt(self, token, password):
        key = deriveKey(password, 32, salt)
        data = sym_decrypt(token, key)
        return data

#returns a new generated a 32-byte fernet key for symmetric encryption
def generateSymKey():
    key = Fernet.generate_key()
    return key.decode('ascii')

#returns encrypted data using a key with the fernet symmetric encryption algorithm
def sym_encrypt(data, key):
    data = data.encode('ascii')
    key = key.encode('ascii')

    f = Fernet(key)
    return f.encrypt(data).decode('ascii')

#returns decrypted data using a key with the fernet symmetric encryption algorithm
def sym_decrypt(token, key):
    token = token.encode('ascii')
    key = key.encode('ascii')

    f = Fernet(key)
    return f.decrypt(token).decode('ascii')

#derives a key from a password string
def deriveKey(password, length, salt):
    kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=length,
    salt=salt,
    iterations=480000,
    )

    #key = kdf.derive(password.encode('ascii'))
    key = base64.urlsafe_b64encode(kdf.derive(password.encode('ascii')))

    return key.decode('ascii')


#Old stuff that isn't being used rn
"""
The Crypto class contains 3 main pieces of info:

Data - the raw unencrypted text of a message
Key - the key used for encryption of a message
Token - the encrypted version of the message


"""
"""#This is symmetric encryption using the fernet algorithm
class Crypto:

    #you can set the data of the Crypto object when you instantiate the class if you want
    def __init__(self, data = ""):
        self.data = data.encode('ascii')
        self.key = Crypto.generateFernetKey()

    #reads a file and sets self.data to the content of the file
    def readFile(self, file_name):
        with open(file_name, "r", encoding="ascii") as file:
            self.data = file.read().encode('ascii')
    
    #generates a 32-byte fernet key for symmetric encryption
    def generateFernetKey():
        key = Fernet.generate_key()
        return key
    
    #sets self.key to the key you input
    def setKey(self, key):
        self.key = key

    def setToken(self, token):
        self.token = token

    #converts data to token using set key
    def encrypt(self):
        f = Fernet(self.key)
        self.token = f.encrypt(self.data)
    
    #converts token to data using set key
    def decrypt(self):
        f = Fernet(self.key)
        self.data = f.decrypt(self.token)



class sym:
        #converts data to token using set key
        def encrypt(self):
            f = Fernet(self.key.encode('ascii'))
            self.token = f.encrypt(self.data.encode('ascii')).decode('ascii')
        
        #converts token to data using set key
        def decrypt(self):
            f = Fernet(self.key)
            self.data = f.decrypt(self.token)"""