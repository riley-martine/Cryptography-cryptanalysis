message = input("Input your message to be railfenced here:\n")
workingtext = message #text that is being worked on
rows = input("How many rows would you like to be used? [0-infinity(theoretically)]: \n")
rows = int(rows)
index = 0 #where in the text we are working on
rotcount = 0 #how many letters we have worked, mod 5 
store = '' #store strings here
translated = '' #ciphertext

workingtext = workingtext.upper() #capitalizes all text, bonus #1 achieved

for characters in workingtext:   #for every character in the text
  if workingtext[index] != ' ': #if the current character is not a space
    store += workingtext[index] #store it in the store
  index += 1 #add one to where we are in the text and repeat

#we now have a text with no spaces, bonus #2 achieved

index = 0 #reset index to 0
workingtext = store #set the workingtext to what we have in the store
store = '' #reset the store to blank
rotcount = 0 #reset rotcount to 0

import string #import this library
exclude = set(string.punctuation) #not gonna lie, I copy pasted this bit from stackoverflow
workingtext = ''.join(ch for ch in workingtext if ch not in exclude) #otherwise I would have a chain of if's that was really long

#text has no punctuation, bonus #3 achieved

for x in range(0, rows): #for as many rows as you enter
  while index < len(workingtext): #inside loop- while pointer is in text
    store += workingtext[index] #store the thing you're on
    index += rows # go up by the same number as the number of rows
  index = rotcount + 1 #set index to 1 higher than before
  rotcount = index #make sure index score persists
  
#look at that super awesome code /\
#ok not really but it lets you do 3 row (and more) so bonus #4 achieved
  
workingtext = store #make the workingtext what we have in the store

translated = workingtext  #move workingtext to finished translated variable
print translated #print the translated thing

#known issue- newline characters are not filtered out.