### Binary Search ###

# BINARY SEARCH. divide and conquer SORTED ONLY

# TARGET = 11

sorted_array = [1, 3, 5, 7, 9, 11, 13, 15]
taget = 11

#  [1, 3, 5, 7, 9, 11, 13,15]   Divide Find Middle
#                               index (0+7)//2 = 3, add first and last index then floor divide by 2
# [1, 3, 5, 7]-[9, 11, 13, 15]  split at index 3 
# 7 = 11 + 7 < 11               Check last index value on first split
#      [9, 11, 13, 15]          If not disgard 1st split
#     [9, 11] - [13, 15].       divide index (4+7)//2=5 add original index divide
# 11 = 11                       If yes return index 5 

def binary_search(arr, target):
    start = 0
    end = len(arr) -1

    while start <= end:                  # while loop
        mid_index = (start + end) // 2   # index 3
        mid_value = arr[mid_index]       # value at index 3 (7)

        if mid_value == target:
            return mid_index
        elif mid_value < target:
            start = mid_index + 1
        else:
            end = mid_index - 1

print(binary_search(sorted_array, 11))


def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1  # Not found

# Example usage
sorted_numbers = [1, 3, 5, 7, 9, 11, 13, 15]
index = binary_search(sorted_numbers, 11)

if index != -1:
    print(f"Found 11 at index {index}")
else:
    print("11 not found")
