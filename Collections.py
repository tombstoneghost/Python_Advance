# Collections: Counter, namedtuple, OrderedDict, DefaultDict, deque
from collections import Counter, namedtuple, OrderedDict, defaultdict, deque

'''
Counter: Counts the number of occurrence of a character and converts it into a dictionary
'''
a = "aaaaaabbbbcccc"
my_counter = Counter(a)
print(my_counter)

# Printing Keys or Values
print(my_counter.keys())
print(my_counter.values())

# Printing Most Common Element
print(my_counter.most_common())

# Converting it in a list
my_list = list(my_counter.elements())
print(my_list)

'''
namedtuple: Creates a class with the given name and variables and then we can access them the same way
'''
Point = namedtuple('Point', 'x, y')
pt = Point(1, -4)
print(pt)

# Printing values for x or y
print(pt.x)
print(pt.y)

'''
OrderedDict: This Dictionary type remembers the order we have inserted the pairs
'''
ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
print(ordered_dict)

'''
DefaultDict: Similar to a normal dictionary but it has a default value
'''
d = defaultdict(int)
d['a'] = 1
d['b'] = 2
print(d)
print(d['c'])

'''
Deque: Double Ended Queue in which you can add and remove elements from both the ends.
'''
d = deque()
d.append(1)
d.append(2)

print(d)

# Adding Elements to Left
d.appendleft(3)
print(d)

# Removing Elements
d.pop()
d.popleft()

# To remove all elements we can use the clear()

# Extending the Queue
d.extend([4, 5, 6])
print(d)

d.extendleft([1, 2, 3])
print(d)

# Rotate the Deque
d.rotate(1)
print(d)

d.rotate(-1)
print(d)
