# Use map() to add 10 to each element of a given list of numbers.

lst=[10, 20, 30, 40, 50]
new_lst=map(lambda x:x+10 ,lst)
print("List:",lst)
print("Updated List:",list(new_lst))