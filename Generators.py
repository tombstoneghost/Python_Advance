# Working with Generators in Python
# A Basic Generator
def my_generator():
    yield 1
    yield 2
    yield 3


g = my_generator()
for i in g:
    print(i)

# value = next(g)
# print(value)

print(sum(g))
print(sorted(g))


# A generator which will perform a countdown from the given number
def countdown(num):
    print('Starting')
    while num > 0:
        yield num
        num -= 1


cd = countdown(4)

for i in cd:
    print(i)


# A generator which will return a sequence of numbers starting from 0 to n
def first_n(n):
    num = 0

    while num < n:
        yield num
        num += 1


my_list = list(first_n(10))
print(my_list)


# Fibonacci Generator
def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b


fib = fibonacci(30)
print(list(fib))

# Generator Expression
new_generator = (i for i in range(10) if i % 2 == 0)
print(list(new_generator))
