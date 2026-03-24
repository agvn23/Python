### Lists ###   Ordered. Mutable. Allows duplicates. Indexed. Iterable. Heterogeneous. Dynamic.

# Creating a list using square brackets
my_list = ["apple", "banana", "cherry"]
print("Initial List:", my_list)

# Ordered - values can be accessed by their index
print("\nFirst element: ", my_list[0])
print("\nSecond element: ", my_list[1])
print("\nThird element: ", my_list[2])
# An index value out of range throws an error
#print("\nFourth element: ", my_list[3])

# Changeable - we can change, add or remove items
my_list.append("cucumber")
print("\nAfter adding a new entry: ", my_list)
my_list[1] = "blueberry"
print("\nAfter changing the second item to 'blueberry':", my_list)

my_list.remove("cherry")
print("\nAfter removing 'cherry':", my_list)

# Allow duplicates
my_list.append("apple")

print("\nFinal List:", my_list)

# Order hasn't change even if values were removed
print("\nFirst element: ", my_list[0])
print("\nSecond element: ", my_list[1])
print("\nThird element: ", my_list[2])
print("\nThird element: ", my_list[3])

### Accessing ###

my_list = ["apple", "banana", "cherry", "date", "elderberry"]
print("Original list:", my_list)

# 1. Accessing elements
print("\n--- Accessing Elements ---")
print("Index 0:", my_list[0])        # First item
print("Index -1:", my_list[-1])      # Last item
print("Index range 1:3:", my_list[1:3])  # Items from index 1 to 2
print("Index range :2:", my_list[:2])   # Items from start up to (not including) index 2
print("Index range 2::", my_list[2:])   # Items from index 2 to the end

# 2. Check if item exists
print("\n--- Check if 'banana' in list ---")
if "banana" in my_list:
    print("Yes, 'banana' is in the list.")

# 3. Change items by index
print("\n--- Changing Items by Index ---")
my_list[1] = "blueberry"
print("After changing index 1 to 'blueberry':", my_list)

# 4. Change items by range of values
print("\n--- Changing a Range of Items ---")
my_list[1:3] = ["grape", "fig"]  # Replace items at indexes 1 and 2
print("After replacing indexes 1 and 2 with 'grape' and 'fig':", my_list)

# 5. Insert method
print("\n--- Insert Method ---")
my_list.insert(2, "blackberry")
print("After inserting 'blackberry' at index 2:", my_list)

# 6. Append method
print("\n--- Append Method ---")
my_list.append("honeydew")
print("After appending 'honeydew':", my_list)

# 7. Extend method
print("\n--- Extend Method ---")
another_list = ["kiwi", "lime"]
my_list.extend(another_list)
print("After extending with another_list:", my_list)

# 8. Remove method
print("\n--- Remove Method ---")
my_list.remove("fig")
print("After removing 'fig':", my_list)

# 9. Pop method
print("\n--- Pop Method ---")
popped_item = my_list.pop()  # Removes the last item
print(f"Popped item: {popped_item}")
print("After popping last item:", my_list)
popped_item_index = my_list.pop(0)  # Removes the item at index 0
print(f"Popped item from index 0: {popped_item_index}")
print("After popping item from index 0:", my_list)

# 10. Del keyword
print("\n--- Del Keyword ---")
del my_list[1]  # Delete the item at index 1
print("After deleting item at index 1:", my_list)

# 11. Clear method
print("\n--- Clear Method ---")
my_list.clear()
print("After clearing all items:", my_list)
