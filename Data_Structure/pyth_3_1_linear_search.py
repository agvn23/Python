### Linear Search ###

list_a = [4, 2, 7, 1, 8]

def linear_search(arr, target):
    for index, value in enumerate(arr):  #For Loop
        if value == target:
            return index
        
print(linear_search(list_a, 7))          # Search for 7 Answer 2 second index
print(linear_search(list_a, 10))         # Search 10 Answer None


def linear_search(arr, target):
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1

# Example usage
numbers = [4, 2, 7, 1, 8]
index = linear_search(numbers, 7)

if index != -1:
    print(f"Found 7 at index {index}")
else:
    print("7 not found")

list_a = [4, 2, 7, 1, 8]

for num in enumerate(list_a):          # For Loop
    print(num)                              #(0, 4)
                                            #(1, 2)
                                            #(2, 7)   prints index and value
                                            #(3, 1)   as pairs TUPLES
                                            #(4, 8)  

for index, value in enumerate(list_a): # unpack TUPLE
    print("index", index)                   # index 0
    print("value", value)                   # value 4
                                            # index 1
                                            # value 2
                                            # index 2
                                            # value 7
                                            # index 3
                                            # value 1
                                            # index 4
                                            # value 8