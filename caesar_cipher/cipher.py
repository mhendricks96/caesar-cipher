def encrypt(plain_text, shift_key):
  result = ''
  print(plain_text)
  
  #result = ""
  
  for char in plain_text:
    num = int(char)
    shifted_num = num + shift_key
    if shifted_num > 9:
      shifted_num = shifted_num % 10
    result += str(shifted_num)
  return result

if __name__ == "__main__":
  print(encrypt('2345', 7))