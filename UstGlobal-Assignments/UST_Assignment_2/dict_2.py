# What happens if you try to access a key that does not exist in a dictionary?

""" ANS:
    When we try to access a key that does not exist in a dictionary
    we get KeyError
     If we try below code:
      we get:
       Traceback (most recent call last):
        print(dict["Grapes"])
            ~~~~^^^^^^^^^^
        KeyError: 'Grapes' """

dict={"Milk": 6}
dict["Apple"]=3
dict["Banana"]=5
dict["Orange"]=10
print(dict["Grapes"])