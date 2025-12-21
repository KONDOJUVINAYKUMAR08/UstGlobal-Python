# Write a program using map() to convert all strings in a list to uppercase.

lst=["Apple","Banana","Bread","Milk","Orange"]
new_lst=map(lambda item:item.upper(), lst)
print("List:",lst)
print("Updated List:",list(new_lst))