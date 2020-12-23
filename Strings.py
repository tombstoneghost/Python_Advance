# Strings: Ordered, immutable, text representation
my_string = "Hello World!"

'''
my_string = "Hello \
World"""
'''

print(my_string)

# Extract a character from a string
char = my_string[0]
print(char)

'''
You cannot access a character and change it as strings are immutable.
Which means, my_string[0]="G" is not possible
'''

# Substring
substring = my_string[1:5]  # You can also add step size as well
print(substring)

# Concatenating Strings
greeting = "Hello"
name = "Tom"
sentence = greeting + name
print(sentence)

# Iterating a String
for i in greeting:
    print(i)

# Check for Character/SubString inside a String
if 'e' in greeting:
    print("Yes")
else:
    print("No")

if 'ell' in greeting:
    print("Yes")
else:
    print("No")

# Removes all WhiteSpaces from beginning and end
new_string = '     Hello World     '
new_string = new_string.strip()
print(new_string)

# Convert to UpperCase or LowerCase
print(my_string.upper())

print(my_string.lower())

# Check if the String starts with or ends with a particular character/substring
print(my_string.startswith("Hel"))
print(my_string.endswith("rld"))

# Find a character/Substring and it will return the index number
print(my_string.find('o'))

# Count number of characters/substrings it finds
print(my_string.count('o'))

# Replace a character/substring
print(my_string.replace('World', 'Universe'))

# Converting words to a list
new_string2 = 'how are you doing'
my_list = new_string2.split()
print(my_list)

# Converting back List to String
new_string3 = ' '.join(my_list)
print(new_string3)

# Formatting Strings (Old Style)
var = "Tom"
my_string4 = "The Variable is %s" % var
print(my_string4)

var = 5
my_string4 = "The Variable is %d" % var
print(my_string4)

# Formatting Strings (New Style)
var = 3.1234567
var2 = 6
my_string4 = "the variable is {:.2f} and {}".format(var, var2)
print(my_string4)

my_string4 = f"the variable is {var} and {var2}"
print(my_string4)
