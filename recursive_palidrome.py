
def palindrome(word):
    #base case if false
    
    if word[0] != word[-1]:
        return False
    
    #base case if true
    elif len(word) <= 1:
        return True
    
    else:
        return palindrome(word[1:-1])

def main():
    print(palindrome("civic"))
    print(palindrome("civvic"))
    print(palindrome("civic"))
main()