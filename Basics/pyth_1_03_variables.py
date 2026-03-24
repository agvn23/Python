# Creating variables and naming rules
name = "Alice"  # String variable. Type is assumed from the value.
age = 25        # Integer variable. Type is assumed from the value.
_height = 5.6   # Float variable. Type is assumed from the value.

# Many values to multiple variables
a, b, c = 1, 2, 3  # Assign multiple values at once

# One value to multiple variables
x = y = z = 10     # Assign the same value to multiple variables

# Casting
int_value = int(5.5)    # Cast to integer. Type is enforced.
str_value = str(100)    # Cast to string. Type is enforced.
float_value = float(3)  # Cast to float. Type is enforced.

# Getting the type of a variable
print(type(name))  # Outputs: <class 'str'>
print(type(age))   # Outputs: <class 'int'>

# Single vs Double Quotes
print("It's a beautiful day")  # Double quotes for strings with single quotes
print('He said "Hello"')       # Single quotes for strings with double quotes

# Case Sensitivity
Name = "John"
name = "Jane"
print(Name)  # Outputs: John
print(name)  # Outputs: Jane

# Printing and Type Checking
# This will throw an error:
#print("Age is " + age)

# Correct way: convert age to string
print("Age is " + str(age))

# Global Variables
global_var = "I am global"

# 👇 This is how a function looks in Python
def test_global():
    # The local_var can only be accessed from within the function
    local_var = 'This value is local'
    global global_var               # Declare to modify the global variable
    global_var = "Changed globally" # Now this will assign this new value

# 👇 and this is how you call a function in Python
test_global()

#print(local_var)  # This would trigger an error. Uncomment to see what happens
print(global_var)  # Outputs: Changed globally



##### Challange #####

# Step 1: Create variables:
name = Bob
age = 26
height = 1.8

# Step 2: Print the variables:
message = f'{name}, {age}, {height}'
print(message)

# Step 3: Check the type of the variables:
print(type(name))
print(type(age))
print(type(height))

# Step 4: Casting
name = Bob
age = str(input("26")) = age_str
height = float(input("1.8"))
print(f"My name is ,{name}, and I am {age_str}  ") 

# Bonus: Global Variable (Bonus)
global_var = "I am global"
def test_global():
    local_var = 'This value is local'
    global global_var
    global_var = "Changed globally"
test_global()
print(global_var)