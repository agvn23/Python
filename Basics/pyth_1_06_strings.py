#-------------------------------------STRINGS------------------------------------
# TYPES  | MATH     | TRANSFORMATIONS | CLEANING          | SEARCH        | VALIDATION
# types()| len()    | replace()       | #clean whitespace | startswith()  | isalpha()
# str()  | count()  |   +             | lstrip()          | endswith()    | isnumeric()
#                   |   f             | rstrip()          | find() 
#                   | split()         | strip()           | in
#                   |   *             | #clean cases
#                   |  [0]            | lower()
#                   |  [1:3]          | upper()

# TYPES 
name = "Jorge"
print(type(name))      #<class 'str'>

age = 60
print(type(age))       #<class 'int'>
print('Your Age is:' + str(age))
print(type(age))       #<class 'int'>
age = str(age)
print(type(age))       #<class 'str'>

# Single and Double Quotes
single_quote = 'Hello'
double_quote = "It's a beautiful day"
print(single_quote)
print(double_quote)

# Multi-Line Strings
multiline = """This is
a multi-line 
string."""
print(multiline)

# Strings are Arrays
text = "Python"
print("First character:", text[0])
print("Last character:", text[-1])

# Looping Through a String
for char in text:
    print(char)

# String Length (maths)
print("Length of the string:", len(text))

password ="123a76354rrrt"
print(len(password))

if len(password) < 8:
    print('Your password is too short!')

# Count (maths)
text ='''
Python is easy.
Python is powerful.
many ppl love python
'''  
print(text)
print(text.count('Python'))         # returns 2 pyThOn iS cAsE SensItivE
print(text.lower().count('python')) # returns 3

# Check if String Exists
phrase = "Learning Python is fun!"
print("Python" in phrase)
print("fun" not in phrase)

# Slicing Strings
print("Slice 0-6:", text[0:6])
print("Slice from 3:", text[3:])

# Modifying Strings
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Trimmed:", "     Hello     ".strip())
print("Replace:", text.replace("Py", "My"))
print("Split:", text.split("t"))

# Concatenation
first_name = "John"
last_name = "Doe"
print("Full name:", first_name + " " + last_name)

# String Formatting
age = 34
name = "Jorge"
# Format function
print("I am {name} and I'm {age} years old.".format(name = "Jorge", age = 34))
print("I am {name} and I'm {age} years old.".format(name = "Jorge", age = 34))
print("I am {} and I'm {} years old.".format("Jorge", 34))
# f-string
print(f"I am {name} and I'm {age} years old.")

# Escaping Characters
escaped = "He said \"Python is great!\""
print(escaped)

# String Methods
example = " python programming "
print("Capitalized:", example.capitalize())
print("Count of 'p':", example.count('p'))
print("Is alphanumeric:", example.isalnum())
print("Stripped:", example.strip())
print("Replaced 'python':", example.replace("python", "Java"))

# Transformations
price = "$1234,56"
print(price.replace(',', '.').replace('$', ''))
phone = "176-1234-56"
print(phone.replace('-', ''))   