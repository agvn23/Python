 ############          DATA STRUCTURES        #############
#        LIST []    TUPLE ()     SET {}    DICT {} 
#                   locked     no doubles  key:value

#       Function         vs       Methods  
#     costs = [10, 20, 15]      costs = [10, 20, 15]
#     len(costs)                costs.remove(10)
#     input  ->  func->output   input -> method -> output   
#     [10,20,15]->len->3        [  ,20,15]->remove
#                                 ^<-<-<-<-<-<-' 

### List ###   Ordered. Mutable. Allows duplicates. Indexed. Iterable. Heterogeneous. Dynamic.

# create
empty = []
print(empty)               # []
print(type(empty))         # <class 'list'>
letters = ['a','b','c']
numbers = [1,2,3]
mixed = [1,'a', True, None]
print(mixed)               # [1, 'a', True, None]
print(type(mixed))         # <class 'list'>
# OR
letters2 = list('Python')
print(letters2)            # ['P', 'y', 't', 'h', 'o', 'n']
numbers2 = list(range(1, 6))
print(numbers2)            # [1, 2, 3, 4, 5]

# nested list

matrix =[['a', 'b', 'c'],   # row 0
         ['d', 'e', 'f']]   # row 1

mixed_matrix = [['a', 'b'],
                [1, 2, 3],
                [True]]
print(mixed_matrix)        # [['a', 'b'], [1, 2, 3], [True]]
print(type(matrix))        # <class 'list'>

### Read Access Lists ###

lst = ['a', 'b', 'c', 'd']
print(lst[0])    # 'a'
print(lst[-1])   # 'd'
print(lst[-2])   # 'c'

matrix1 =[['a', 'b', 'c'],  # row 0
         ['d', 'e', 'f'],   # row 1
         ['g', 'h', 'i']]   # row 2
print(matrix1)
print(matrix1[2])           # ['g', 'h', 'i']]
print(matrix1[-1])          # ['g', 'h', 'i']] 
print(matrix1[-1][2])       # i
print(matrix1[0][0])        # a
print(matrix1[1][1])        # e

### Slicing ###
#multipe items

letters = ['a', 'b', 'c', 'd']
print(letters[:])            # default start 0 : default end -1 =(whole list)
print(matrix1[:2])           # default start 0 : end index 2 (rows)end =(row0 + row1) 
print(matrix1[1:])           # start index 1 : default end =(row1 + row2)
print(matrix1[2][:2])        # row 2, default start : end index 2 = ['g', 'h']

### Unpacking

person = ['Maria', 29,'Data Engineed', 'Berlin']
# name = person[0]
# age = person[1]
# role = person[2]
# country = person[4]
# or unpacking
#name, age, role, country = person    # Atomatic assigns index in the order given
#print(name) 
#print(role)

# Asterisk                            # groups items together
#name, *details, country = person      # 1st item, details, last item 
# print(name)                           # Maria
# print(details)                        # [29, 'Data Engineed']
# print(country)                        # Berlin
#name, *details = person               # 1st item, details everything else
# print(name)                           # Maria
# print(details)                        # [29, 'Data Engineed', 'Berlin']
#*detail, country = person             # details everything except country

# Rules unpacking
numbers = [1,2,3,4]                   # 4 values
first, second, third, last = numbers  # must be same amount variables as values 
first, *digits, last = numbers        # only 1 *
print(digits)                         # [2, 3]
string = "Python" 
first, next, *letters, sec_last, last = string
print(next)                           # y
print(letters)                        # ['t', 'h']
print(sec_last)                       # o

# unpacking_      _ommits item from list
name, _, role, _ = person    # Atomatic assigns index in the order given
print(name)
#print(age)
print(role)
#print(country)

#long_list[30,40,46,48,50,56,59,60,61,64,70,80,90,93,95]
#      first, _, _, _, _, _, _, _, _ etc.         _,last
#      first, *_, last   
 
### explore + analyze ###

#Functions#  max() min() sum() len()   = analyze
#Functions#   all()  any()             = completeness + existence check
# Methods #  count('A')  index('A')    = search + count
#Operators#    in   is                 = membership + identity
#Operators#    ==   >   <  !=          = comparison

### functions ###

numbers = [1,5,5,3,4,]
print("max:", max(numbers))       # max: 5
print("min:", min(numbers))       # min: 1
print("sum:", sum(numbers))       # sum: 15
print("length:", len(numbers))    # length: 5

