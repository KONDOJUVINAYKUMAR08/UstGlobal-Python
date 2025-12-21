# Given a list of integers, use filter() to remove all negative numbers.

lst=[10, 22, -33, 4, 55, -18, 98, -1]
pos_lst=list(filter(lambda x:x>=0 ,lst))
print("List:",lst)
print("Positive List:",pos_lst)