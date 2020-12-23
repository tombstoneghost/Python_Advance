# itertools: product, permutations, combinations, accumulate, groupby and infinite iterators
from itertools import product, permutations, combinations, combinations_with_replacement, accumulate, groupby, count, \
    cycle, repeat
import operator

'''
Product: To perform a product of two lists
'''
a = [1, 2]
b = [3, 4]
prod = product(a, b)
print(list(prod))

'''
Permutations: Returns all Possible orderings of an input
'''
a = [1, 2, 3]
perm = permutations(a, 2)  # Permutations with Length 2
print(list(perm))

'''
Combinations: Return all possible combinations with the specified length
'''
a = [1, 2, 3, 4]
comb = combinations(a, 2)
print(list(comb))

comb_wr = combinations_with_replacement(a, 2)
print(list(comb_wr))

'''
Accumulate: This functions returns a iterator that returns accumulated sums for the input
'''
a = [1, 2, 3, 4]
acc = accumulate(a)
print(a)
print(list(acc))

# Combining it with a Operator
acc = accumulate(a, func=operator.mul)
print(list(acc))

'''
GroupBy: This functions returns a iterator which returns groups and keys from a iterable input.
'''


def smaller_than_3(x):
    return x < 3


a = [1, 2, 3, 4]
group_obj = groupby(a, key=smaller_than_3)

for key, value in group_obj:
    print(key, list(value))

'''
Infinite Iterators: 
    count: Infinite loop which will start from the given value, 
    cycle: Infinite loop which will cycle through the given iterable, and 
    repeat: Infinite loop which will repeat the iterator the given number of items
'''
for i in count(10):
    print(i)
    if i == 15:
        break

a = [1, 2, 3]
for i in cycle(a):
    print(i)
    if i == 3:
        break  # Did this so that next example can run :P

for i in repeat(1, 4):
    print(i)
