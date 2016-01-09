message = 'hello'

arraything = [0] * len(message)
index = 0

def arrayify(message, arraything, index):
  for char in message:
    arraything[index] = message[index]
    index += 1
  return arraything

def dearrayify(message, arraything, index):
  message = ''
  for char in arraything:
    message += arraything[index]
    index += 1
  
arrayify(message, arraything, index)
print arraything
dearrayify(message, arraything, index)
print message