print("all:", all(numbers))       # all: True
print("all:", all([1,0,9]))       # all: False  (remember 0 is not a number)
print("all:", all(["a", "", "B"]))# all: False  ( 0 and "" are empty so None False)

print("any:", any(numbers))       # any: True
print("any:", any([1,0,9]))       # any: True
print("any:", any([0,0,0]))       # any: False

print("count:", numbers.count(5)) # count: 2    counts 2 5s
print("index:", numbers.index(5)) # index: 1    sees only first 5 at pos 2 

print(4 in numbers)               # True
print(8 in numbers)               # False
print(8 not in numbers)           # True

list1 = [1,2,3]
list2 = [1,2,3]
list3 = [5,2,3]
print(list1 == list2)             # True
print(list1 < list3)              # True
print(list1 is list2)             # False 2 diffrent list same values

### Changing Lists ###
# New  Remove  Update

# New .append(value) add to end .insert(index, value) 

letts1 = ['a','b','c']
letts1.append('x')                 # ['a', 'b', 'c', 'x']
letts1.append('y')                 # ['a', 'b', 'c', 'x', 'y']
letts1.insert(0, 'x')              # ['x', 'a', 'b', 'c', 'x', 'y']
letts1.insert(1, 'f')              # ['x', 'f', 'a', 'b', 'c', 'x', 'y']
letts1.insert(4, 'd')              # ['x', 'f', 'a', 'b', 'd', 'c', 'x', 'y']
print(letts1) 

matrix2 =[['a', 'b', 'c'],  # nest array 0
         ['d', 'e', 'f'],   # nest array 1
         ['g', 'h', 'i']]   # nest array 2

matrix2.append(['x', 'y', 'z'])  # [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['x', 'y', 'z']]
matrix2.insert(1, [1,2,3,])      # [['a', 'b', 'c'], [1, 2, 3], ['d', 'e', 'f'], ['g', 'h', 'i'], ['x', 'y', 'z']]
matrix2.append('x')              # .....['x', 'y', 'z'], 'x'] added to parent not child (nested array)
matrix2[1].append('x')           # [['a', 'b', 'c'], [1, 2, 3, 'x'], ['d', 'e', 'f'].......
matrix2[0].insert(0, 'x')        # [['x', 'a', 'b', 'c'], [1, 2, 3, 'x'],.....
print(matrix2)  

# Remove .clear() .remove(value)removes first match .pop()removes by index defalt -1

#letts1.clear()              # []
letts1.remove('x')           # ['f', 'a', 'b', 'd', 'c', 'x', 'y'] Only first x removed
letts1.remove('x')           # ['f', 'a', 'b', 'd', 'c', 'y'] 2 times to remove 2 x
#letts1.pop()                 # ['f', 'a', 'b', 'd', 'c']  default last item
#removed = letts1.pop()       # ['f', 'a', 'b', 'd'] \n Removed Items: c
#removed = letts1.pop(1)      # ['f', 'b', 'd'] \n Removed Items: a
print(letts1)
#print('Removed Items:', removed)

matrix2.remove(['x', 'a', 'b', 'c']) # [[1, 2, 3, 'x'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['x', 'y', 'z'], 'x']
matrix2.pop()                        # [[1, 2, 3, 'x'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['x', 'y', 'z']]
matrix2.pop()                        # [[1, 2, 3, 'x'], ['d', 'e', 'f'], ['g', 'h', 'i']]
#matrix2.remove('e')                 # ValueError
matrix2[1].remove('e')               # [[1, 2, 3, 'x'], ['d', 'f'], ['g', 'h', 'i']]
matrix2[-1].pop(0)                   # [[1, 2, 3, 'x'], ['d', 'f'], ['h', 'i']] 
matrix2[0].pop()                     # [[1, 2, 3], ['d', 'f'], ['h', 'i']]
print(matrix2)

# Update 

lett2 = ['a', 'b', 'c']
lett2[0] = 'x' 
lett2[1] = 'y'
print(type(lett2))
print(lett2)

matrix2[-1] = ['x', 'y', 'z']
matrix2[0][0] = '-'
matrix2[1][1] = '-'
matrix2[-1][-1] = '-'
print(matrix2)

### Sorting Lists ###
# using Method

