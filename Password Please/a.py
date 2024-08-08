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
    original_text = ''.join([ciphertext[i] for i in range(0, len(ciphertext), key)])
    return original_text

def main():
    ciphertext = input("Input the text: ")
    key = 0
    for i in range(100):
      key = key + 1
      decrypted_text = decrypt(ciphertext, key)
      if (decrypted_text[:7] == "HACKSOC"):
         print (decrypted_text)
         break
      else:
         continue

if __name__ == "__main__":
  main() 