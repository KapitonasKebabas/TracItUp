from base64 import b64decode
from Cryptodome.Cipher import AES
from Crypto.Util.Padding import unpad

def decrypt_password(encrypted_value, key):
    chiper = AES.new(key.encode(), AES.MODE_ECB)
    return unpad(chiper.decrypt(b64decode(encrypted_value.encode())), 16).decode()
