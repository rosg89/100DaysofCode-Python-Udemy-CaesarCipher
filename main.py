alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#Print logo
from art import logo
print(logo)

should_continue = True

while should_continue:
  
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  
  #Por si ponen un numero muy alto en el shift
  shift = shift % 26 
  
  #Encrypt function
  def encrypt(plain_text, shift_amount):
    cipher_text = "" 
    for letter in plain_text:
      #Se fija si es letra u otro caracter
      if letter in alphabet:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        cipher_text += new_letter
      #Si es otro caracter lo agrega sin fijarse en la lista de alphabet
      else:
        cipher_text += letter
    print(f"The encoded text is {cipher_text}")
  
  #Decrypt function
  def decrypt(cipher_text, shift_amount):
    plain_text = ""
    for letter in cipher_text:
      if letter in alphabet:
        #Index
        position = alphabet.index(letter)
        #Le cambia la posición
        new_position = position - shift_amount
        #Lo arma de nuevo
        plain_text += alphabet[new_position]
      else:
        plain_text += letter
    print(f"The decoded text is {plain_text}")
  
  
  #Call the functions
  if direction == "encode":
    encrypt(plain_text = text,shift_amount= shift)
  elif direction == "decode":
    decrypt(cipher_text = text, shift_amount = shift)
  
  result = input("Type 'yes' if you want to go again. Otherwise type 'no'\n")
  
  if result == "no":
    should_continue = False
    print("Goodbye")

