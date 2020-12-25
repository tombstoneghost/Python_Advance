# Shallow Copy and Deep Copy in Python
import copy

org = 5
cpy = org  # This will create a new variable with same reference

print(org)
print(cpy)

org_list = [1, 2, 3, 4, 5]
cpy_list = org_list
cpy_list[0] = 5

print(org_list)
print(cpy_list)

"""
Shallow Copy: One Level Deep and only references of nested child objects
Deep Copy: Full independent copy
"""

# Shallow Copy
org_list = [1, 2, 3, 4, 5]

cpy_list = copy.copy(org_list)
cpy_list[0] = 5

print(org_list)
print(cpy_list)

# Shallow Copy won't work on a nested list.
# Solution: DeepCopy

org_list = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]]
cpy_list = copy.deepcopy(org_list)

cpy_list[0][1] = -10

print(org_list)
print(cpy_list)


# Copying Class Objects
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Company:
    def __init__(self, boss, employee):
        self.boss = boss
        self.employee = employee


p1 = Person('Alex', 27)
p2 = copy.copy(p1)  # Shallow Copy

p1 = Person('Alex', 55)
p2 = Person('Joe', 27)

company = Company(p1, p2)
company_clone = copy.deepcopy(company)  # Deep Copy
company_clone.boss.age = 56
print(company_clone.boss.age)
print(company.boss.age)
