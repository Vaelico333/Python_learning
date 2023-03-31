# Question: write a script that iterates through all 26 files, checks if the letter is contained in 'python', and then appends it to a list if it does.

# My answer:
import glob
letters_python = []
file_list = glob.glob('/Users/dariozoreda/Documents/GitHub/Python_learning/100_exercises/txts/*.txt')
for filepath in file_list:
    with open(filepath, 'r') as file:
        f = file.read()
        if f in 'PYTHON':
            letters_python.append(f)
print(letters_python)