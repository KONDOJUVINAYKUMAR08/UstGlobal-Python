# How do you check if an element is present in a set?
# We can check if an element is present in a set using 'element in set'
s={10, 20, 30, 40}
ele=int(input("Enter the element to check if it is in set: "))
if ele in s:
    print(ele,"exists in the set")

else:
    print("Element does not exist.")