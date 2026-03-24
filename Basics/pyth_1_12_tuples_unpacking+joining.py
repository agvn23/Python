### Unpacking ###

# Packing values into a tuple
my_tuple = ("apple", "banana", "cherry", "date", "elderberry", "fig")

# 1. Basic Unpacking (when the number of items matches the number of variables)
fruit1, fruit2, fruit3, fruit4, fruit5, fruit6 = my_tuple
print("Basic Unpacking:")
print(fruit1, fruit2, fruit3, fruit4, fruit5, fruit6)

# 2. Unpacking with Asterisk on the Last Variable
#    The 'others' variable will be a list containing "cherry", "date", "elderberry", "fig"
(fruit_a, fruit_b, *others) = my_tuple
print("Asterisk on the Last Variable:")
print("fruit_a:", fruit_a)
print("fruit_b:", fruit_b)
print("others (as a list):", others)

# 3. Unpacking with Asterisk in the Middle
#    Python will unpack items into 'middle' until the remainder matches the last variable.
(fruit_x, *middle, fruit_y) = my_tuple
print("Asterisk in the Middle:")
print("fruit_x:", fruit_x)
print("middle (as a list):", middle)
print("fruit_y:", fruit_y)
print()

### Joining ###   Concatenation. Repetition.

# 1. Joining Tuples with Concatenation
fruits1 = ("apple", "banana", "cherry")
fruits2 = ("date", "elderberry", "fig")

# Use the + operator to join (concatenate) the tuples
combined_fruits = fruits1 + fruits2
print("Combined Tuples (Concatenation):", combined_fruits)

# 2. Multiplying Tuples
# Repeat the tuple multiple times using the * operator
repeated_fruits = fruits1 * 2  # This will create a new tuple that repeats fruits1 twice
print("Repeated Tuple (Multiplied):", repeated_fruits)

# Another example using a numeric tuple
numbers = (1, 2, 3)
numbers_repeated = numbers * 3  # Repeats (1, 2, 3) three times
print("Repeated Numbers Tuple:", numbers_repeated)