# CSC 212-01 Kevin Concepcion 10/24/25
# This program defines a Queue class with methods that demonstrate how Queue can be used
import random

class Queue:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def enqueue(self, item):
        self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
    def print_queue(self):
        for item in self.items:
            print(item, end=" ")
        print()
        
        
def getSum(q):
    sum = 0
    for i in range(q.size()):
        val = q.dequeue()
        sum += val
        q.enqueue(val)
    return sum

def hotpotato(names,num):
    q=Queue()
    for name in names:
        q.enqueue(name)
        
    q.print_queue()
        
    while q.size() > 1:
        random_passes = random.randint(1,num)  # Random number of passes between 1 and num
        for i in range(random_passes):
            player=q.dequeue()
            q.enqueue(player)
        eliminated=q.dequeue()
        print(f"{eliminated} was caught with potatoe and is eliminated!")
    
    return q.dequeue()

def main():
    print("Hot potato game\nPlayers: ", end="")
    names = ["Kevin","Kelsey","Keylin"]
    num = 10
    s= hotpotato(names,num)
    
    print("Winner is: " + s)
    
    print("\nTesting Queue Operations:")
    q = Queue()
    
    print(q.is_empty())  # If the queue is empty, it should return True. If not, then False.
    
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    
    print("Current Queue: ", end="")
    q.print_queue()
    
    print("Current Sum of Queue: ", end="")
    s = getSum(q)
    print(s)
    
    print("Current Queue: ", end="")
    q.print_queue()
main()