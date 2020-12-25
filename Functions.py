"""
- Difference between arguments and parameters
    Parameters are the variables that are defined or used inside parentheses who are defining a function
    Arguments are the values passed for these parameters while calling a function

- Positional and Keyword Arguments

- Default Arguments
    Passing a value in the function parameters and it will be the default value even if you don't pass any

- Variable Length Arguments
    Such arguments are passed when you don't know the exact number of arguments to be passed. You can add a '*' prefix
    to the parameter name.

- Difference between '*args' and '**kwargs'
    *args -> You can pass any number of positional arguments to the function
    **kwargs -> You can pass any number of keyword arguments to the function

- Forced Keyword Arguments

- Unpacking Arguments

- Local and Global Variables
    Local Variables are those which has a limited scope within its given block
    Global Variables are those can be used anywhere in the program, all you need is to use the keyword 'global' when
    using the global variable inside some function or block
"""


# Arguments and parameters
def print_name(name):
    print(name)


print_name('Alex')


# Positional and Keyword Arguments
def foo(a, b, c=4):  # c has a default value of 4
    print(a, b, c)


foo(1, 2, 3)  # Positional Argument
foo(a=1, b=2, c=3)  # Keyword Argument


# Forced Keyword Arguments
def foo(a, b, *args, c, d):
    print(a, b)

    for arg in args:
        print(arg)

    print(c, d)


foo(1, 2, 3, 4, c=5, d=6)


# Unpacking Arguments
def foo(a, b, c):
    print(a, b, c)


my_list = [0, 1, 2]
foo(*my_list)  # This will unpack my_list[0] to a, [1] to b and [2] to c
# This can also be done with a dictionary, but they key names should be same as the parameter names.
