# Write a Python program that uses try, except, else, and finally blocks.

try:
    a=int(input("Enter value of a: "))
    b=int(input("Enter value of b: "))
    r=a/b
except Exception as e:
    print("Error:",e)
else:
    print("Result:",r)
finally:
    print("Program Executed!!")