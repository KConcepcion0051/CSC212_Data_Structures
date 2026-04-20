#recursive factorial
def factorial(number):
    if number == 1:
        return number * 1
    else:
        return number * factorial(number-1)
    
#f(n)= n * f(n-1)


def main():
    
    print(f" The factorial is {factorial(5)}")
main()