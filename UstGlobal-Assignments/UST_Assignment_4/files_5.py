# Write a Python program to search for a 
# specific word in a text file and display the line numbers where it appears.
word= input("Enter the word to search: ")
f= open("UstGlobal-Assignments/UST_Assignment_4/Data5.txt", "r")
content=f.readlines()
current_line = 1
word_found = False
for line in content:
    if word.lower() in line.lower():
        print(f"Word found at line {current_line}")
        word_found = True
    current_line += 1
f.close()
if not word_found:
    print("Word not found in the file.")
