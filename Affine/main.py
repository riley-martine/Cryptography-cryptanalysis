message = open('sometext.new').read().upper()
translated = ''

mkey = 7 
akey = 5

mode = 'decrypt' #encrypt, decrypt, ~~or crack~~

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def findinverse(key):
  for test in range(0,26):
    if (test * key) % 26 == 1:
      return test
  print ('no inverse key')
  return -1

if mode == 'encrypt':
  for char in message:
    if char in alphabet:
      translated += (alphabet[ ((alphabet.find(char) + akey) * mkey) % 26 ] )

if mode == 'decrypt':
  minv = findinverse(mkey)
  for char in message:
    if char in alphabet:
      translated += (alphabet[ ((alphabet.find(char) * minv ) - akey) % 26 ] )
      
#if mode == 'crack':
#  key = 0
#  while key < 26:
#    for char in message:
#      if char in alphabet:
#        translated += (alphabet[ (alphabet.find(char) - key) % 26] )
#    print str(key) + '\n' + translated
#    translated = ''
#    key += 1
      
print(translated)