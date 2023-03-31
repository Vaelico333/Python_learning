# Question: The code produces an error. Please understand the error and try to fix itage = input("What's your age? ")
'''age = input("What's your age? ")
age_last_year = age - 1
print("Last year you were %s." % age_last_year)
'''
# My answer:
# The error info tells us that we cannot substract an integer from a string.
# The reason being, all input is converted into a string, so the solution is 
# turning that string into an integer before the operation:

age = input("What's your age? ")
age_last_year = int(age) - 1
print("Last year you were %s." % age_last_year)