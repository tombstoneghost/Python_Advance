# lambda arguments: expression
from functools import reduce
add10 = lambda x: x + 10
print(add10(5))


def add10_func(x):
    return x + 10


mult = lambda x, y: x * y
print(mult(2, 7))

# Practical Example
points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
points2D_sorted = sorted(points2D, key=lambda x: x[1])

print(points2D_sorted)

# Map Function
a = [1, 2, 3, 4, 5]
b = map(lambda x: x*2, a)
print(list(b))

# Filter Function
b = filter(lambda x: x % 2 == 0, a)
print(list(b))

# Reduce Function
product_a = reduce(lambda x, y: x * y, a)
print(product_a)
