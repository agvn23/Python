### Big O Notation ###

## 1. Drop the constants 
## 2. Drop the non-dominant term 


def print_numbers(n):
    print("Ready...")        #O(1)     Constant Time  will not increase with more items
    print("Set...")          #O(1)
    print("Go!")             #O(1)

    for num in n:            #O(n)     Linear Time   every item increase by 1
        print(num)           #O(1)
        #ie2 print(num)      #O(1)
    print("Finished!")       #O(1)


# Total = 3 + (n * 1) for each operation in for loop #ie2 (n * 2) + 1  
# sum 4 + (n * 2)
# or  4 + 2n
# remove constant
# = n
# Conclusion O(n)



#------- Example 2 


def complex_printer(list):
    n = len(list)            #O(1)     single operation
#Part A 
    for i in list:           #O(n)     the more input more runs   
        for j in list:       #O(n)
            print(i, j)      #O(1)
    # Total Part A => n * n = n^2
         
#Part B
    for k in list:           #O(n)
        print(k)             #O(1)     is obsolete

    print("finished")        #O(1)   


# 1 + n^2 + n + 1
# n^2 + n  drop the nondominate leave the worst case
# O(n^2) 
 
 
#---------Example 3  


def process_two_lists(list_a, list_b):
    # Loop through first list
    for item in list_a:        #O(a)    Depends on the size of list_a
        print(item)

    # Loop through the second list
    for item in list_b:        #O(b)    Depends on the size of list_b
        print(item)


# a+b
# O(a^2 + b)


#---------


def print_powers_of_n(n):
    i = 1

    while i < n:
        print(i)
        i = i * 2

print_powers_of_n(100)    # n(200) double the number 
                          # would increase print once ie 128
                          # O(logn) just off Constant Time O(1)

#would print
#0
#1
#2
#4
#8
#16
#32
#64

# power of 2 stopping at n = 100 WHILE i < n(100)



#log^2 8 = 3   (2, 4, 8, 16, 32, etc). ie log^2 16 = 4
#log^3 9 = 2   (3, 9, 27, 81, etc)

# FACTORIAL O(n!)  AKA Traveling Salesman

#   City A   City B   City C
#   A > B > C or A > C > B                1 + 1
#   B > C > A or B > A > C                1 + 1
#   C > A > B or C > B > A                1 + 1   
#                                         6 possible routes   
# 1 more input
#   City A    City B   City C   City D    24 possible routes

#number of cities = 2
#2! = 1 * 2 = 2
#3! = 1 * 2 * 3 = 6
#4! = 1 * 2 * 3 * 4 = 24
#5! = 1 * 2 * § * 4 * 5 = 120
#20! = 2,432,902,008,176,640,000