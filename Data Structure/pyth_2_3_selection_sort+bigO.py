### Selection Sort ###

def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

unsorted_array = [64, 25, 12, 22, 11]
sorted_array = selection_sort(unsorted_array.copy())

print("Original Array:", unsorted_array) # Original Array: [64, 25, 12, 22, 11]
print("Sorted Array:", sorted_array) # Sorted Array: [11, 12, 22, 25, 64]


### Big O Notation ###

import random

def selection_sort_with_operations(arr):
    n = len(arr)
    comparisons = 0
    swaps = 0
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            comparisons += 1  # Count the comparison
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            swaps += 1  # Count the swap
    return comparisons, swaps, swaps + comparisons

# Test Cases: Best, Worst and Average
# Change the number of elements in the array
# ⚠️ A large enough value WILL crash your browser 💥
num_elements = 100
best_case_array = list(range(1, num_elements + 1 ))
average_case_array = random.sample(best_case_array, len(best_case_array))
worst_case_array = best_case_array[::-1]

# Run sorting function
best_comparisons, best_swaps, best_operations = selection_sort_with_operations(best_case_array.copy())
avg_comparisons, avg_swaps, avg_operations = selection_sort_with_operations(average_case_array.copy())
worst_comparisons, worst_swaps, worst_operations = selection_sort_with_operations(worst_case_array.copy())

# Print results
print("Best Case Scenario:")
print("Comparisons:", best_comparisons)
print("Swaps:", best_swaps)
print("Total Operations:", best_operations)

print("\nAverage Case Scenario:")
print("Comparisons:", avg_comparisons)
print("Swaps:", avg_swaps)
print("Total Operations:", avg_operations)

print("\nWorst Case Scenario:")
print("Comparisons:", worst_comparisons)
print("Swaps:", worst_swaps)
print("Total Operations:", worst_operations)