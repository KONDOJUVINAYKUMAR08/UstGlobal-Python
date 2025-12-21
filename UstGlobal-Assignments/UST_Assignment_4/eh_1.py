# Write a Python program to handle a ZeroDivisionError.

try:
    a=int(input("Enter value of a: "))
    b=int(input("Enter value of b: "))
    print(a/b)
except ZeroDivisionError as e:
    print("Error:",e)