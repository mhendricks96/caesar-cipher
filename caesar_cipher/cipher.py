import nltk
from nltk.corpus import words, names
nltk.download('words', quiet=True)
nltk.download('names', quiet=True)



word_list = words.words()
#name_list = names.words()


def encrypt(plain_text, key):
  result = ''
  #print(f"plain text: {plain_text}")
  
  #result = ""
  
  for i in range(len(plain_text)):
    char = plain_text[i]
    
    if char.isupper():
      result += chr((ord(char) + key - 65) % 26 + 65)

    else:
      result += chr((ord(char) + key - 97) % 26 + 97)

  return result

def decrypt(encoded, key):
  return encrypt(encoded, - key)


def crack(encrypted_text):
  encrypted_words = encrypted_text.split()
  most_common = 0
  likely_key = 0

  for i in range(1, 26):
    count = 0
    for word in word_list:
      if decrypt(word, i) in word_list:
        count += 1

    if count > most_common:
      most_common = count
      likely_key = i

  probability = most_common / len(encrypted_words) * 100
  result = decrypt(encrypted_text, likely_key)

  print(f"Probablility of correct decryption: {probability}")
  print(f"alleged key: {likely_key}")

  return result



if __name__ == "__main__":
  #print(encrypt('2345', 7))
  plain_text = "Nikola Jokic is MVP"
  key = 8
  print(f"plain text: {plain_text}")
  print(f"key: {key}")
  print(f"encrypted: {encrypt(plain_text, key)}")

  encrypted = encrypt(plain_text, key)

  testing = crack(encrypted)
  print(testing)
