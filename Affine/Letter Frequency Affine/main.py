import pygal
message = open('sometext.txt').read().upper()
translated = ''
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
counter = [0] * 26
fullcount = 0
mkey = 3 
akey = 0

mode = 'decrypt' #encrypt, decrypt, ~~or crack~~

def findinverse(key):
  for test in range(0,26):
    if (test * key) % 26 == 1:
      return test
  print ('no inverse key')
  return -1
  


index = 0
keynew = 0
key = 3
cont = ''
while cont != '-1':
  cont = input('cont?')
  minv = findinverse(mkey)
  for char in message:
    if char in alphabet:
      translated += (alphabet[ ((alphabet.find(char) * minv ) - akey) % 26 ] )
  for char in translated:
    if char in alphabet:
      counter[ alphabet.find(char) ] += 1
      fullcount += 1
  
  
  check = 0
  
  for x in range (0, 26):
    counter[x] /= fullcount
    counter[x] *= 100
    check += counter[x]
  
  key += 2
  



  bar_chart = pygal.Bar()
  bar_chart.title = 'Letter Distribution'
  bar_chart.x_labels = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z' ]
  bar_chart.add('Ciphertext', counter)
  bar_chart.render()

"""
mode = 'decrypt' #crack or decrypt

key = 0

while key != -1:
  
  key = int(input('Key?'))
  
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
  translated = ''
"""