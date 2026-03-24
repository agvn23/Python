### Try-Except Blocks ###

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
# print(combined_args(1, 2 , 3, 4)) #Raises an error because d is keyword only

### Lambda ###

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