# Write a Python program using map() to convert a list of integers into their squares.

lst=[10, 20, 30, 40, 50]
squared_lst=map(lambda x:x**2 ,lst)
print("List:",lst)
print("Squared List:",list(squared_lst))