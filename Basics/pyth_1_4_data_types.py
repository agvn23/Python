#-------------------------------------------------------DATA TYPES-----------------------------------------------------------
#
#  No Value |                  Single Value               |                   Multi Values
#           |          |          |        |              |          |          |          |          |
#  NoneType | Numeric, | str,     | bool,  | Date & Time, | list,    | tuple,   |  set,    |  dict,   |   array
#   (None)  |          |("Hello") |(True)  |              |([1,2,3]) |((1,2,3)) |({1,2,3}) |({"a":1,  |(array("i",[10,20]))
#           | int                 |(False) | date         |                                   "a":1, 
#           | (15)                           (2026-09-20) |                                   "b":2
#           | float                          time         |                                  })
#           | (3.1415)                       (18:05:30)   | 
#----------------------------------------------------------------------------------------------------------------------------


# Dynamic Typing: Python detects the type automatically
name = "Alice"  # String. All kinds of text.
age = 25        # Integer. Good for ages, amounts, etc.
height = 5.6    # Float. Good for prices or accurate data.
is_student = True  # Boolean. Good for using in conditions!

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Student Status:", is_student)

# Type checking
print("The type of 'name' is:", type(name))      # <class 'str'>
print("The type of 'age' is:", type(age))        # <class 'int'>
print("The type of 'height' is:", type(height))  # <class 'float'>

# Type Safety in Operations
# This will throw an error because of type mismatch, uncomment to see it
#print("Next year, your age will be " + age)

# Fix with Explicit Typing (Casting)
print("Next year, your age will be " + str(age))

# Explicit Typing (Casting Examples)
x = 10.5
y = int(x)     # Cast to integer
z = float(10)  # Cast to float

print("Casted int from float:", y)
print("Casted float from int:", z)

# Example with User Input (Simulated)
user_input = "30"           # Imagine this comes from input()
user_age = int(user_input)  # Convert to integer for calculations
print("Your age next year will be:", user_age + 1)