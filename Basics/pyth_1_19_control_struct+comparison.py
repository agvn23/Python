### Control Structure ###

# Sequential Execution: instructions run one after another
print("Starting program")
a = 5
b = 10
sum_ab = a + b
print("The sum of", a, "and", b, "is", sum_ab)

# Decision Making with if-elif-else
if sum_ab > 10:
    print("The sum is greater than 10.")
elif sum_ab == 10:
    print("The sum is exactly 10.")
else:
    print("The sum is less than 10.")

# Pattern Matching (Python 3.10+)
day = 3
print("\nUsing pattern matching for day number:")
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case _:
        print("Another day")

# Repetition: For Loop on list
fruits = ['cherry', 'banana', 'apple']
for fruit in fruits:
    print(f"I really like {fruit}")

# Repetition: While Loop
print("\nWhile loop until count reaches 5:")
count = 0
while count < 5:
    print(count)
    count += 1

### Control Comparison ###    

# Define some sample variables
x = 10
y = 20
z = 10
a = 5
b = 15

# Equal (==)
print("Is x equal to y?", x == y)       # Expected: False
print("Is x equal to z?", x == z)       # Expected: True

# Not equal (!=)
print("Is x not equal to y?", x != y)   # Expected: True
print("Is x not equal to z?", x != z)   # Expected: False

# Greater than (>)
print("Is y greater than x?", y > x)    # Expected: True
print("Is a greater than b?", a > b)    # Expected: False

# Less than (<)
print("Is x less than y?", x < y)       # Expected: True
print("Is b less than a?", b < a)       # Expected: False

# Greater than or equal to (>=)
print("Is x greater than or equal to z?", x >= z)  # Expected: True
print("Is y greater than or equal to b?", y >= b)  # Expected: True

# Less than or equal to (<=)
print("Is x less than or equal to z?", x <= z)     # Expected: True
print("Is a less than or equal to b?", a <= b)     # Expected: True

# Additional combined comparisons
print("Is x equal to 10 and y greater than 15?", (x == 10) and (y > 15))  # True and True -> True
print("Is a less than 10 or b greater than 100?", (a < 10) or (b > 100))   # True or False -> True
