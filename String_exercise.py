# Assigment 1 - Kevin Concepcion CSC 212-01. Strings
# Goal : create a program that prompts the user to enter two inputs( some text and a word).
#The program outputs the starting indencies of all occurances of the word in the text. 

sentence = input("Type your sentence:")     # Holds the user's sentence
word = input("Type your word:")             # Gets the user's word that we will search for
position=[]                                 # Empty list to hold the indecies position number for the search word

start = 0                                   # Starts the word search at the very begining of sentence

while True:                                 # While loop that will be repeated until no more words are found
    index = sentence.find(word,start)       # The find method takes first parameter as substring and the second one as the start
    if index == -1:                         # This breaks the while loop if the word isnt found
        break
    else:
        position.append(index)              # When the word is found its index position while be recorded in the position list we made
    start = index + 1                       # When a word is found the the search will move one character to the right to search for the next

if position:                                # If the position list is populated it will print its contents
    print(position)
else:                                       # If no words are found "Word not found" gets printed
    print("Word not found")