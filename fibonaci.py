# CSC 212 Kevin Concepcion 11/21/25
# This program defines a recursive function to calculate the Fibonacci number for a given input.
def fib(number):
    if number == 0 or number == 1 :
        return 1
    else:
        return fib(number -1) + fib(number-2)
    
def main():
    print(fib(6))
main()