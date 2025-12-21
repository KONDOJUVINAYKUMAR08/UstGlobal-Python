# Use filter() to extract all palindromic strings from a list.

def is_palindrom(st):
    return st.lower()==st[::-1].lower()

lst=["Apple", "Dad", "Orange", "Wow", "Banana", "Madam", "Refer"]
pal_lst=list(filter(is_palindrom,lst))
print("List:",lst)
print("Palindromic List:",pal_lst)