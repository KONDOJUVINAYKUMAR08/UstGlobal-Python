# How can you remove an element from a list by its index?

lst=["Apple","Banana","Bread","Milk","Orange"]
print("List berfore removing the Element: ")
print(lst)
index=int(input("Enter the index value to remove the element from that index: "))
if index>=len(lst):
    print("Index is out of range !!!")
else:
    lst.remove(lst[index])
    print("List after removing the Element at index "+ str(index) + ".")
    print(lst)