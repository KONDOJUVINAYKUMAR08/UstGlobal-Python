# What is the difference between a list and a tuple in Python?

#Ans:
""" The main difference between a list and tuple is:
    Lists are Mutable while Tuples are Immutable. i.e., 
    Lists can be modified but tuples cannot be modified once created
    Syntax for List is 'lst=[1, 2, 3, 4, 5]'
    Synatx for Tuple is 'tup=(1, 2, 3, 4, 5)'
    """
#example:
#list
lst = ["Apple","Banana","Bread","Milk"]
lst[1:3] = [10, 20]
print(lst)
#tuple
tup=("Apple","Banana","Bread","Milk")
print(tup)
try:
    tup[1]="Orange"
    print(tup)
except:
    print("Tuples cannot be Modified!!!")

#output:
# ['Apple', 10, 20, 'Milk']
# ('Apple', 'Banana', 'Bread', 'Milk')
# Tuples cannot be Modified!!!