message= input('What is the text:') #input plaintext
message= message.upper().replace(' ', '') #this will make your message all caps and remove spaces
key = int(input('What is the key:')) #input key
translated = '' #define translated
store = '' #define store
index = 0 # define index
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' #import alphabet

import string #import this library
exclude = set(string.punctuation) #not gonna lie, I copy pasted this bit from stackoverflow
message = ''.join(ch for ch in message if ch not in exclude) #otherwise I would have a chain of if's that was really long

for letter in message: #for every letter in the message
  store = (LETTERS.find(message[index]) + key) % 26 #take the letter and find it's number counterpart, then add the key, mod 26
  translated += LETTERS[store] #convert the number to a letter and add it to the translated
  index += 1 #add one to the index  

#index = 0 # reset index
#store = ''
#store = str(store)
#translated = str(translated)
#rotcount = 0

#print type(store)
#print type(translated)
#print type(index)

#for char in translated:
#  if rotcount == 5:
 #   print 'hello'
 #   translated += '_'
  #  rotcount = 1
  #  store += translated[index]
#  else:
 #   print 'goodbye'
 #   index += 1
 #   rotcount += 1
 #   store += translated[index]
  
  
print(translated) #print ciphertext