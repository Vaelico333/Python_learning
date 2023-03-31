# Question: Please create a script that generates 26 text files named a.txt,b.txt, and so on up to z.txt. Each file should contain a letter reflecting its filename. So, a.txt will contain letter a, b.txt will contain letter b and so on.

# My answer:
import string
for i in string.ascii_uppercase:
    with open('/Users/dariozoreda/Documents/GitHub/Python_learning/100_exercises/txts/'+i+'.txt', 'w') as f:
        f.write(i)
