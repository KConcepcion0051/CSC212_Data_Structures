#Kevin Concepcion CSC 212 Assignment 5

# This program defines a Stack class with methods to check if the stack is empty, 
# push an item onto the stack, pop an item from the stack, peek at the top item of 
# the stack, and get the size of the stack. It also includes two functions: palin_check, 
# which checks if a given word is a palindrome using a stack, and num_check, which 
# takes a stack of integer numbers and returns the maximum value in the stack while 
# keeping the original order of the numbers. The main function tests both of these functions.

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

#Function that checks if the user's word is a palindrome and returns True or False                          # Write a Python function that takes a user input of a word and returns True if it is a 
def palin_check(word):                                                                                      # Palindrome and returns False otherwise (Your function should use a Stack data structure).  
    s = Stack()                                                                                             # A palindrome is a word that can be read the same backward as forward. Some examples 
    check = ""                                                                                              # of palindromic words are noon, civic, radar, level, rotor, kayak, reviver, racecar, redder,madam, and refer.

    for i in word:
        s.push(i)
    while not s.isEmpty():
        check += s.pop()
    
    if word == check:
        print("True")
        return True
    else:
        print("False")
        return False
    
#Function that takes the Max value of the stack of integer numbers then returns the 
#stack in the original order. Keeping the same numbers as before
def num_check(num_stack):                                                                                   # Write a Python function that takes a stack of integer numbers and returns the maximum 
    temp_stack = Stack()                                                                                             # value of the numbers in the stack. The stack should have the same numbers before and 
    
    find = num_stack.pop()
    temp_stack.push(find)

    x = []
    
    while not num_stack.isEmpty():
        val = num_stack.pop()
        temp_stack.push(val)
        if val > find:
            find = val


    while not temp_stack.isEmpty():
        pri = temp_stack.pop()
        x.append(pri)
        num_stack.push(pri)
    print("The original stack: ", x)
    print("The max value in the stack is :",find)

    
#Main that test both functions
def main():
    word = input("Enter your word : ")
    
    if palin_check(word) == True:
        print("Your word is a Palindrome")
    else:
        print("Your word is not a Palindrome")

    num_stack = Stack()
    num_stack.push(10)
    num_stack.push(3)
    num_stack.push(14)
    num_stack.push(5)
    num_stack.push(13)
    
    num_check(num_stack)
    
main()