# Question: create a dictionary with keys a, b and c, where each key has as value a list from 1 to 10, 11 to 20 and 21 to 30 respectively
 # My answer:

from pprint import pprint
pprint({'a':list(range(1,11)), 'b':list(range(11,21)), 'c':list(range(21,31))})