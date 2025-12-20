# Write a Python program that uses reduce() to find the greatest common divisor (GCD) of a list of numbers.
from functools import reduce

def gcd(m, n):
    while n != 0:
        m, n = n, m % n
    return m
lst=[46, 32, 98, 100, 76, 24]
gcd_result=reduce(gcd, lst)
print("The GCD of list of Numbers:",gcd_result)