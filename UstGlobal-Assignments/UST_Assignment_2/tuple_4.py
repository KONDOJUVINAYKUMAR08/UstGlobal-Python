# Given the tuple t = (1, 2, 3, 4), how can you change the value 3 to 100?

# we can change the value in a tuple by converting it to a list and again converting that list to a tuple.
#given:
t=(1, 2, 3, 4)
print("Tuple before changing value: ")
print(t)
l=list(t)
l[2]=100
t=tuple(l)
print("Tuple after changing value: ")
print(t)
