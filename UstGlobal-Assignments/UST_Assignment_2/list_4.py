# How can you check if an element exists in a list in Python?
#Checking if an element exists in list
lst=["Apple","Banana","Bread","Milk","Orange"]
ele=input("Enter the element to check if it is in list: ").title()
if ele in lst:
    print("Element exists at index: ",lst.index(ele))

else:
    print("Element does not exist.")
