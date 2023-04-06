# Question: Please open company1.json and use Python to add a new employee to the content of the file after Peter called Albert Bert

# My answer:
import json
{'firstName':'Albert', 'lastName':'Bert'}
with open('company1.json', 'r+') as file:
    d = json.load(file)
    d['employees'].append({'firstName':'Albert', 'lastName':'Bert'})
    file.seek(0)
    json.dump(d, file, indent=4)
    