### List Comprehensions ###

# 1. Simple transformation
numbers = [1, 2, 3, 4, 5]
squares = [num ** 2 for num in numbers]
print("Original numbers:", numbers)
print("Squares:", squares)

# 2. Filtering
even_numbers = [num for num in numbers if num % 2 == 0]
print("\nEven numbers:", even_numbers)

# 3. Data transformation with condition
fruits = ["apple", "banana", "cherry", "date"]
short_fruits = [fruit.upper() for fruit in fruits if len(fruit) <= 5]
print("\nOriginal fruits:", fruits)
print("Short fruits (5 letters or fewer, in uppercase):", short_fruits)

# 4. Using range in list comprehension
multiples_of_three = [x for x in range(1, 20) if x % 3 == 0]
print("\nMultiples of 3 (1-19):", multiples_of_three)

# 5. Nested list comprehension (all pairs of letters)
letters = ["A", "B", "C"]
pairs = [[x, y] for x in letters for y in letters if x != y]
print("\nAll possible distinct pairs:", pairs)

### List Sorting ###

# 1. Sorting
numbers = [5, 2, 9, 1, 5, 6]
print("Original list of numbers:", numbers)

# In-place sort (ascending)
numbers.sort()
print("Sorted in-place (ascending):", numbers)

# Sort in descending order using sorted()
desc_numbers = sorted(numbers, reverse=True)
print("Descending order (new list):", desc_numbers)

# 2. Copying
original_list = ["apple", "banana", "cherry"]
reference_list = original_list  # Passes reference, not a true copy
copy_list_1 = original_list.copy()  # Creates a shallow copy (new list in memory)
copy_list_2 = original_list[:] # Another way to create a shallow copy

# Modify the original to see the difference
original_list.append("date")
print("\nAfter appending 'date' to original_list:")
print("original_list:", original_list)
print("reference_list (points to same list):", reference_list)
print("copy_list_1 (separate list):", copy_list_1)
print("copy_list_2 (separate list):", copy_list_2)

# 3. Joining Lists
list_a = [1, 2, 3]
list_b = [4, 5, 6]
list_c = list_a + list_b  # Concatenate
print("\nJoin with '+':", list_c)

# Using extend()
list_a.extend(list_b)
print("After list_a.extend(list_b):", list_a)

# Using a for ... in loop with append()
list_f = [100, 200]
list_g = [300, 400]
for item in list_g:
    list_f.append(item)
print("After for-loop append:", list_f)