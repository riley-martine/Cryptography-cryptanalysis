import pygal
message = open('sometext.txt').read().upper().replace('\n', '').replace(' ','')
key = open('key.txt').read().upper().replace('\n', '')

index = 0
translated = ''
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

mode = 'decrypt' #encrypt or decrypt

print('Key:        ' + key + '\n' + 'Message:    ' + message.replace(' ', ''))

if mode == 'encrypt':
  for char in message:
    if char in alphabet:
      translated += alphabet[ (alphabet.find(char) + alphabet.find(key[index % len(key)])) % 26]
      print translated
      translated = ''
      index += 1
indexa = 0
indexb = 0

if mode == 'decrypt':
  for char in message:
    if char in alphabet:
      translated += alphabet[ (alphabet.find(char) - alphabet.find(key[index % len(key)])) % 26]


if mode == 'crack':
  while indexa < 26:
    while indexb < 26:#^2:
      key = alphabet[indexa] + alphabet[indexb]
      for char in message:
        if char in alphabet:
           translated += alphabet[ (alphabet.find(char) - alphabet.find(key[index % len(key)])) % 26]
      index += 1
      indexb += 1
    indexb = 0
    indexa += 1
  

counter = [0] * 26
fullcount = 0
index = 0
rotations = 0

if mode == 'crack2':
  bar_chart = pygal.Bar()
  bar_chart.title = 'Letter Distribution'
  bar_chart.x_labels = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z' ]
  keylength = int(input('Key length?'))
  while rotations < keylength:
    while index < len(message):
      if message[index] in alphabet:
        counter[ alphabet.find(message[index]) ] += 1
        fullcount += 1
      index += keylength 
      rotations += 1
    bar_chart.add('message', counter)


if mode != 'crack': 
  print('Translated: ' + translated)


