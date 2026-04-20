# Implementation of an Unordered List ADT as a linked list.  The list
# is accessed through a reference to the first element, head.  
# Adopted from Section 3.9 of the textbook.

from node import Node

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

#def main():
    # alist = OrderedList()
    
    # alist.add(5)
    # alist.add(9)
    # alist.remove(5)
    # alist.print_list()
    # alist.add(1)
    # print(alist.size())
    
#main()
    

          


