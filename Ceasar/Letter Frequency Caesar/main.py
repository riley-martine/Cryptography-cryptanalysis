import pygal

message = open('sometext.txt').read().upper()

translated = ''

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

counter = [0] * len(alphabet)
fullcount = 0

for char in message:
  if char in alphabet:
    counter[ alphabet.find(char) ] += 1
    fullcount += 1

bar_chart = pygal.Bar()
bar_chart.title = 'Letter Distribution'
bar_chart.x_labels = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z' ]
bar_chart.add('Ciphertext', counter)
bar_chart.render()

mode = 'crack' #crack or decrypt

key = 0

while key != -1:
  
  key = (input('Key?'))
  
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