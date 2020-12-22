# Dictionary: Key-Value pairs, Unordered, Mutable
my_dict = {
    "name": "Max",
    "age": 28,
    "city": "New York"
}

print(my_dict)

'''
my_dict2 = dict(name="Mary", age=27, city="Boston")
'''

# Printing Values for a Key
print(my_dict["name"])

# Add a Key-Value Pair
my_dict["email"] = "max@xyz.com"
print(my_dict)

# Removing a Pair
del my_dict["email"]
print(my_dict)

my_dict.pop("name")

'''
When we use popitem(), it will remove the last inserted item.
'''

# Check for key inside a dictionary
if "name" in my_dict:
    print(my_dict["name"])
else:
    print("No")

'''
We can also use a try-except method as well
'''

# Printing all the Keys
for key in my_dict.keys():
    print(key)

# Printing all the values
for value in my_dict.values():
    print(value)

# Printing both together
for key, value in my_dict.items():
    print(key, value)

# Copying a Dictionary
my_dict_copy = my_dict.copy()

# Mering two dictionaries
a = {"name": "Max", "age": 28, "email": "max@xyz.com"}
b = dict(name="Mary", age=27, city="Boston")

a.update(b)
print(a)

'''
You can use any immutable types as a key
'''

# Using a tuple as a Key
my_tuple = (8, 7)
tuple_dict = {my_tuple: 15}

print(tuple_dict)
