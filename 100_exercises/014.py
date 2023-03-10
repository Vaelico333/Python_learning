# Question: Complete the script so that it removes duplicate items from list a .
a = ["1", 1, "1", 2]
# My answer:
print(list(set(a)))

# Their answer:
from collections import OrderedDict
a = ["1", 1, "1", 2]
a = list(OrderedDict.fromkeys(a))
print(a)
# So I'll take just one point out of two