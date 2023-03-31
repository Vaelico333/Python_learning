# Question: Create a script that generates a file where all letters of English alphabet are listed two in each line.

# My answer:
import string
with open('/Users/dariozoreda/Documents/GitHub/Python_learning/100_exercises/pairs.txt', 'w') as file:
    for i in zip(string.ascii_uppercase[0::2], string.ascii_uppercase[1::2]):
        file.write(i[0]+i[1]+'\n')