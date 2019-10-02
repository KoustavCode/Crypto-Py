import sys
from termcolor import cprint
from cryptography.fernet import Fernet

charset="utf-8"

def enc(message):
    key=Fernet.generate_key()
    e=Fernet(key)
    message=message.encode(charset)
    ciphertext=e.encrypt(message)
    return ciphertext,key

def dec(cipher):
    key=input("Enter the key to decrypt: ")
    key=key.encode(charset)
    d=Fernet(key)
    message=d.decrypt(cipher.encode(charset))
    return message

if __name__ == "__main__":
    print("[1] To encrypt")
    print("[2] To decrypt")
    choice=int(input(">>"))
    if choice==1:
        message=input("Enter the plain text here to encrypt: ")
        ciphertext,key=enc(message)
        print("Encrypted text: "+ciphertext.decode(charset))
        print("Key: "+key.decode(charset))
    elif choice==2:
        cipher=input("Enter the message to decrypt: ")
        result=dec(cipher)
        print(result)
    else:
        cprint("Invalid option. Please select a valid option.",'red',attrs=['bold'])
        cprint("Exiting.....",'red',attrs=['bold'])