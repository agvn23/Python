### Sets ###   Unordered. Mutable. No duplicates. No indexing. Iterable. Heterogeneous. Static.

# 1. Creating a Set
# Sets are written with curly brackets {} or the set() constructor.
my_set = {"apple", "banana", "cherry", "apple"}  # Duplicate "apple" will be removed automatically
print("Initial set:", my_set)

# 2. Unordered Nature
# The order of elements in the printed set may vary.
print("Accessing set elements (unindexed):")
for item in my_set:
    print(item)
# 3. Unchangeable Items
# Attempting to change an individual element will result in an error.
#my_set[0] = "orange"  # This will raise an error because sets are unindexed.

# 4. Adding and Removing Items
# Although individual items cannot be changed, you can add or remove items from the set.
my_set.add("date")
print("After adding 'date':", my_set)

my_set.remove("banana")
print("After removing 'banana':", my_set)

# remove() raises an error if item doesn't exist
#my_set.remove('papaya')

# Using discard() to remove an item that might not be present:
my_set.discard("kiwi")  # Does nothing if 'kiwi' is not in the set, no error raised.

# 5. Membership Testing
if "cherry" in my_set:
    print("'cherry' is in the set")

### Accessing ###

# Create a set with some initial items
fruits = {"apple", "banana", "cherry"}
print("Original set:", fruits)

# Accessing items:
# Membership testing
if "apple" in fruits:
    print("Apple is in the set.")

# Iterating over items
print("Iterating over set items:")
for fruit in fruits:
    print(fruit)

# Adding items:
fruits.add("date")          # Adding a single item
print("\nAfter adding 'date':", fruits)

more_fruits = {"elderberry", "fig", "grape"}
fruits.update(more_fruits)  # Adding multiple items
print("After updating with more fruits:", fruits)

# Removing items:
fruits.remove("banana")     # Remove 'banana'; error if not found
print("\nAfter removing 'banana':", fruits)

fruits.discard("kiwi")     # Attempt to remove 'kiwi', no error if not present
print("After discarding 'kiwi' (which may not be present):", fruits)

# Using pop to remove an arbitrary item
removed = fruits.pop()
print("\nAfter pop(): removed", removed)
print("Set now:", fruits)

# Clearing the set
fruits.clear()
print("\nAfter clear():", fruits)