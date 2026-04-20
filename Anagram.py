# Kevin Concepcion CSC 212-01 Anagram exercise

# This program will determine if two strings are anagrams of each other. The function anagramSolution1 takes two strings as input and checks if they are anagrams by comparing the characters and their counts in both strings. 
# If the strings have different lengths, they cannot be anagrams. The function uses a list to keep track of the characters in the second string and checks if each character in the first string can be found in that list. 
# If a character is found, it is removed from the list to ensure that each character is only used once. If all characters in the first string are found in the second string, the function returns True, indicating that the 
# strings are anagrams; otherwise, it returns False.

def anagramSolution1(s1,s2):
    stillOK = True              # 1 
    if len(s1) != len(s2):      # 4
        stillOK = False

    alist = list(s2)            #2
    pos1 = 0                    #1

    while pos1 < len(s1) and stillOK:   # worst case, the len is N(unknown). since its a loop itll be n*(inside operators )
        pos2 = 0
        found = False
        while pos2 < len(alist) and not found:
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 = pos2 + 1

        if found:
            alist[pos2] = None
        else:
            stillOK = False

        pos1 = pos1 + 1

    return stillOK

s1= input("Enter string #1")
s2= input("Enter string #2")

print(anagramSolution1(s1,s2))