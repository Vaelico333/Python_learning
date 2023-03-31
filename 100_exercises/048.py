# Question: The script is supposed to print out letter "e" if the letter is in string "Hello", but it doesn't. Please try to fix the script.
'''for letter in "Hello":
    if letter == "e":
    print(letter)'''

# My answer:
# In this code, we are missing one indentation on the 3rd line,
# where the print function is called:
for letter in "Hello":
    if letter == "e":
        print(letter)

# This way, the print() will be inside the if statement.