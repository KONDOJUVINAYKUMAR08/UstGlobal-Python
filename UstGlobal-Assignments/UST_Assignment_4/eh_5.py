# Write a program to handle multiple exceptions in a single try block.
try:
    print("Enter numbers for division:")
    a=int(input("Enter value of a: "))
    b=int(input("Enter value of b: "))
    print(a/b)
except ZeroDivisionError as e:
    print("Error:",e)
except ValueError as e:
    print("Error:",e)
finally:
    print("Program executed")