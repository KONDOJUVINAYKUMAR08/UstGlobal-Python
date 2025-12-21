# Write a Python program to create a text file and write multiple lines into it.

f=open("UstGlobal-Assignments/UST_Assignment_4/Data1.txt","w")
print("Enter Student details.")
for i in range(3):
    id=int(input("Enter id number: "))
    name=input("Enter name: ")
    c_name=input("Enter course name: ")
    f.write(f"{name.title()} having roll number {id} has enrolled in {c_name} course.\n")
f.close()