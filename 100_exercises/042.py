# Question: Print out in each line the sum of homologous items of the two sequences.
a = [1, 2, 3]
b = (4, 5, 6)

# My answer:
for i in zip(a, b):
    print(sum(i))
