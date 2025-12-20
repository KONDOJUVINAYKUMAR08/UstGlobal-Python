# How does a set handle duplicate values when adding them?

""" ANS:
    In Python set only stores unique elements.
    If we try to add an element that already exsits in set, nothing changes and 
    no error is raised..."""

s=set()
s.add(22)
s.add(24)
s.add(24)
s.add(25)
s.add(28)
s.add(28)
s.add(22)
print(s)