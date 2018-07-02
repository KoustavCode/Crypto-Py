
from Crypto import Random
from Crypto.Cipher import AES
import base64
import random


BS = 16


def pad(s): return s + (BS - len(s) % BS) * chr(BS - len(s) % BS)


def unpad(s): return s[0:-ord(s[-1:])]



key = ''
key = [key + str((random.randint(0, 9))) for _ in range(16)]
key = ''.join(key)
print (key)


def encrypt(text):
    text = pad(text)
    # padding of the input text is done to match the byte length of 16
    IV = Random.new().read(AES.block_size)
    # having a random Initialization vector adds unique randomess to the start of the encryption process
    cipher = AES.new(key, mode=AES.MODE_CBC, IV=IV)
    cipher_text = cipher.encrypt(text)
    key1 = key.encode('utf-8')
    base_value = base64.b64encode(IV + key1 + cipher_text)
    return base_value


def decrypt(cipher_text):
    cipher_text = base64.b64decode(cipher_text)
    IV = cipher_text[:16]
    key = cipher_text[16:32]
    key = key.decode('utf-8')
    data = cipher_text[32:]
    decryptor = AES.new(key, mode=AES.MODE_CBC, IV=IV)
    plain_text = decryptor.decrypt(data)
    print (plain_text)
    return unpad(plain_text)


if __name__ == "__main__":

    text = "koustav1234Chand"
    ciphertext = encrypt(text)
    print (ciphertext)
    actualtext = decrypt(ciphertext)
    print(actualtext)
