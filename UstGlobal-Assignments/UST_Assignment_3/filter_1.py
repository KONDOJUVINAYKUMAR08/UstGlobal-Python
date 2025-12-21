# Write a Python program using filter() to extract all even numbers from a list.

lst=[11, 22, 33, 44, 55]
even_lst=list(filter(lambda x:x%2==0 ,lst))
print("List:",lst)
print("Even List:",even_lst)