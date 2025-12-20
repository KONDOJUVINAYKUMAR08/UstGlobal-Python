# Write a Python function that takes a tuple of numbers and returns the sum of all its elements.

def sum_of_ele(t):
    sum=0
    for ele in t:
        sum+=ele

    return sum

t=(12, 56, 98, 34)
print("Sum of elements in tuple: ", sum_of_ele(t))