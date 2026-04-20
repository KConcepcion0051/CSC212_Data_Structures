#CSC 212 Kevin Concepcion
# This program defines an OrderedList class that implements a linked list data structure.
# The assignemnt given was to implement the following functions into the Orderlist class we learned 
# in class: index(item), pop(), pop_pos(pos), item_count(), del_rep() and then test those functions in the main function. 
from node import Node
import random

class OrderedList:
    '''
    List is empty upon creation and the head reference is None
    '''
    def __init__(self):
        self.head = None    
        
    '''
    Returns True if list is empty, False otherwise
    '''
    def is_empty(self):
        return self.head == None 
    
    '''
    Add an element to head of the list
    '''
    def add(self, item):
         # keep track of current and previous elements
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            # if we have a match, stop
            if current.get_data() > item:
                stop = True
            # otherwise advance current and next references
            else:
                previous = current
                current = current.get_next()
           
        # Create a node using item as its data
        temp = Node(item)
        if previous == None:
            temp.set_next(current)
            self.head = temp
                # the element to be deleted is not the head
        else:
            temp.set_next(current)
            previous.set_next(temp)
          
       
        
    '''
    Returns the size of the list
    '''
    def size(self):
        # start at the head of the list
        current = self.head
        count = 0
        # Traverse the list one element at a time.  We know
        # we reached the end when the next reference is None
        while current != None:
            count = count + 1
            current = current.get_next()
        return count

    '''
    Search for an item in the list.  Returns True if found, False otherise.  
    '''
    def search(self,item):
        current = self.head
        found = False
        stop=False
        # As long as the element is not found and we haven't 
        # reached the end of the list
        while current != None and not found and not stop:
            if current.get_data() == item:
                found = True
            else:
                if current.get_data()>item:
                    stop= True
                else:
                    # go to the next element
                    current = current.get_next()
        return found
    
    '''
    Remove the first occurrence of item from the list.  
    '''
    def remove(self, item):
        # keep track of current and previous elements
        current = self.head
        previous = None
        found = False
        # traverse the list 
        while current != None and not found:
            # if we have a match, stop
            if current.get_data() == item:
                found = True
            # otherwise advance current and next references
            else:
                previous = current
                current = current.get_next()
           
        # the element to be deleted is the head of the list     
        if found:
            if previous == None:
                self.head = current.get_next()
                # the element to be deleted is not the head
            else:
                previous.set_next(current.get_next())
                
    def print_list(self):
        print("[", end="")
        current = self.head
        while current != None:
            print(current.get_data(), end="")
            
        
            if current.get_next() != None:
                print(", ", end="")
            current = current.get_next()
        print("]")
        
   
   # ---------------------------------My class functions---------------------------------------------------------------------------


   
    # while we traverse the list we initiate the variable position as our counter and once our current.get_data() == the item then return the position.

    def index(self,item):
        position = 0
        current = self.head
        find= False
        
        while find != True:
            # if node == item return position
            if current.get_data() == item:
                print(f"Found {current.get_data()}, at index [{position}]")
                find = True
                return position
            else:
            # if node != item then we move to next node
                position += 1
                current = current.get_next()


    # traverse the list until the next reference is none, then we use our 'previous' variable to set next node to none getting rid of the last node in list
                
    def pop(self):
        current = self.head
        previous = None
        check = False
        
        while check != True:
            # if this is the last node in list then we use the previous pointer to do previous.set_next() to none deleting the last node
            if current.get_next() == None:
                previous.set_next(current.get_next())
                check = True
                return current.get_data()
            else:
            # otherwise we move both pointers to next node 
                previous = current
                current = current.get_next()

    # traverse the list and if the position counter == pos number then we return the current.get_data() then using the 'previous' varible we set the next node reference to the next one is list, removing the node at position( pos )
    
    def pop_pos(self,pos):
        position = 0
        current = self.head
        previous = None

        while current != None:
            # if position == pos we remove the current node
            if position == pos:
                previous.set_next(current.get_next())
                return current.get_data()
            else:
            # other wise we move to next node and +1 to position counter
                previous = current
                current = current.get_next()
            position += 1
    
    
    # traverse the list and count each occurance of the node value

    def item_count (self):
        current = self.head
        temp = current.get_data()
        count = 0


        while current != None:
            # if the node == same value then we add 1 to our counter
            if current.get_data() == temp:
                count += 1
                current = current.get_next()
            else:
            # once new node value is reach we print out the count 
                print(f"The current item : {temp} has count of {count}")
                # reset for the next node value
                temp = current.get_data()
                count = 1 
                current = current.get_next()
        #print count for the last node in list
        print(f"The current item : {temp} has count of {count}")
        
    # traverse the list and delete replicated node values

    def del_rep(self):
        current = self.head
        #stops comparing once the next node is none
        while current.get_next() != None:
            # temp is looking at next node
            temp = current.get_next()
            # if there is duplicate then we remove that node
            if current.get_data() == temp.get_data():
                current.set_next(temp.get_next())
            else:
            # if not dupe then we move on to next node
                current = current.get_next()
                         
                
                
def main():
    alist = OrderedList()
    
    print("Creating 15 random integers in the range 1 - 5 and adding to the list")
    for i in range(15):
        num = random.randint(1,5)
        alist.add(num)
    
    print("Linked list display :", end = "")
    alist.print_list()

    # since the integer values are random indexing head 
    value = random.randint(1,5)
    alist.index(value)


    print(f"The popped value is {alist.pop()}")

    value_1 = random.randint(1,5)
    print(f"Popping node with value {value_1}")
    alist.pop_pos(value)
    
    print("List display :", end = "")
    alist.print_list()

    print("Current count for each node value ")
    alist.item_count()

    print("Removing duplicates")
    alist.del_rep()
    alist.print_list()


main()

    