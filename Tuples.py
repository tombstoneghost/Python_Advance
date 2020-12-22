# Tuples: ordered, immutable, allows duplicate elements
my_tuple = ("Max", 28, "Boston")  # You are also write a tuple without parentheses
print(my_tuple)

'''
my_tuple = tuple("Max", 28, "Boston")
'''

# Accessing an item
item = my_tuple[0]
print(item)

# We cannot change an element inside a element since its immutable

# Iterate a Tuple
for x in my_tuple:
    print(x)

# Check if element is present inside a tuple
if "Max" in my_tuple:
    print("Yes")
else:
    print("No")

# Length of Tuple
print(len(my_tuple))
print(my_tuple.count("Max"))

# To get index of an element
print(my_tuple.index("Max"))

# Tuple to List
my_list = list(my_tuple)
print(my_list)

# Slicing a Tuple
a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
b = a[2:8:2]
print(b)

# Unpacking
new_tuple = "Max", 28, "Boston"

name, age, city = new_tuple

print(name)
print(age)
print(city)

i1, *i2, i3 = a
print(i1)
print(i2)
print(i3)

'''
Tuples requires less memory to store and is time efficient as well than a list
'''
