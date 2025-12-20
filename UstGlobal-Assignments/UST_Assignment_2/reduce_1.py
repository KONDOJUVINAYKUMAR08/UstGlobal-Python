# What is the output of the following code?

# from functools import reduce
# result = reduce(lambda x, y: x * y, [1, 2, 3, 4])
# print(result)

""" ANS:
    the output of above code will be 24.
    reduce() repeatedly applies the function to items in iterable, reducing it to single value
    1*2=2
    2*3=6
    6*4=24
    so, the output is: 24."""

from functools import reduce
result = reduce(lambda x, y: x * y, [1, 2, 3, 4])
print(result)