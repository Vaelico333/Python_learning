# Question: Create a function that takes a text file as input and returns the number of words contained in the text file. Please take into consideration that some words can be separated by a comma with no space. For example "Hi,it's me." would need to be counted as three words. 
# My answer:
def word_count(filename):
    with open(filename, 'r') as file:
        data = file.read()
    return len(data.replace(',',' ').split())
print(word_count('/Users/dariozoreda/Documents/GitHub/Python_learning/100_exercises/words2.txt'))