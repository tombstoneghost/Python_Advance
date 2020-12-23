# Errors and Exceptions
"""
Syntax Error: A syntax error occurs when the parser detects a syntactically
    incorrect statement.

    Eg:
        a = 5 print(a)
        print(a))
        print(a

Exceptions: When a statement in syntactically correct but throws an error
    during execution

    Eg:
        a = 5 + '10'  # Type Error since you cannot sum a int and a string
        import someModule  # Module Error as Module does not exist
        a = 5
        b = c  # Name Error since variable c is not defined
        f = open('someFile.txt')  # File Not Found Error
        a = [1, 2, 3]
        a.remove(4))  # Remove Error
        a[4]  # Index Error, Similar we get the Key Error when using a dictionary
"""

# Raising an Exception
x = -5
if x < 0:
    raise Exception('x should be positive')

# Using Assert Statement
assert (x >= 0), 'x is not positive'

# Handling Exceptions
try:
    a = 5 / 0

except Exception as e:
    print(e)

else:  # If no exception occurs
    print("Everything is fine")

finally:  # Will always run even if the exceptions occurs or not
    print("Cleaning up....")


# Defining own Exceptions
class ValueTooHighError(Exception):
    pass


def test_value(val):
    if val > 100:
        raise ValueTooHighError('Value is too high')


try:
    test_value(200)
except ValueTooHighError as e:
    print(e)