lett3 = ['c', 'a', 'd', 'b']      # ['c', 'a', 'd', 'b']
lett3.sort()                      # ['a', 'b', 'c', 'd']
lett3.sort(reverse = True)        # ['d', 'c', 'b', 'a']
print(lett3)
nested_lists = [['d', 'e', 'f'], ['g', 'h', 'i'], ['a', 'b', 'c']]
nested_lists.sort() #sort by 1st item in nest  # [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']] 
nested_lists2 = [['d', 'e', 'f'], ['a', 'z', 'i'], ['a', 'a', 'c']]
nested_lists2.sort() #sort by 2nd if 1st same  # [['a', 'a', 'c'], ['a', 'z', 'i'], ['d', 'e', 'f']]
nested_lists2[1].sort() #sort by index of nest # [['a', 'a', 'c'], ['a', 'i', 'z'], ['d', 'e', 'f']]
print(nested_lists2)

# sort copy keep og  
# using FUNCTION
print(lett3)                                # ['d', 'c', 'b', 'a']
copy_lett3 = sorted(lett3)                  # ['a', 'b', 'c', 'd']
copy_lett3 = sorted(lett3, reverse = True)  # ['d', 'c', 'b', 'a']
print(copy_lett3)

# Reverse List
# using METHOD
lett4 = ['c', 'a', 'b']
lett4.reverse()                    # ['b', 'a', 'c']
print(lett4)
# using FUNCTION and new copy
copy_lett4 = list(reversed(lett4)) # ['b', 'a', 'c']
print(copy_lett4)

### Copy List ###

# Assignement                       # Not a Copy
original = ['a', 'b', 'c']
og_shortcut = original              # NOT A COPY 
og_shortcut.append('z')
print('original:', original)        # original: ['a', 'b', 'c', 'z']
print('OG shortcut:', og_shortcut)  # OG shortcut: ['a', 'b', 'c', 'z']

# Shallow Copy  only copies top level uses same child class  
og_copy = original.copy()
og_copy.append('!')  
original.pop()          # ['a', 'b', 'c', 'z', '!']
print(original)                # ['a', 'b', 'c', 'z']
print(og_copy)

# Deep Copy   true independent copy
# import module
import copy  
nested_lists2.pop()
nested_lists2_copy = nested_lists2.copy()      # [['a', 'a', 'c'], ['a', 'i', 'z']]
nested_lists2.pop()                            # [['a', 'a', 'c']
nested_lists2_copy[0].append('z')              # [['a', 'a', 'c', 'z'], ['a', 'i', 'z']]
    # shallow copy z appears also in OG list   # [['a', 'a', 'c', 'z']
nested_lists2_copy_a = copy.deepcopy(nested_lists2)
nested_lists2_copy_a[0].pop()
nested_lists2_copy_a[0].append('x')            # [['a', 'a', 'c', 'x']]
    # deep copy x only appears in copy_a
print(nested_lists2)
print(nested_lists2_copy)
print(nested_lists2_copy_a)

# is operator Test
print(og_shortcut is original)     # True  assignements
print(og_copy is original)         # False shallow copy
print(original[0] is og_copy[0])   # True  shallow same child [0]
print(nested_lists2 is nested_lists2)
print(nested_lists2 is nested_lists2_copy_a)

### Combine Lists ###

letts5 = ['a', 'b', 'c']
numbs5 = [1, 2, 3]
#comb = letts5 + numbs5                  # ['a', 'b', 'c', 1, 2, 3] letts5 first
#comb = [letts5, numbs5]                 # [['a', 'b', 'c'], [1, 2, 3]]
#numbs5.extend(letts5)                   # [1, 2, 3, 'a', 'b', 'c']
#comb = zip(letts5, numbs5)              # <zip object at 0x10096f840>
#comb = list(zip(letts5, numbs5))        # [('a', 1), ('b', 2), ('c', 3)]
comb = list(zip(letts5, numbs5, "Hi"))  # [('a', 1, 'H'), ('b', 2, 'i')] stops at shortage 
print(comb)
print(numbs5)
ids = [101, 102, 103]
names = ['ali', 'Sara', 'john']
print(list(zip(ids, names)))          # [(101, 'ali'), (102, 'Sara'), (103, 'john')]

### Iterate ###
###############. iterable => object (lists)  iterator  => process
#  Loop #  Save memory #  Speeed

new_letters = ['a', 'b', 'c']
new_list = []                  # creat new list append new letters    
for l in new_letters:          # for loop
    #print(l.upper())          # A B C each on new line, new letter each loop
    new_list.append(l.upper()) # ['A']  ['A', 'B']  ['A', 'B', 'C'] each [] new line, adds a letter each loop
    print(new_list)       

