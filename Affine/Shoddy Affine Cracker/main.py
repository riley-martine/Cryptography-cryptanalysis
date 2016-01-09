message = open('sometext').read().upper()
translated = ''

mode = 'decrypt' # encrypt or decrypt

akey = 2
mkey = 3

  
def findinverse(key):
  for test in range(0,26):
    if (test * key) % 26 == 1:
      return test
  print('No Key')
  return -1

minv = findinverse(mkey)

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


if mode == 'encrypt':
  for char in message:
    if char in alphabet:
      translated += (alphabet[ (alphabet.find(char) + akey) * mkey % 26 ] )
  print(translated)

if mode == 'decrypt':
  akey = 0
  while akey < 26:
    for char in message:
      if char in alphabet:
        translated += (alphabet[ ((alphabet.find(char) * minv) - akey ) % 26 ] )
    akey += 1
    print(translated + '\n')
    translated = ''