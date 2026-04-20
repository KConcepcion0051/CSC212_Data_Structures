# CSC 212 Kevin Concepcion

# Write a recursive function to perform the following:
# count_down(n)
# Given a value n, the function prints the value n and count down printing (n-1),…till it
# prints 0.

# Implement a main function to demonstrate that the functions work as expected.\\
    
def count_down(n):
    if n == 0:
        print(f"N reached 0, n value:{n}")
    else:
        print(f"Current n value: {n}, next will be {n-1}")
        count_down(n-1)

def main():
    
    count_down(5)
    
main()