# Working with asterisk(*) operator

# Multiplication Operation
result = 2 * 5
print(result)

# Power Operation
result = 2 ** 5
print(result)

# List with Repeated Elements
result = [0] * 10
print(result)

result = [0, 1] * 10
print(result)

# Tuple with Repeated Elements
result = (0, ) * 10
print(result)

# String with Repeated Elements
result = "AB" * 10


# Using with *args and **kwargs
def foo(a, b, *args, **kwargs):
    print(a, b)

    for arg in args:
        print(arg)

    for key in kwargs:
        print(key, kwargs[key])


foo(1, 2, 3, 4, 5, six=6, seven=7)


# Using as a parameter
def foo(a, b, *, c):
    print(a, b, c)


foo(1, 2, c=3)


# Argument Unpacking
my_list = [0, 1]
foo(*my_list, c=0)

numbers = (1, 2, 3, 4, 5, 6)

beginning, *middle, last = numbers

print(beginning)
print(middle)
print(last)
