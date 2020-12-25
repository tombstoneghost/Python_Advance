# Working with Context Managers in Python
from threading import Lock
from contextlib import contextmanager

# Here the Context Manager will close the file properly automatically
with open('notes.txt', 'w') as file:
    file.write("Some Todo...")

# When we want to use a lock while working on multi-threading or multi-processing
lock = Lock()

with lock:
    print("Hello World")


# Custom Context Manager
class ManagedFile:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        print("Enter")
        self.file = open(self.filename, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        print('Exit')


with ManagedFile('notes.txt') as file:
    file.write('Some todo...')


# Creating a Context Manager Function
@contextmanager
def open_managed_file(filename):
    f = open(filename, 'w')

    try:
        yield f
    finally:
        f.close()


with open_managed_file('notes.txt') as file:
    file.write('Some Todo...')
