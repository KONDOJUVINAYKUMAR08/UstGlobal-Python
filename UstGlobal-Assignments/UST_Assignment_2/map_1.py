# How does the map() function work in Python? Give an example where you square each number in a list.

""" ANS:
    map() is a built in function that applies a function to every item in a iterable and 
    return map object"""

#example:
lst=[10, 20, 30, 40, 50]
squared_lst=map(lambda x:x**2 ,lst)
print(lst)
print("Squared List:",list(squared_lst))