# Question: replace "break" with something else so Hello is printed repeatedly but Hi is never printed.
'''while True:
    print('Hello')
    if 2>1:
        break
    print('Hi')
'''
# My answer:
while True:
    print('Hello')
    if 2>1:
        continue
    print('Hi')
