message = open('sometext.txt').read().upper().replace('\n', '')
key = (open('key.txt').read().replace('\n', ''))
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

a = int(input('Key position a: '))
b = int(input('Key position b: '))
c = int(input('Key position c: '))
d = int(input('Key position d: '))

inversenum = (a * d - b * c)

if inversenum % 2 == 0:
  print('ad-bc must not be even. Try again.')

index = 0
translated = ''
p1 = 0
p2 = 0

if len(message) % 2 != 0:
  message += 'X'
  
if len(key) != 4:
  print 'Your key must be four numbers in length'
  key = '0000'

index = 0
textindex = 0
c1 = 0
c2 = 0

while index < len(message):
  p1 = alphabet.find(message[index])
  p2 = alphabet.find(message[index + 1])
  index += 2
  translated += alphabet[(((a * p1) + (b * p2)) % 26)]
  translated += alphabet[(((c * p1) + (d * p2)) % 26)]
print translated