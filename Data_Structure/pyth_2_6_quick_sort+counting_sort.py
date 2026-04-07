### Quick Sort ###

def quick_sort(arr, left, right):
    if left < right:
        pivot_index = partition(arr, left, right)
        quick_sort(arr, left, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, right)
    return arr

def partition(arr, left, right):
    pivot_value = arr[right]
    i = left - 1
    for j in range(left, right):
        if arr[j] <= pivot_value:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    # Place the pivot in its final position
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1

# Example usage
my_array = [10, 7, 8, 9, 1, 5]
sorted_array = quick_sort(my_array.copy(), 0, len(my_array) - 1)
print("Original Array:", my_array)   # [10, 7, 8, 9, 1, 5]
print("Sorted Array:", sorted_array) # [1, 5, 7, 8, 9, 10]

### Counting Sort ###

def counting_sort(arr, max_val):
    count = [0] * (max_val + 1)
    for x in arr:
        count[x] += 1
    for i in range(1, max_val + 1):
        count[i] += count[i - 1]
    n = len(arr)
    result = [0] * n
    for i in range(n - 1, -1, -1):
        x = arr[i]
        count[x] -= 1
        new_index = count[x]
        result[new_index] = x
    return result

unsorted_array = [4, 2, 2, 8, 3, 3, 1]
max_value = max(unsorted_array)  # 8
sorted_array = counting_sort(unsorted_array, max_value)
print("Original Array:", unsorted_array)
print("Sorted Array:", sorted_array)

