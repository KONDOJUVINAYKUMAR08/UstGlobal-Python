# Write a program that accepts user input and handles a ValueError if the input is not an integer.

try:
    a=int(input("Enter value of a: "))
    b=int(input("Enter value of b: "))
    print(a+b)
except ValueError as e:
    print("Error:",e)
