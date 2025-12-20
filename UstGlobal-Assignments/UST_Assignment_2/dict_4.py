# How would you iterate over both keys and values of a dictionary in Python?

dict={"Apple" : 150,
      "Banana" : 30,
      "Orange" : 45,
      "Bread" : 56,
      }
for k,v in dict.items():
    print("Key: "+k+" , Value: "+str(v))