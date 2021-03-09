alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

l = alphabet*2
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

if direction == "encode":
  def encrypt(b,c):
    result_decoded = ''
    for i in range(len(b)): 
      letter = b[i]
      if ' ' != letter:
        x = l.index(letter)
        y = int(c) + int(x)
        result_decoded += l[y]
      else:
        result_decoded += ' '
    return result_decoded

  print(encrypt(b=text,c=shift))

else:
  def decrypt(a,b):
    result_encoded = ''
    for letter in a:
      pos = l.index(letter)
      if ' ' != letter:
        pos_X = int(pos) - int(b)
        result_encoded += l[pos_X]
      else:
        result_encoded += ' '
    return result_encoded
  
  print(decrypt(a=text,b=shift))
