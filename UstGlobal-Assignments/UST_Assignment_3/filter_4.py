# Write a program using filter() to find numbers greater than 50 from a list.

lst=[10, 22, 39, 74, 55, 18, 98, 81]
new_lst=list(filter(lambda x:x>50 ,lst))
print("List:",lst)
print("List of elements greater than 50:",new_lst)
