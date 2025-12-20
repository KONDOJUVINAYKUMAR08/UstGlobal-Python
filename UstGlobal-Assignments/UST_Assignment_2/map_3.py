# Compare and contrast the map() and filter() functions in Python.

""" ANS:
    map() applies the function to each element in iterable and transforms each element
    filter() applies a function that returns True or False."""

#Example:
#map():
lst=[10, 20, 30, 40, 50]
squared_lst=map(lambda x:x**2 ,lst)
print(lst)
print("Squared List:",list(squared_lst))

#filter():
lst=[11, 22, 33, 44, 55]
even_lst=filter(lambda x:x%2==0 ,lst)
print(lst)
print("Even List:",list(even_lst))