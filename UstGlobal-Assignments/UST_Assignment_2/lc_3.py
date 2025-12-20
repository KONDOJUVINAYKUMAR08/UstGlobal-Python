# Write a list comprehension to extract all words that are longer than 4 characters from a sentence.

st="Naruto is the 7th Hokage and Kakashi is the 6th Hokage."
lst=st.split(" ")
new_lst=[i for i in lst if len(i)>4]
print(lst)
print(new_lst)