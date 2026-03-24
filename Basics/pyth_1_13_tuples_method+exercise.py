### Methods ###

# 1. Create a Tuple
my_tuple = ("apple", "banana", "cherry", "banana", "date", "banana")

# 2. Using the count() method
banana_count = my_tuple.count("banana")
print("The word 'banana' appears:", banana_count, "times in my_tuple.")

# 3. Using the index() method
first_banana_index = my_tuple.index("banana")
print("The first occurrence of 'banana' is at index:", first_banana_index)

# Trying index() on a value that does not exist will raise an error
# Uncomment the next line to see the error
# my_tuple.index("grape")

### Exercise ###

#1 Create A Tuple

my_tuple =("ginger", 143, "dance", 23)

#2 print access slice 
print(my_tuple)
print(my_tuple[0])         #first item
print(my_tuple [-1])       #last item
print(my_tuple [1:3])      #middle items
print(my_tuple [:2])       #first to x
print(my_tuple [2:])       #x to last

#3 check if item exists

if "dance" in my_tuple:
    print("dance is in tuple")

#4 count and index

ginger_count = my_tuple.count("ginger")    
print("The word 'ginger' appears:", ginger_count, "times in my_tuple.")

first_ginger_index = my_tuple.index("ginger")
print("The first occurrence of 'ginger' is at index:", first_ginger_index)

#5 packing unpacking

fruit1, number1, activity1, number2 = my_tuple     #packing 
print(fruit1)                                      #unpacking
fruit_a, number_a, *others = my_tuple
print(others)

#6 joining

another_tuple =("tea", "milk", "cookies")
print(another_tuple)
combined_tuple = my_tuple + another_tuple
print(combined_tuple)

repeated_items = my_tuple *3
print(repeated_items)