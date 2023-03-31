# Question: Create a script that generates a file where all letters of English alphabet are listed three in each line.

# My answer: 
import string
with open('/Users/dariozoreda/Documents/GitHub/Python_learning/100_exercises/trios.txt', 'w') as file:
    for i in zip(string.ascii_uppercase[0::3], string.ascii_uppercase[1::3], string.ascii_uppercase[2::3]+' '):
        file.write(i[0]+i[1]+i[2]+'\n')