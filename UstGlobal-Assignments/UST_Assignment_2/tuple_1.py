# Can you modify the elements of a tuple after it has been created? Why or why not?

#Ans:
'''No.. We cannot modify the elements of a tuple after it has been created.
    This is because tuples are immutable and they cannot be changed once created...

    The below example shows why tuple are not modified..'''

tup=("Apple","Banana","Bread","Milk")
print(tup)
try:
    tup[1]="Orange"
    print(tup)
except:
    print("Tuples cannot be Modified!!!")
finally:
    print(tup)
