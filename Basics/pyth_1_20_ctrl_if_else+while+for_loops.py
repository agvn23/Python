### Control If Else ###

# Simple if
number = 10 # Change the value of 10 to see how the conditions behave
if number > 5:
    print("Number is greater than 5")

# if...else
if number % 2:
    print("Number is odd")
else:
    print("Number is even")

# if, elif, else
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: D or below")

# Shorthand if...else (ternary operator)
result = "odd" if number % 2 else "even"
print("The number is", result)

# The following block will throw an error if uncommented
#if number > 0:
#print("Positive number")

### Control while Loop ###

# 1. Simple While Loop
print("Simple While Loop:")
count = 1
while count <= 5:
    print("Count:", count)
    count += 1
else: 
    print("Simple loop finished.\n")

# 2. While Loop with continue (starting count at 1)
print("While Loop with 'continue' (skipping even numbers):")
count = 0
while count < 10:
    count += 1
    if count % 2 == 0:
        continue  # Skip printing for even numbers
    print("Odd number:", count)
print("Finished skipping even numbers.\n")

# 3. While Loop with break and else

print("While Loop with 'break'")
i = 1
while i < 6:
  print(i)
  if (i == 3):
    break
  i += 1
else:
    print("This won't be executed")

print("Search completed.")

### Control for Loop ###

# Looping over a list
my_list = [1, 2, 3, 4]
print("Iterating over a list:")
for item in my_list:
    print(f"List item: {item}")
print()  # Blank line for readability

# Looping over a tuple
my_tuple = ('apple', 'banana', 'cherry')
print("Iterating over a tuple:")
for fruit in my_tuple:
    print(f"Tuple fruit: {fruit}")
print()

# Looping over a dictionary by keys
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
print("Iterating over a dictionary (keys):")
for key in my_dict:
    print(f"Key: {key}, Value: {my_dict[key]}")
print()

# Looping over a dictionary using items() to get key-value pairs directly
print("Iterating over a dictionary with items():")
for key, value in my_dict.items():
    print(f"{key}: {value}")
print()

# Looping over a set
my_set = {10, 20, 30, 40}
print("Iterating over a set:")
for num in my_set:
    print(f"Set number: {num}")
print()

# Looping over a string
my_string = "Hello"
print("Iterating over a string:")
for char in my_string:
    print(f"Character: {char}")
print()

# Using range() in a for loop to generate a sequence
print("Using range() to iterate over a sequence of numbers:")
for i in range(5):  # Generates numbers from 0 to 4
    print(f"Number from range: {i}")
print()

# Loop with 'continue'
for num in range(5):
    if num == 2:
        continue  # Skips the rest of this iteration when num equals 2
    print(num)
print()

# Loop with 'break'
for num in range(3):
    print(num)
else:
    print("Loop completed without a break.")
print()
# Nested loop
words = ["apple", "banana", "cherry", "watermelon"]
target_letter = "n"
print("Words containing the letter 'n':")
for word in words:
    for letter in word:
        if letter == target_letter:
            print(f"{word} contains '{target_letter}'")
            break  # Stop checking the current word once target letter is found



