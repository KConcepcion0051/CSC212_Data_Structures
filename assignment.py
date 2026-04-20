#CSC 212 Kevin Concepcion

# Write a recursive function that takes a string as an input and returns
# the reverse of the string


def reverse_s(word):
   #if the string has one character just return back the character
   if len(word)<=1:
      return word
   else:
      # 'word[-1]' returns the last character then 'reverse_s(word[:-1])' calls the function again removing the last char of word
      return word[-1] + reverse_s(word[:-1])
   
   
# Write a recursive function rec_string that produces the output shown
# below for the corresponding function calls. Write a main function to
# test the function. 


def rec_string(word):
   if word =="":
      print("*")
      return
   else:
      #recursive that removes the first char of word until it becomes emtpy with will cause the * to print
      rec_string(word[1:])
      print(word)



def main():
   print(reverse_s('hello'))
   #print()
   rec_string('abcde')
   rec_string('abc')
   
main()