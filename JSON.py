# Working with JSON Data
import json

person = {"name": "John",
          "age": 30,
          "city": "New York",
          "hasChildren": False,
          "titles": ["engineer", "programmer"]
          }

# Converting Dictionary to JSON Data
personJSON = json.dumps(person, indent=4)
print(personJSON)

# Converting JSON Data to Dictionary
person = json.loads(personJSON)
print(person)


# Converting Class Objects to JSON Data
class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age


user = User('Max', 27)


# Function to perform Encoding from Object to Dictionary
def encode_user(o):
    if isinstance(o, User):
        return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
    else:
        raise TypeError


userJSON = json.dumps(user, default=encode_user)

'''
We can also use the in-built JSON Encoder by importing JSONEncoder from json
'''

# Accessing data from JSON file
with open("exampleData.json") as jsonData:
    obj = json.loads(jsonData.read())

    print(obj)
