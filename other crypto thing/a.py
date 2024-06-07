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
    if password == chr(0x79) +chr(0x6f) +chr(0x75) +chr(0x5f) +chr(0x77) +chr(0x61) +chr(0x73) +chr(0x74) +chr(0x65) +chr(0x64) +chr(0x5f) +chr(0x61) +chr(0x6c) +chr(0x6c) +chr(0x5f) +chr(0x6f) +chr(0x66) +chr(0x5f) +chr(0x74) +chr(0x68) +chr(0x69) +chr(0x73) +chr(0x5f) +chr(0x74) +chr(0x69) +chr(0x6d) +chr(0x65) +chr(0x5f) +chr(0x66) +chr(0x6f) +chr(0x72) +chr(0x5f) +chr(0x73) +chr(0x6f) +chr(0x6d) +chr(0x65) +chr(0x74) +chr(0x68) +chr(0x69) +chr(0x6e) +chr(0x67) +chr(0x5f) +chr(0x79) +chr(0x6f) +chr(0x75) +chr(0x5f) +chr(0x63) +chr(0x6f) +chr(0x75) +chr(0x6c) +chr(0x64) +chr(0x5f) +chr(0x64) +chr(0x65) +chr(0x6c) +chr(0x65) +chr(0x74) +chr(0x65):
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