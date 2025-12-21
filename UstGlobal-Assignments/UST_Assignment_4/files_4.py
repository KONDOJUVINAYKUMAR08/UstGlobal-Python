# Write a program to copy the contents of one text file into another file.

f1=open("UstGlobal-Assignments/UST_Assignment_4/Data3.txt","r")
content=f1.read()
f2=open("UstGlobal-Assignments/UST_Assignment_4/Data4.txt","w")
f2.write("Contents of Data3.txt are:\n")
f2.write(content)
f1.close()
f2.close()