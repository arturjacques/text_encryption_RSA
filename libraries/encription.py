from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA

class Encrypt:
    def __init__(self):
        pass

    def read_public_key(self, path):
        self.public_key = RSA.import_key(open(path).read())

    def set_private_key_path(self, path):
        self.private_key_path = path

    def encrypt_string(self, text):
        text_binary = text.encode("utf-8")
        session_key = get_random_bytes(16)

        # Encrypt the session key with the public RSA key
        cipher_rsa = PKCS1_OAEP.new(self.public_key)
        enc_session_key = cipher_rsa.encrypt(session_key)

        # Encrypt the data with the AES session key
        cipher_aes = AES.new(session_key, AES.MODE_EAX)
        ciphertext, tag = cipher_aes.encrypt_and_digest(text_binary)

        text_encrypted = list()
        text_encrypted.append(enc_session_key)
        text_encrypted.append(cipher_aes.nonce)
        text_encrypted.append(tag)
        text_encrypted.append(ciphertext)
        return text_encrypted

    def decrypt_data(self, data):
        enc_session_key = data[0]
        nonce = data[1]
        tag = data[2]
        ciphertext = data[3]

        private_key = RSA.import_key(open(self.private_key_path).read())

        # Decrypt the session key with the private RSA key
        cipher_rsa = PKCS1_OAEP.new(private_key)
        session_key = cipher_rsa.decrypt(enc_session_key)

        # Decrypt the data with the AES session key
        cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
        data = cipher_aes.decrypt_and_verify(ciphertext, tag)
        return (data.decode("utf-8"))

    def generate_keys(size=1024, secret = 'Secret'):
        secret_code = secret
        key = RSA.generate(1024)
        private_key = key.export_key()
        public_key = key.publickey().export_key()


        return {'public_key': public_key, 'private_key':private_key}

