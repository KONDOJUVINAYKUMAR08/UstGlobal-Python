# Write a program using map() to calculate the length of each word in a list of strings.

lst=["Apple","Banana","Bread","Milk","Orange"]
len_lst=map(lambda item:len(item), lst)
print("List:",lst)
print("Length List:",list(len_lst))