# Question: Here's another similar exercise. What will the following script output? Try to do this mentally if you can.
'''c = 1
def foo():
    c = 2
    return c
c = 3
print(foo())'''

# My answer:
# The output will be 2, 
# because the variable c that foo is returning 
# is a local variable, with a value of 2, while 
# the other c (c=3) is a global variable, out of foo's scope.