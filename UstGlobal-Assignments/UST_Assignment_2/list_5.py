# Write a Python function that removes duplicates from a list without using the set() function.
def remove_dup(lst):
    new_list=[]
    for item in lst:
        if item in new_list:
            continue
        else:
            new_list.append(item)
    return new_list

lst=[10, 20, 30, 30, 45, 50, 55, 60, 55]
print("List before removing duplicates: ")
print(lst)
new_lst=remove_dup(lst)
print("List after removing duplicates: ")
print(new_lst)
