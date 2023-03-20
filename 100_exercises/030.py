'''Question: Why do you get an error and how would you fix it?

def foo(a=2, b):
    return a + b'''

# My answer:
# It returns a SyntaxError, because 
# you have to define the non-default arguments 
# before the default arguments in a function. 
# The solution would be:
def foo(b, a=2):
    return a + b