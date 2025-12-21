# Write a program to read the contents of a text file line by line.

f=open("UstGlobal-Assignments/UST_Assignment_4/Data2.txt","r")
print("Contents in file:")
for line in f.readlines():
    print(line)
f.close()