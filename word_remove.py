# Kevin Concepcion
# This program will remove the word "my" from the user's sentence and print the new sentence without "my"

sentence = "my name is Amy and my friend name is Amy too that is fun"
words = sentence.split()                       # splits the words in the user's sentence and held in varibable called words
counts = words.count("my")                                   # counts the amount of times "my" in in the varibale words

print(words)

for w in range(counts):
    words.remove("my")
print(words)


