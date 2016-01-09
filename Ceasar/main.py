message = open('sometext.txt').read().upper()
translated = ''

key = 5 

mode = 'decrypt' #encrypt or decrypt

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

if mode == 'encrypt':
  for char in message:
    if char in alphabet:
      translated += (alphabet[ (alphabet.find(char) + key) % 26 ] )

if mode == 'decrypt':
  for char in message:
    if char in alphabet:
      translated += (alphabet[ (alphabet.find(char) - key) % 26 ] )
      
if mode == 'crack':
  key = 0
  while key < 26:
    for char in message:
      if char in alphabet:
        translated += (alphabet[ (alphabet.find(char) - key) % 26] )
    print str(key) + '\n' + translated
    translated = ''
    key += 1
      
print(translated)