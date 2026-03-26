### Radix Sort ###

def get_digit(number, d):
    """Return d-th digit of number, where d=0 is LSD."""
    return (number // 10**d) % 10

def counting_sort_by_digit(arr, d):
    """Stable counting sort of arr by digit d."""
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    for value in arr:
        digit = get_digit(value, d)
        count[digit] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    for i in range(n - 1, -1, -1):
        digit = get_digit(arr[i], d)
        count[digit] -= 1
        new_index = count[digit]
        output[new_index] = arr[i]
    return output

def radix_sort(arr):
    if not arr:
        return arr
    max_val = max(arr)
    k = 0
    while 10**k <= max_val:
        arr = counting_sort_by_digit(arr, k)
        k += 1
    return arr

my_array = [170, 45, 75, 90, 802, 24, 2, 66]
sorted_array = radix_sort(my_array.copy())
print("Original Array:", my_array)
print("Sorted Array:", sorted_array)

### Merge Sort ###

def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)
    return arr

def merge(arr, left, mid, right):
    # Create temporary arrays
    n1 = mid - left + 1
    n2 = right - mid
    L = [0] * n1
    R = [0] * n2
    
    for i in range(n1):
        L[i] = arr[left + i]
    for j in range(n2):
        R[j] = arr[mid + 1 + j]
    
    # Merge step
    i = 0
    j = 0
    k = left
    
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    
    # Copy remaining elements
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

# Example usage
my_array = [38, 27, 43, 3, 9, 82, 10]
sorted_array = merge_sort(my_array.copy(), 0, len(my_array) - 1)
print("Original Array:", my_array)
print("Sorted Array:", sorted_array)