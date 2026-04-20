#csc 212 Kevin Concepcion 11/7/25
# This program defines a Deque class with methods that demonstrate how Deque can be used
class Deque:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def add_front(self, item):
        self.items.append(item)
    def add_rear(self, item):
        self.items.insert(0,item)
    def remove_front(self):
        return self.items.pop()
    def remove_rear(self):
        return self.items.pop(0)
    def size(self):
        return len(self.items)
    def print_deque(self):
        for item in self.items:
            print(item, end=" ")
        print()      
    
# Steps for palindrone checker using deque
# step 1 create a deque
# step 2 add all characters from a string into the deque
# step 3 loop until first = get first item, = last " " = first " " 
#                   if missmatch return false

def palin_check(word):
    d = Deque()
    
    for i in word:
        d.add_front(i)
    
    while d.size() > 1:
        first = d.remove_rear()
        last = d.remove_front()
        if first != last:
            return False
    return True
            
         
        

def main():
    d = Deque()
    
    word = input("Enter your word : ")
    print(palin_check(word))
    
    if palin_check(word) == True:
        print("Word is palindrone")
    else:
        print("Word is not palindrone")
    
    print("\nTesting Deque Operations:\n")
    d_size = d.size()
    print("The deque size is : ",d_size)
    print("Is deque empty? ", end="")
    print(d.is_empty())
    d.add_front(3)
    d.add_rear("pumpkin")
    d.add_front(4)
    
    print("Removing all elements in deque from front:")
    for i in range(d.size()):
        print(d.remove_front())
    print("The deque size is : ",d_size)
    
    d.add_rear(10)
    d.add_front("purple")
    print("Is deque empty? ", end="")
    print(d.is_empty())
    print("Current deque size ", end="")
    print(d.size())
    d.add_front(7)
    d.add_rear(20)
    d.add_front("Haloween")
    
    
    print("Current Deque: ", end="")
    d.print_deque()
    print("Removing from front value. ", d.remove_front())
  
    print("Removing from rear value. ", d.remove_rear())
    print("Printing removed items from front of deque: \n", end="")
    while not d.is_empty():
        print(d.remove_front(),end=" ")
    print("\nCurrent Deque size: " , d_size)
    
main()
    