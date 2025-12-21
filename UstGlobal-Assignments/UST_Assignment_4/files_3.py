# Write a Python program to count the number of lines, words, and characters in a text file.

f=open("UstGlobal-Assignments/UST_Assignment_4/Data3.txt","r")
content=f.readlines()

l_count=len(content)
w_count=0
c_count=0

for line in content:
    w_count+=len(line.split())
    c_count+=sum([len(j) for j in line.split(" ")])
    # c_count+=len(line)

print("Number of lines in file:",l_count)
print("Number of words in file:",w_count)
print("Number of characters in file:",c_count)
f.close()