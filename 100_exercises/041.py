# Question: Create a script that generates a text file with all letters of English alphabet inside it, one letter per line.

# My answer:
import string
a = list(string.ascii_uppercase)
with open ('/Users/dariozoreda/Documents/GitHub/Python_learning/100_exercises/abecedario.txt', 'w') as file:
    for i in a:
        file.write(i+'\n')