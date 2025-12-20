# Write a Python function that takes a dictionary and returns a list of keys that have values greater than 50.

def dict_f(d):
    lst=[]
    for k,v in d.items():
        if v>50:
            lst.append(k)
    return lst

dict={"Apple" : 150,
      "Banana" : 30,
      "Orange" : 45,
      "Bread" : 56,
      }
print(dict)
print("Values greater than 50 are:",dict_f(dict))