def factorial(n):
    return 1 if n in (0,1) else n*factorial(n-1)
number=int(input("enter a number to find factorial:"))
print("the factorial value is",factorial(number))
print("the number:")
