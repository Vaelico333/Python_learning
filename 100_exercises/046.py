# Question: write a script that extracts the letters from the 26 files we created and puts them in a list

# My answer:
import string
letters = []
for i in string.ascii_uppercase:
    with open('/Users/dariozoreda/Documents/GitHub/Python_learning/100_exercises/txts/'+i+'.txt', 'r') as f:
        letters.append(f.read())
print(letters)

# A better answer (I didn't know the module glob)
import glob
letters_1 = []
file_list = glob.glob('/Users/dariozoreda/Documents/GitHub/Python_learning/100_exercises/txts/*.txt')
for file_name in file_list:
    with open(file_name, 'r') as file:
        letters_1.append(file.read())
print(letters_1)