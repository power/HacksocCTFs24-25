import random

def encrypt(plaintext, key):
  alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ{()}:@<>?~[];'#,./\|0123456789"
  ciphertext = ""
  for i in range(0, len(plaintext)):
    character = plaintext[i]
    ciphertext = ciphertext + character
    for j in range(0, key):
      ciphertext = ciphertext + random.choice(alphabet)
  return ciphertext

def decrypt(ciphertext, key):
    #Code goes here!
    return 

def main():

    password = input("What's the secret password?")
    if password == chr(0x68) + chr(0x34) + chr(0x63) + chr(0x6b) + chr(0x33) + chr(0x72) + chr(0x21) + chr(0x21):
        plaintext = input("Enter a message to encrypt (plaintext): ")
        key = int(input("Pick a number: "))
        ciphertext = encrypt(plaintext, key)

        print("Ciphertext:")
        print(ciphertext)

        decrypted_text = decrypt(ciphertext, key)
        print("Decrypted text:")
        print(decrypted_text)
    else:
       print("Wrong password!")

if __name__ == "__main__":
  main()