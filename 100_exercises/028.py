# Question: Why is there an error in the code and how would you fix it?
'''def foo(a, b):
    print(a + b)
 
x = foo(2, 3) * 10'''

# My answer:
# The error is inside the function foo(): 
# it doesn't return any values, instead, it tries to print it out. 
# To fix it, I'll replace the print() with a return method, and add a print() inside x()

def foo(a, b):
    return(a + b)
 
x = print(foo(2, 3) * 10)