# Lists: ordered, mutable, allows duplicate elements
my_list = ["banana", "cherry", "apple"]
print(my_list)

'''
my_list2 = [5, True, "apple", "apple"]
print(my_list2)
'''

# Accessing List Item
item = my_list[1]
print(item)
item = my_list[-1]
print(item)

# Iterating over a list
for i in my_list:
    print(i)

# Check for items in the list
if "banana" in my_list:
    print("Yes")
else:
    print("No")

# Length of List
print("Length:", len(my_list))

# Appending an item
my_list.append("lemon")
print(my_list)

my_list.insert(1, "blueberry")
print(my_list)

# Remove Items
item = my_list.pop()
print("Item Removed:", item)
print(my_list)

item = my_list.remove("cherry")

# Remove all elements
# my_list.clear()

# Reverse List
my_list.reverse()
print(my_list)

# Sorting List
my_list.sort()
print(my_list)

# Creating a list with 5 Zeros
new_list = [0] * 5
print(new_list)

# Concatenating List
new_list = new_list + [1] * 5
print(new_list)

# Slicing the List
my_list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

a = my_list2[1:5]
print(a)

a = my_list2[1::2]
print(a)

# Copying a list
list_original = ["banana", "cherry", "apple"]

list_copy = list_original.copy()  # Can Also be done by doing list(list_original)

print(list_copy)

# List Comprehension
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = [i*i for i in a]

print(b)
