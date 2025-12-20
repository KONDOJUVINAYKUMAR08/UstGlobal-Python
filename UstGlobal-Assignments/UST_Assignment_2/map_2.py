# How would you use the map() function to convert all string elements of a list to uppercase?

lst=["Apple","Banana","Bread","Milk","Orange"]
new_lst=map(lambda item:item.upper(), lst)
print(lst)
print("Updated List:",list(new_lst))