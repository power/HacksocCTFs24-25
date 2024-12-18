import random

def encrypt(plaintext, key):
  alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ{()}:@<>?~[];'#,./\|0123456789"
  ciphertext = ""
  """
  1. For each letter in the secret message (plaintext):
   a. Take the current letter (character).
   b. Add the letter (character) to the scrambled message (ciphertext).
   
   c. Repeat the following "key" number of times:
      i.  Pick a random letter from the alphabet.
      ii. Add the random letter to the scrambled message (ciphertext).
      
    2. Move on to the next letter in the secret message.

    3. Repeat this until you've done this for every letter in the secret message.
  """
  return ciphertext

def main():

    password = input("What's the secret password?")
    if password == chr(0x79) +chr(0x6f) +chr(0x75) +chr(0x5f) +chr(0x77) +chr(0x61) +chr(0x73) +chr(0x74) +chr(0x65) +chr(0x64) +chr(0x5f) +chr(0x61) +chr(0x6c) +chr(0x6c) +chr(0x5f) +chr(0x6f) +chr(0x66) +chr(0x5f) +chr(0x74) +chr(0x68) +chr(0x69) +chr(0x73) +chr(0x5f) +chr(0x74) +chr(0x69) +chr(0x6d) +chr(0x65) +chr(0x5f) +chr(0x66) +chr(0x6f) +chr(0x72) +chr(0x5f) +chr(0x73) +chr(0x6f) +chr(0x6d) +chr(0x65) +chr(0x74) +chr(0x68) +chr(0x69) +chr(0x6e) +chr(0x67) +chr(0x5f) +chr(0x79) +chr(0x6f) +chr(0x75) +chr(0x5f) +chr(0x63) +chr(0x6f) +chr(0x75) +chr(0x6c) +chr(0x64) +chr(0x5f) +chr(0x64) +chr(0x65) +chr(0x6c) +chr(0x65) +chr(0x74) +chr(0x65):        
        plaintext = input("Enter a message to encrypt (plaintext): ")
        key = int(input("Pick a number: "))
        ciphertext = encrypt(plaintext, key)

        print("Ciphertext:")
        print(ciphertext)

        # Make a decryption function so I can figure out my password if I ever lose this script.
    else:
       print("Wrong password!")

if __name__ == "__main__":
  main()
