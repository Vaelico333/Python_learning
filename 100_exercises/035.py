# Question: Create a function that takes any string as input and returns the number of words for that string.

# My answer: 
def words(a):
    length = a.split()
    return len(length)
print(words('1 2 3'))