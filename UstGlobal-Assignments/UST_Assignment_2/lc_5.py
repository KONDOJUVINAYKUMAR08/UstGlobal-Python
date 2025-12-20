# Can you use an if condition inside a list comprehension? 
# Provide an example where only odd numbers are selected from a list.
"""
ANS:
    Yes we can, using if condition inside a list comprehension
"""
#example

lst=[1,2,3,4,5,6,7]
odd_lst=[i for i in lst if i%2==1]
print(odd_lst)