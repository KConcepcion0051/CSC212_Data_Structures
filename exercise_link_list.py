# CSC 212 Kevin Concepcion 11/14/25
# This program defines an UnorderedList class that implements a linked list data structure. 
# It includes methods for adding, searching, removing, and printing elements in the list. 
# The main function demonstrates how to use the UnorderedList class by adding some elements 
# and printing the list.

from node import Node

class UnorderedList:
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
        # Create a node using item as its data
        temp = Node(item)
        # make the next reference of the new node refer to the head 
        # of the list
        temp.set_next(self.head)
        # modify the list head so that it references the new node
        self.head = temp
        
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
        # As long as the element is not found and we haven't 
        # reached the end of the list
        while current != None and not found:
            if current.get_data() == item:
                found = True
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
        



def main():
    aList = UnorderedList()
    print("Adding 3, 5, 8, and 11 to the list.")
    aList.add(3)
    aList.add(5)
    aList.add(8)
    aList.add(11)
    
    aList.print_list()
main()
