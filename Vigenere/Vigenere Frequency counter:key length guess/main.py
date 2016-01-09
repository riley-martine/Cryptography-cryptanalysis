import pygal

message = open('sometext.txt').read().upper()

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ*'

index = 0
fullcount = 0
counter = [0] * len(alphabet)

while index < len(message):
  if message[index] in alphabet:
    counter[ alphabet.find(message[index]) ] += 1
    fullcount += 1
  index += 1

probsum = 0
letterindex = 0

print(message.find('ninau'))

while letterindex < 26:
  probsum += (counter[letterindex] * (counter[letterindex] - 1))/(fullcount * (fullcount -1))
  letterindex += 1
print probsum
r = (.027 * fullcount) / ((fullcount - 1) * probsum - 0.038 * fullcount + 0.065)
print('Guess for key length: ' + str(r))
bar_chart = pygal.Bar()
bar_chart.title = 'Letter Distribution'
bar_chart.x_labels = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z' ]
bar_chart.add('Ciphertext', counter)
bar_chart.render()

