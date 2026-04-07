### Insertion Sort ###

unsorted_list = [34, 9, 27, 45, 9]

def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):                       # 1, 2, 3, 4
        insert_index = i                        # keeps track of hole index
        current_value = arr[i ]                 # keeps track of value

        for j in range(i-1, -1, -1):            # sorted items from right to left
            if arr[j] > current_value:          # Comparison j (last sorted) i (next sorted)
                arr[j+1] = arr[j]               # move j to the right, up one index
                insert_index = j 
            else:                               # Saves rechecking,  
                break                           # if ommited answer reamins the same

            arr[insert_index] = current_value   # replace i into the vacant index left by j 

    return arr 

print(insertion_sort(unsorted_list))


for i in range (0, 5):           # index 0 start, 5 end at 4, 0 steps default +1
    print(i)                     # 0, 1, 2, 3, 4  EACH i ON NEW LINE

for i in range (0, 10, 2):       # index 0 start, 10 end at 9, 2 steps /incruments
    print (i)                    # 0, 2, 4, 6, 8  EACH i ON NEW LINE  

for i in range (-1, -1, -1):     # index -1 start, -4 end at -3, -1 steps countbackwards 
    print(i)                     # 1-, -2, -3.    EACH i ON NEW LINE    

def insertion_sort(arr):
    n = len(arr)
    for i in range(1,n):
        insert_index = i
        current_value = arr[i]
        for j in range(i-1, -1, -1):
            if arr[j] > current_value:
                arr[j+1] = arr[j]
                insert_index = j
            else:
                break
        arr[insert_index] = current_value
    return arr

unsorted_array = [12, 11, 13, 5, 6]
sorted_array = insertion_sort(unsorted_array.copy())
print("Original Array:", unsorted_array)  # [12, 11, 13, 5, 6]
print("Sorted Array:", sorted_array)      # [5, 6, 11, 12, 13]

### Big O Notation ###

import random

def insertion_sort_with_operations(arr):
    n = len(arr)
    comparisons = 0
    shifts = 0
    for i in range(1,n):
        insert_index = i
        current_value = arr[i]
        for j in range(i-1, -1, -1):
            comparisons += 1 # Count comparison
            if arr[j] > current_value:
                shifts += 1 # Count shifts
                arr[j+1] = arr[j]
                insert_index = j
            else:
                break
        arr[insert_index] = current_value
    return comparisons, shifts, comparisons + shifts

# Test Cases: Best, Worst and Average
num_elements = 100
best_case_array = list(range(1, num_elements + 1))
average_case_array = random.sample(best_case_array, len(best_case_array))
worst_case_array = best_case_array[::-1]

# Run sorting function
best_comparisons, best_shifts, best_operations = insertion_sort_with_operations(best_case_array.copy())
avg_comparisons, avg_shifts, avg_operations = insertion_sort_with_operations(average_case_array.copy())
worst_comparisons, worst_shifts, worst_operations = insertion_sort_with_operations(worst_case_array.copy())

print("Best Case Scenario:")
print("Comparisons:", best_comparisons)
print("Shifts:", best_shifts)
print("Total Operations:", best_operations)

print("\nAverage Case Scenario:")
print("Comparisons:", avg_comparisons)
print("Shifts:", avg_shifts)
print("Total Operations:", avg_operations)

print("\nWorst Case Scenario:")
print("Comparisons:", worst_comparisons)
print("Shifts:", worst_shifts)
print("Total Operations:", worst_operations)


