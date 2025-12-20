# How can you use list comprehension to generate a list of the first 10 Fibonacci numbers?

lst=[0,1]
[lst.append(lst[-1]+lst[-2]) for i in range(5)]
print("Fibonacci numbers using list comprehension: ",lst)