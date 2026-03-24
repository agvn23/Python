### Functions ###

#efine a function that greets a user by D name
def greet(name):
    print(f"Hello, {name}! Welcome to Python functions.")

# Define a function that checks if a number is even or odd
def check_even_odd(number):
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")

# Define a function that prints numbers from 1 to n using a loop
def print_numbers(n):
    print(f"Printing numbers from 1 to {n}:")
    for i in range(1, n + 1):
        print(i, end=" ")
    print()  # For newline after the loop

# Define a function that sums a list of numbers
def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    print(f"The sum of {numbers} is {total}.")

# Using the functions defined above
greet("Alice")
check_even_odd(7)
print_numbers(5)
sum_list([1, 2, 3, 4, 5])

### Parameters and Arguments ###

def add(a, b):
    return a + b
try:
    add(1)  # Raises TypeError due to missing argument
except Exception as e:
    print(e)

def square(x): 
    return x * x
result = square(4)  # result will be 16

def greet(name, greeting): 
    print(f"{greeting}, {name}!")
greet("Reagan", "Howdy")  # Positional arguments. Prints: Howdy, Reagan! 
greet(greeting="Hi", name="Alice")  # Keyword arguments. Prints: Hi, Alice!
greet(name="Bob", greeting="Hello")  # Keyword arguments. Prints: Hello, Bob!

def greet(name, greeting="Hello"): 
    print(f"{greeting}, {name}!")
greet("Bob")  # Prints: Hello, Bob! using the default greeting
greet(name="Bob", greeting="Howdy")  # Prints: Howdy, Bob!

def collect_with_args(*my_arbitrary_args):
    print(type(my_arbitrary_args))
    print(my_arbitrary_args)

collect_with_args(1, 2, 3)  # Prints: <class 'tuple'> (1, 2, 3)

def collect_with_kwargs(**kwargs): 
    print(type(kwargs))
    print(kwargs)

collect_with_kwargs(a=1, b=2)  # Prints: <class 'dict'> {'a': 1, 'b': 2}

def only_positional(a, b, /): 
    return (a, b)
print(only_positional(1, 2))
#print(onlyPositional(a=1, b=2)) # Raises an error

def only_keyword(*, x):
  return x

print(only_keyword(x = 3))
#print(onlyKeyword(3)) # Raises an error

def combined_args(a, b, c, /, *, d): 
    return (a, b, c, d)
print(combined_args(1, 2 , 3, d=4)) 
# print(combined_args(1, 2 , 3, 4)) #Raises an error because d is keyword onl