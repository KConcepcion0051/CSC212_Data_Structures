#Recurvise Summation example

def listsum(alist):
    if len(alist) == 1:
        return alist[0]
    else:
        return alist[0] + listsum(alist[1:])
        
    
    
# 1. Base case 
# 2. function in terms of itself the recursive call use a smaller size of the data structure to reahc the base case 
# 3. function calls itself
#  sum (alist)= first.item + sum(alist.without.first.item)