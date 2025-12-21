# Write a program to open a file and handle a FileNotFoundError.
try:
    f=open("data.txt","r")
    print(f.readlines())
except FileNotFoundError as e:
    print("Error:",e)
