# Question: explain why this returns a KeyError, and how can we access 'Smith'
"""d = {"Name": "John", "Surname": "Smith"}
print(d["Smith"])"""
# My answer:
# It returns KeyError because there is no key with that name, as Smith is a value, not a key.
d = {"Name": "John", "Surname": "Smith"}
f = list(d.values())
print(f[f.index("Smith")])
# I could have used its key to access Smith, but in this case I've written the way to find it if we ignore the key