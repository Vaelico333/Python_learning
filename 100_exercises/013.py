# Question: Complete the script so it generates the expected output using my_range  as input data. Please note that the items of the expected list output are all strings.
my_range = range(1, 21)
# My answer:
print([str(i) for i in my_range])

# Their answer: 
print(list(map(str, my_range)))
