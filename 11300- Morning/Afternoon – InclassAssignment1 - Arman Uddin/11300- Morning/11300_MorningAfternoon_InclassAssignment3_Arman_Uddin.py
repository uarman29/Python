# Arman Uddin
# Section 2N Tuesday 12:30pm - 1:45 pm

def collatzMain():
    try:
        n = int(input("Please enter a positive integer to get collatz sequence:"))
        if(n<1):
            print("Invalid Input")
            return
        collatz(n)
    except:
        print("Invalid Input")

def collatz(n):
    if(n == 1):
        print(1)
        return
    print(n)
    if(n%2 == 0):
        collatz(n//2)
    else:
        collatz(3*n+1)


def divide():
    try:
        print("This program will divide the first input by the second input")
        a = int(input("Enter a number:"))
        b = int(input("Enter a number:"))
        print(a/b)
    except ZeroDivisionError:
        print("Cannot divide by zero")
    except ValueError:
        print("Invalid Input")

def primeFactors():
    try:
        n = int(input("Please enter a positive integer to get all the prime factors:"))
        if (n < 1):
            print("Invalid Input")
            return
        for i in range(n,0,-1):
            if(n%i == 0 and isPrime(i)==1):
                print(i)
    except:
        print("Invalid Input")


def primeNumber():
    try:
        n = int(input("Please enter a positive integer to list all prime numbers less than or equal to the number:"))
        if (n < 1):
            print("Invalid Input")
            return
        for i in range(n,1,-1):
            if(isPrime(i)==1):
                print(i)
    except:
        print("Invalid Input")

def isPrime(n):
    for i in range(n-1, 1, -1):
        if(n%i == 0):
            return 0
    return 1

collatzMain() # Input:11 Result: 11,34,17,52,26,13,40,20,10,5,16,8,4,2,1
divide() # Input: 5,0 Result: Cannot Divide by zero ; Input: "a","b" Result: Please enter valid inputs
primeFactors() # Input:20 Result: 5 2 1
primeNumber() # Input: 20 Result: 19 17 13 11 7 5 3 2