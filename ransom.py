# Assigment 2 - Kevin Concepcion CSC 212-01
# This program will determine if the characters in the short string can be found in the long string.

def ransom(long,short):
    # Dictionary for the long string
    check_L = {}
    for i in long:
        check_L[i] = check_L.get(i,0) + 1
        
    # Dictionary for the short string
    check_S = {}
    for i in short:
        check_S[i] = check_S.get(i,0) + 1

    # Compare the characters if characters in short exceed amount of char in long it will return flase otherwise true.
    # Using dictionary makes this comparison check both char and number of times. 
    for i in check_S:
        if check_S[i] > check_L.get(i,0):
            return False
    return True

long = input("Enter your long string:")
short = input("Enter your short string:")

print(ransom(long, short))