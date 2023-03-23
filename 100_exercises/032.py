# Question: What will the following script output? Please try to do this mentally if you can.
'''c = 1
def foo():
    return c
c = 3
print(foo())'''

# My answer:
# The output is 3, because we define foo's value as the value of c, 
# and then we change c's value to 3. 
# Python reads the code from top to bottom.