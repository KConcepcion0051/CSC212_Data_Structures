# Assigment 1 - Kevin Concepcion CSC 212-01
# This program will take a list of numbers and ignore all the numbers between 6 and 7, including the 6 and 7. Then it will print the sum of the remaining numbers in the list.


list=[1,1,3,6,8,9,9,7,1]    #Sample data list
temp=[]                     #Holds the value that come before 6 and after 7(nothing inbetween)
ignoring = False            #This variable will be our "checker". Set to false because function will check for 6 before starting to ignore


for i in list:                  # This loop iterates each number in order
    if not ignoring and i == 6: # In the iterations, if the number is 6 set the "checker to true" 
        ignoring = True         # when false the number will be added to our temp list, on true the number will be ignored
        continue                # The number after and including 6 will be skipped until a 7 is found in the list
    
    if ignoring:
        if i == 7:              # while the "checker" variable is set to to true every number in the list will be skipped until a 7 is found
            ignoring = False
        continue
    
    if ignoring == False:       # All the numbers the was checked while our varibable was set to false will be added to our temp list.
        temp.append(i)
print(temp)                     # showing contents of list 
print(sum(temp))                # Printing sum of list