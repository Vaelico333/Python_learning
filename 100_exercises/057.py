# Question: Please download the file in the attachment and use Python to print out its content. The file's name is company1.json

# My answer:
import json
from pprint import pprint
with open('company1.json', 'r') as file:
    pprint(json.load(file))