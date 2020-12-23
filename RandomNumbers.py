# Working with random numbers
import random
import secrets
import numpy as np

# Getting a Random Number
a = random.random()
print(a)

# Specifying a Range
a = random.uniform(1, 10)
print(a)

# Getting a Random Integer
a = random.randint(1, 10)  # This includes the upperbound where randrange() does not include the upperbound
print(a)

# Working with List
my_list = list('ABCDEFGH')
a = random.choice(my_list)  # Used to pick a random choice from the list
print(a)

a = random.sample(my_list, 3)  # Will pick 3 random elements
print(a)

random.shuffle(my_list)  # Randomly Shuffle the list
print(my_list)

# To initialize a random number generator
random.seed(10)
print(random.random())
print(random.randint(1, 100))

# To work with passwords we need to use the secrets module

a = secrets.randbelow(10)  # This will produce a random integer between 0 and upperbound (upperbound not included)
print(a)

a = secrets.randbits(4)  # This will return a random number with k random bits
print(a)

a = secrets.choice(my_list)  # This will return a random choice which is not reproducible
print(a)

# Working with Arrays
a = np.random.rand(3)  # Returns an Array with 3 random elements
print(a)

a = np.random.randint(0, 10, (3, 4))  # A 3 X 4 Array with random integers in range (3, 4)
print(a)

'''
You can also shuffle the array using np.random.shuffle(arr).

The Numpy's Random Number generator is not similar to the one in random module
'''
