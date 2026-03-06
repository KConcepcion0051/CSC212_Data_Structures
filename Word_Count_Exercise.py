# Kevin Concepcion Word Count Exercise (given a sentence)


sentence= input("Type your first sentence:")   # gets the sentence from user
words = sentence.split()                       # splits the words in the user's sentence and held in varibable called words
counts = {}                                    # empty dictionary to hold the words of sentence ** not same as list

for w in words:                                # This loop goes through each word in sentence and counts each accurance of word and stores in dictionary
    counts[w] = counts.get(w,0) + 1



print()                                        # Just a space before output

for w, c in counts.items():                    # The loop returns the words and its assigned value from the dictionary
    print(w,c)                                 # then prints out the word and count seperatly