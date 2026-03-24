### List Methods ###

# Starting list
my_list = [3, 1, 4, 1, 5, 9]
print("Original list:", my_list)

# 1) append()
my_list.append(2)
print("\nAfter append(2):", my_list)

# 2) clear() - We'll do this on a separate list to avoid losing data
temp_list = [10, 20, 30]
print("\nTemp list before clear():", temp_list)
temp_list.clear()
print("Temp list after clear():", temp_list)

# 3) copy()
copied_list = my_list.copy()
print("\nCopied list:", copied_list)

# 4) count()
ones_count = my_list.count(1)
print(f"\nCount of '1' in my_list: {ones_count}")

# 5) extend()
another_list = [7, 8, 9]
my_list.extend(another_list)
print("\nAfter extend([7, 8, 9]):", my_list)

# 6) index()
index_of_4 = my_list.index(4)
print("\nIndex of '4':", index_of_4)

# 7) insert()
my_list.insert(1, "new")
print("\nAfter insert(1, 'new'):", my_list)

# 8) pop()
popped_item = my_list.pop()  # By default, pops the last item
print("\nAfter pop() - removed item:", popped_item)
print("my_list after pop():", my_list)

popped_item_1 = my_list.pop(1)  # Remove item at index 1
print(f"After pop(1) - removed item '{popped_item_1}' at index 1:", my_list)

# 9) remove()
my_list.remove(1)  # Remove the first occurrence of 'new'
print("\nAfter remove(1):", my_list)

# 10) reverse()
my_list.reverse()
print("\nAfter reverse():", my_list)

# 11) sort()
my_list.sort()
print("\nAfter sort():", my_list)


### List Exercise ###

# --- 1. Create and Print a List ---
# Creating a list of 5 fruits
my_list = ["apple", "banana", "cherry", "mango", "strawberry"]
print("Original List:", my_list)

# --- 2. Access Elements by Index and Negative Index ---
# First item (index 0)
print("First item:", my_list[0])
# Last item (index -1)
print("Last item:", my_list[-1])
# Second to last item (index -2)
print("Second to last item:", my_list[-2])

# --- 3. Slice a List ---
# Subset from index 1 to 3 (doesn't include 3)
print("Slice [1:3]:", my_list[1:3])
# Beginning up to index 2
print("Slice [:2]:", my_list[:2])
# Index 2 to the end
print("Slice [2:]:", my_list[2:])

# --- 4. Check if an Item Exists ---
if "apple" in my_list:
    print("apple is in the list")


# --- 5. Add Items ---
# Append to the end
my_list.append("durian")
print("After append('durian'):", my_list)

# Insert at specific index (index 1)
my_list.insert(1, "blueberry")
print("After insert(1, 'blueberry'):", my_list)

# --- 6. Change Items ---
# Update a specific element (change index 2)
my_list[2] = "coconut"
print("After changing index 2 to 'coconut':", my_list)

# Change multiple items (slice assignment)
# Replacing items at index 1 and 2 with two new items
my_list[1:3] = ["blackberry", "cantaloupe"]
print("After slice assignment [1:3]:", my_list)

# --- 7. Remove Items ---
# Remove by value
if "mango" in my_list:
    my_list.remove("mango")
print("After removing 'mango':", my_list)

# Remove by index using pop (removing index 0)
popped_item = my_list.pop(0)
print(f"Popped item: {popped_item}")
print("After popping index 0:", my_list)

# Clear list (Demo using a temporary list so we don't lose our main list)
temp_list = ["a", "b", "c"]
temp_list.clear()
print("Cleared temp_list:", temp_list)

# --- 8. Copy a List ---
# Create a copy
list_copy = my_list.copy()

# Modify the original to show independence
my_list.append("guava")

print("Original List (modified):", my_list)
print("Copy List (unchanged): ", list_copy)

# --- 9. Concatenate and Extend ---
list_a = [1, 2]
list_b = [3, 4]

# Using + operator (creates a new list)
joined_list = list_a + list_b
print("Joined with +:", joined_list)

# Using extend() (modifies list_a in place)
list_a.extend(list_b)
print("List A after extend:", list_a)

# --- 10. Sort and Reverse ---
# We will use the 'list_copy' from step 8 since it is cleaner
print("Current list to sort:", list_copy)

# Sorting (Permanent change)
list_copy.sort()
print("Sorted:", list_copy)

# Reversing (Permanent change)
list_copy.reverse()
print("Reversed:", list_copy)

# Optional: Sorted() function (Non-permanent)
numbers = [5, 1, 8, 3]
sorted_numbers = sorted(numbers)
print(f"Original numbers: {numbers}, New sorted list: {sorted_numbers}")

# --- 11. Count and Index ---
# Let's add a duplicate to demonstrate count
my_list.append("apple")
print("List for counting:", my_list)

count_apple = my_list.count("apple")
print(f"Count of 'apple': {count_apple}")

# Find index of 'apple' (finds the first one)
index_apple = my_list.index("apple")
print(f"Index of first 'apple': {index_apple}")

# --- 12. List Comprehension (Bonus) ---
# Convert all fruits to UPPERCASE
# Store only words that are more than or equal to 5
upper_fruits = [fruit.upper() for fruit in my_list if len(fruit) <= 3]
print("Uppercase fruits", upper_fruits)

