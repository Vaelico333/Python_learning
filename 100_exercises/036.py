# Question: Please download the words1.txt file from the attachment and then create a Python function that takes a text file as input and returns the number of words contained in the text file.

# My answer:
words = open("/Users/dariozoreda/Documents/GitHub/Python_learning/100_exercises/words1.txt", "r")
def word_count(a):
    words_data = a.read()
    return len(words_data.split())
print(word_count(words))

