# Write a program using filter() to select all words from a list that start with a vowel.
def check_vowel(l):
    return l[0].lower() in 'aeiou'

lst=["Apple","Banana","Egg","Milk","Orange","Ice-cream","Unibic"]

vowel_list=list(filter(check_vowel,lst))
print("List:",lst)
print("Vowel Words List:", vowel_list)
