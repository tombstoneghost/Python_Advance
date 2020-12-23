# Working with Decorators in Python
import functools

# Function Decorator
"""
@myDecorator
def doSomething():
    pass
"""


def start_end_decorator(func):
    def wrapper():
        print('Start')
        func()
        print('End')
    return wrapper()


def argument_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('Start')
        res = func(*args, **kwargs)
        print('End')
        return res

    return wrapper


@start_end_decorator
def print_name():
    print('Alex')


print_name


# Function has some arguments
@argument_decorator
def add5(x):
    return x + 5


result = add5(10)
print(result)

# Print Help of a Decorator
print(help(add5))


# Class Decorator
class CountCalls:

    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f'This is executed {self.num_calls} times')
        return self.func(*args, **kwargs)


@CountCalls
def say_hello():
    print('Hello')


say_hello()
say_hello()
say_hello()
