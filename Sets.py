# Sets: Unordered, Mutable, No Duplicates

my_set = {1, 2, 3, 4, 4}
print(my_set)

'''
my_set = set(1, 2, 3, 4, 5, 6, 6)
'''

# Adding Elements
my_set.add(1)
my_set.add(5)
my_set.add(6)

# Removing an Element
my_set.remove(4)
print(my_set)

my_set.discard(15)
print(my_set)

'''
To clear complete set: my_set.clear()
To remove a arbitrary value: my_set.pop()
'''

# Iterate over the set
for x in my_set:
    print(x)

# Check for element in the set
if 2 in my_set:
    print("Yes")
else:
    print("No")

# Unions and Intersections
odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

union = odds.union(evens)
print(union)

intersection = odds.intersection(evens)
print(intersection)

intersection = odds.intersection(primes)
print(intersection)

intersection = evens.intersection(primes)
print(intersection)

# Difference of two Sets
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}

difference = setA.difference(setB)
print(difference)

symmetric_difference = setB.symmetric_difference(setA)
print(symmetric_difference)

# Modify our Set
setA.update(setB)
print(setA)

'''
There are update methods for intersection, difference and symmetric_difference

Similarly, there are in-built functions to check for issubset(), issuperset(), disjoint()
'''

# Copying two sets
set_copy = setA.copy()
print(set_copy)

'''
You can also create a frozenset(), which is an immutable version of a normal set.


a = frozenset([1, 2, 3, 4])
'''
