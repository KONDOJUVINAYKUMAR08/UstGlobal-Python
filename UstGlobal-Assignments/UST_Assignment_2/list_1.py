#How do you add an element at the end of a list in Python?
#Adding element at the end of the list

lst=["Apple","Banana"]
print("Elements in list before appending: ")
print(lst)
ele=input("Enter the element to add in list at the end: ") 
lst.append(ele)
print("Elements in list after appending: ")
print(lst)