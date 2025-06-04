from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend


class AsymKey:
    def __init__(self,keysize=1024):
        self.private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=keysize,
            backend=default_backend()
        )
        self.public_key = self.private_key.public_key()

    def serialize_private(self,password=None):
        if password is None:
            encryption_algorithm = serialization.NoEncryption()
        else:
            encryption_algorithm = serialization.BestAvailableEncryption(password.encode())

        return self.private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=encryption_algorithm
        )
    
    def serialize_public(self):
        return self.public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
    
    def key_to_file(self,datakey,file_path):
        with open(file_path,'wb') as file:
            file.write(datakey)

    def save_private(self,file_path,password=None):
        datakey=self.serialize_private(password=password)
        self.key_to_file(datakey,file_path)

    def save_public(self,file_path):
        datakey=self.serialize_public()
        self.key_to_file(datakey,file_path)
    

keyJack = AsymKey()
keyJack.save_private('private_key_jack.pem',password="Jack")
keyJack.save_public("public_key_jack.pem")

keyMicheal = AsymKey()
keyMicheal.save_private('private_key_micheal.pem',password="Jack")
keyMicheal.save_public("public_key_micheal.pem")

keyBen = AsymKey()
keyBen.save_private('private_key_ben.pem',password="Jack")
keyBen.save_public("public_key_ben.pem")




        