### Functions ###

# Functions can be passed as arguments
def my_func(func):
    print('This is the first function')
    func()
 
def another_func():
    print('This is another function')
 
my_func(another_func)

# Functions can be returned from another function and stored in variables
def multiply_by_n(multiplier):
    def multiply(number):
        print(multiplier * number) 
    return multiply
 
multiply_by_two = multiply_by_n(2)
multiply_by_three = multiply_by_n(3)
 
multiply_by_two(4)
multiply_by_three(4)

# Functions can be passed as arguments
def my_func(func):
    print('This is the first function')
    func()

def another_func():
    print('This is another function')

my_func(another_func)

# Functions can be returned from another function and stored in variables
def multiply_by_n(multiplier):
    def multiply(number):
        print(multiplier * number) 
    return multiply

multiply_by_two = multiply_by_n(2)
multiply_by_three = multiply_by_n(3)

multiply_by_two(4)
multiply_by_three(4)
print()

# Assigning a lambda function to a variable
square = lambda x: x * x
print(square(5))  # Output: 25
print()

# Refactor our multiply_by_n example
def multiply_by_n_lambda(multiplier):
    return lambda number: print(multiplier * number)

multiply_by_five = multiply_by_n(5)
multiply_by_six = multiply_by_n(6)

multiply_by_five(4)
multiply_by_six(4)

### Exercise ###

def sum_list(numbers):
    sum = 0
    for num in numbers:
        sum += num
    return sum
        
# print(sum_list((1,2,3,4,5)))

def repeat_greeting(name, times):
    for x in range(times):
        print(f"Hello {name}")

# repeat_greeting("Karl", 5)

def factorial(n):
    result = 1
    while (n > 1):
        result *= n
        n -= 1
    return result

factorial(5)

def fibonacci(n): 
    sequence = [0,1]
    if n <= 2:
        return sequence
    
    for x in range(2, n):
        sequence.append(sequence[x-1] + sequence[x-2])
    return sequence
        
# print(fibonacci(10)) 
# print(fibonacci(3)) 

def fibonacci2(n):
    sequence = []
    a, b = 0, 1
    while len(sequence) < n:
        sequence.append(a)
        a, b = b, a + b
    return sequence

# print(fibonacci2(10))

def max_of_two(a,b):
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return "both are the same"
    
# print(max_of_two(4,5))
# print(max_of_two(6,5))
# print(max_of_two(6,6))

def print_triangle(row):
    for x in range(1, row +1):
        print("*" * x)
        
# print_triangle(10)

def print_triangleB(row):
    for x in range(1, row +1):
        for y in range(x): 
            print("*", end="")
        print("")

print_triangleB(3)

