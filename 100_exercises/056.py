# Question: Store the dictionary in a json file.

d = {"employees":[{"firstName": "John", "lastName": "Doe"},
                {"firstName": "Anna", "lastName": "Smith"},
                {"firstName": "Peter", "lastName": "Jones"}],
"owners":[{"firstName": "Jack", "lastName": "Petter"},
          {"firstName": "Jessy", "lastName": "Petter"}]}

# My answer:
import json
with open('company1.json', 'w') as file:
    json.dump(d, file, indent=4, sort_keys=True)