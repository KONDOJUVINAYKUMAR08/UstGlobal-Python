# Given a list of temperatures in Celsius, use map() to convert them to Fahrenheit.

cel_List=[31, 43, 37, 41, 23, 18, 14]
fah_List=list(map(lambda x:round((x*1.8)+32,2) ,cel_List))
print("Celsius Temperatures:",cel_List)
print("Fahrenheit Temperatures:",fah_List)