# Enumerate
print(enumerate(new_letters))                   # <enumerate object at 0x100bd6250>
print(list(enumerate(new_letters)))             # [(0, 'a'), (1, 'b'), (2, 'c')]
print(list(enumerate(new_letters, start = 1)))  # [(1, 'a'), (2, 'b'), (3, 'c')]
for index, value in enumerate(new_letters):
    print(index, value)                         # 0 a   1 b   2 c    each on new line
example = ['a', '', 'c']
for index, value in enumerate(example):         # loop each line easy to see missing data
    print(index, value)                         # 0 a   1     2 c    each on new line

# reversed
print(reversed(new_letters))         # <list_reverseiterator object at 0x1045a5630>
print(list(reversed(new_letters)))   # ['c', 'b', 'a'] one line no loop
for l in reversed(new_letters):
    print(l)                         # c   b   a   new line loop

# Zip
new_numbers = [1, 2, 3]    
print(zip(new_letters, new_numbers))      # <zip object at 0x102d62e80>
print(list(zip(new_letters, new_numbers)))# [('a', 1), ('b', 2), ('c', 3)]
for l, n in zip(new_letters, new_numbers):
    print(l, n)                           # a 1   b 2   c 3   each on new line

# iterator map
print(map(str.upper, new_letters))      # <map object at 0x104bfeec0>
print(list(map(str.upper, new_letters)))# ['A', 'B', 'C']
new_numbs2 = ['1', '2', '3']            # str
print(list(map(int, new_numbs2)))       # [1, 2, 3]
names = ['  Maria', 'John ', ' Kumar']
print(list(map(str.strip, names)))      # ['Maria', 'John', 'Kumar']
for n in map(str.strip, names):
    print(n)                            # Maria   John   Kumar  each new line

# Filter iterator
new_letts1 = ['a', '', 'b', None, 'c', False]
print(list(filter(None, new_letts1)))    # ['a', 'b', 'c']  filter none = falsey empty etc
print(list(filter(bool, new_letts1)))    # ['a', 'b', 'c']  filter bool = falsey empty etc
items = ['sql', '123', 'python', '42']
print(list(filter(str.isalpha, items)))  # ['sql', 'python']
for i in filter(str.isalpha, items):
    print(i)                             # sql   python   each on new line

### Lambda ###

multiple = lambda x: x*2 
print(multiple(2))               # 4
add = lambda x, y: x + y
print(add(1, 2))                 # 3
check = lambda i: i in "python"
print(check('n'))                # True
print(check ('e'))               # False

# Lambda Map
prices = ['$12.50', '$9.99', '$100.00']
# experimenting
p = '$12.50'
print(p)                                                       # $12.50
print(p.replace('$', ''))                                      # 12.50
print(float(p.replace('$', '')))                               # 12.5
print(type(float(p.replace('$', ''))))                         # <class 'float'>
# implement 
print(list(map(lambda p: float(p.replace ('$', '')), prices))) # [12.5, 9.99, 100.0]

# Lambda Filter
prices2 = [120, 30, 300, 80]
print(list(filter(lambda p: p >= 100, prices2)))    # [120, 300] filters out low prices
students = [['Maria', 85],
            ['kumar', 90],
            ['Max', 60]]
# experiment
print(students[0][1] > 70)                              # True
print(students[1][1] > 70)                              # True
print(students[2][1] > 70)                              # False
# implement
print(list(filter(lambda row: row[1] > 70, students)))  # [['Maria', 85], ['kumar', 90]]

# task  Keep only students with names starting with M
#print(students[2][0].startswith('M'))                  Max True logic works
print(list(filter(lambda row: row[0].startswith("M"), students))) # [['Maria', 85], ['Max', 60]]


### List Comprehensions ###
# combines 3 steps in one line
# 1 Data Tranformation  # 2 Loop  # 3 Filter


domains = ['www.google.com',
           'openai.com',
           'localhost',
           'WWW.DATAWITHBARAA.COM']

cleaned = [
    # Data Transformation
    d.lower().replace('www.', '')         # transformer lower case delete www
    # loop
    for d in domains                      # for loop without :
    # data filtering
    if '.' in d                           # filter out domains without a dot
]
# cleaned = [ d.lower().replace('www.', '') for d in domains if '.' in d] # same as above

# cleaned2 = [
#     # Data Transformation
#     d                                      # transformer empty but must put something
#     # loop
#     for d in domains                       # for loop
#     # data filtering
#     if '.' in d                            # still filter out domains without a dot
# ]
cleaned2 = [d for d in domains if '.' in d]  # same but as smaller prefer one line
print(cleaned)
print(cleaned2)