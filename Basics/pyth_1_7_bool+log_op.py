#-------------------CONTROL FLOW---------------------
#  Conditional Statements     |   Loops
#          |                        |
#   False --- True                  | <----    
#     |        |                    |     |
# leftblock  rightblock             |--->true
#     |        |                    |
#      ---------                  False
#          |
#      lastblaock
#                               Loop Types   Loop Control
#         if                    for          break
#         elif                  while        pass
#         else                               continue

# Boolean   True/False

# Examples of values that evaluate to True
print("Truthy Values:")
print(True)           # The value True -> True
print(bool("Hello"))  # Non-empty string -> True
print(bool(123))      # Non-zero integer -> True
print(bool(3.14))     # Non-zero float -> True
print(bool([1, 2, 3])) # Non-empty list -> True
print(bool({"a": 1}))  # Non-empty dictionary -> True

# Examples of values that evaluate to False
print("\nFalsy Values:")
print(False)          # The value False -> False
print(bool(""))       # Empty string -> False
print(bool(0))        # Zero -> False
print(bool(0.0))      # Float zero -> False
print(bool(0j))       # Complex zero -> False
print(bool([]))       # Empty list -> False
print(bool(()))       # Empty tuple -> False
print(bool({}))       # Empty dictionary -> False
print(bool(None))     # None -> False

# Truthy and Falsy check with conditionals
print("\nTruthy/Falsy Checks:")
is_list_empty = []                    # We know an emtpy list will evaluate to False
if is_list_empty:
    print("The list is not empty")
else:
    print("The list is empty")        # Empty list -> False

is_string_empty = "Python"            # We know an non-empty string will evaluate to True
if is_string_empty:
    print("The string is not empty")  # Non-empty string -> True
else:
    print("The string is empty")


### Boolean ###   True/False

print("Boolean True False:")
print(True)           # True
print(False)          # False
print(type(True))     # <class 'bool'>
print(bool(123))      # True   (value not nothing)
print(bool("Hi"))     # True     "    "    "
print(bool())         # False  (value nothing)
print(bool(0))        # False  (in boolean 0 = nothing)
print(bool(""))       # False  (in boolean empty str = nothing)
print(bool(None))     # False  (None = nothing)

# All or Any   all true = true / any true = True

email = ""
phone = "0176-123456"
username = ""
print("All or Any:")
# Allow registration if any field is filled
print(any([email, phone, username]))       # True 
# Allow reistration only if all fields filled 
print(all([email, phone, username]))       # False

# Isinstance

print("Isinstance:")
print(isinstance(123, int))                # True
print(isinstance(True, str))               # False   (bool)
print("Hello".endswith("o"))               # True
print("Hello".startswith("o"))             # False

### Arithmetic Operators ###

a = 10
b = 3
print("Arithmetic Operators:")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)

# Assignment Operators

x = 5
x += 3  # Same as x = x + 3
print("\nAssignment Operators:")
print("x after += 3:", x)

### COMPARISON OPERATORS ###

# Value > Operator > Value
# value                3 > 2 => True
# variable (x=5)       x < 2 => False
# expression      2 - 1 != 2 => True
# function    len("Hi") == 3 => False
print("Comparison Operators:")
print(10 == 10)    # True
print(10 != 10)    # False
print(7 > 3)       # True
print(7 >= 3)      # True
print(3 < 7)       # True
print(3 <= 7)      # True
print("a" > "b")   # False  (alphbetical order)
print("a" > "b")   # True
print("a" == "b")  # False
print("a" == "A")  # False  (case sensitive)
print(1 < 4 < 6)   # True   (read from left to right)
print(5 < 4 < 6)   # False  (all must be True)
# Is age between 18 and 30?
age = 20
print(18 <= age <= 30) # True

### LOGICAL OPERATORS ###  

# And / Or
# and = both true
# or = one must be true
print("Logical Operators:")
print(3 > 1 and 5 < 1)   # False
print(3 > 1 and 5 > 1)   # True
print(3 > 1 or 5 < 1)    # True
print(3 > 1 or 5 > 1)    # True
# check if system is under pressure
cpu_usage = 70
memory_usage = 95
print(cpu_usage > 90 or memory_usage > 90)  # True
cpu_usage = 70
memory_usage = 50
print(cpu_usage > 90 or memory_usage > 90)  # False
# Checking user credentials before login
email = True
password = True
print(email and password)     # True

# Not Operator

print(3 > 2)      # True
print(not 3 > 2)  # False
print(not True)   # False
print(5 == 8)     # False
print(not 5 == 8) # True

name = ""
print(not name)   # True  not  False = nothing

### CONTROL MIXED CONDITIONS ###

                 # PRIORITY
#x = 5           # AND before OR
#y = 8           # inside left over right
#z = 6
#       |1.        |2.        |3.  
#       |x == 5 or |y > 5 and |z < 4        
# 1st               8 > 5 = True
# 2nd                          6 < 4 = False  
# 3rd                       True  and  False = False
# 4th    5 == 5 = True
# 5th             True           or            False = True

# Using Parenthsis () to overrule default priority

#       (5 == 5 or 8 > 5) and 6 < 4
#1st       True
#2nd                True
#3rd           True
#4th                         False
#5th                 = False   

# Allow access only if the user is logged in 
# Or they are a guest
# but they must not be banned  #MUST USE PARENTHSIS TO GET DESIRED OUTPUT

is_logged_in = True
is_guest = False
is_banned = False

print(is_logged_in or is_guest and not is_banned)    # True
#                     False
#                                  not False = True
#                     False    and             True = False
#         True     or                                 False = True 
      
is_logged_in = True
is_guest = False
is_banned = True

print(is_logged_in or is_guest and not is_banned)    # True
#                     False
#                                  not  True = False
#                     False    and             False = False
#         True     or                                  False = True 

is_logged_in = True
is_guest = False
is_banned = True

print((is_logged_in or is_guest) and not is_banned)    # False
#       True
#                       False
#                  True
#                                          False
#                  True         and        False     = False

# Membership (in) Operator

print("\nMembership Operators:")
print("o" in "Python")       # True
print("f" in "Python")       # False
print("f" not in "Python")   # True
print(3 in [1, 2, 3])        # True

# Security check: ensure the domain is not banned
domain = "gamail.com"
banned_domains = ["spam.com", "fake.org", "bot.net"]
print(domain not in banned_domains)       # True

### Identity Operators ###
#    IS is not ==

x = ["a", "b", "c"]
y = ["a", "b", "c"]
print(x == y)      # True
print(x is y)      # False     2 lists / objects (id) with same value
x = 10
y = 10
print(x == y)      # True
print(x is y)      # True      2 variables 1 objest same id
x = ["a", "b", "c"]
y = x
print(x == y)      # True
print(x is y)      # True

# Make sure the email exists, and its not empty.
email = ""
print (email != "")         # False 
email = "g@gmail.com"
print (email != "")         # True
email = None
print (email != "")         # True       None is not == blank
email = None
print (email is not None and email != "") # False   ==None cooler is not None

# Bitwise Operators
print("\nBitwise Operators:")

# Bitwise AND: Compares each bit of two numbers. The result has a 1 in each position where both operands have 1s.
# Example: 5 -> 0101, 3 -> 0011, result -> 0001 (1 in decimal)
print("5 & 3:", 5 & 3)

# Bitwise OR: Compares each bit of two numbers. The result has a 1 in each position where at least one operand has a 1.
# Example: 5 -> 0101, 3 -> 0011, result -> 0111 (7 in decimal)
print("5 | 3:", 5 | 3)

# Bitwise XOR: Compares each bit of two numbers. The result has a 1 in each position where the bits of the operands are different.
# Example: 5 -> 0101, 3 -> 0011, result -> 0110 (6 in decimal)
print("5 ^ 3:", 5 ^ 3)

# Bitwise NOT: Inverts each bit of the number. Flips 0s to 1s and 1s to 0s.
# Example: 5 -> 0101, result -> 1010 (in 2's complement, it's -6 in decimal)
print("~5:", ~5)

# Bitwise Left Shift: Shifts the bits of the number to the left by the specified number of positions.
# Each left shift is equivalent to multiplying the number by 2.
# Example: 5 -> 0101, result after shifting 1 position -> 1010 (10 in decimal)
print("5 << 1:", 5 << 1)

# Bitwise Right Shift: Shifts the bits of the number to the right by the specified number of positions.
# Each right shift is equivalent to dividing the number by 2 (ignoring the remainder).
# Example: 5 -> 0101, result after shifting 1 position -> 0010 (2 in decimal)
print("5 >> 1:", 5 >> 1)

# Operator Precedence Example
print("\nOperator Precedence Example:")
print("3 + 5 * 2 ** 2:", 3 + 5 * 2 ** 2)  # Evaluates to 23

#   challange
#   1 check if user name is not empty and age is greater than or equal to 18

user_name = "jon"
user_age = 21
print(user_age >= 18)     # True
print(user_name is not None and user_name != "") # True
print(user_name is not None or user_name != "" and user_age >= 18) # True
#   2 check if the password is at least 8 char long and does not contain spaces
password = "sg ttrs"
print(len(password) >= 8)   # False
print(" " not in password)   # False
print(len(password) >= 8 and " " not in password)  # False
#   3 check if a users email is not empty, conatins "@" and ends with".com
email = "zu@.com"
print(email is not None or email != "" and email.endswith(".com")) # True
#   4 check if username is a string, is not None and is longer than 5 char
username = "Gavers"
print(username is not int and username is not None and len(username)>= 5)
#   5 check if the user is either an admin or a mod and either theyre not banned or theyve verified their email
user = "Dave"
admin = True
mod = False
banned_list = ["alex", "bob", "ed"]
email = True
print(user is email)
print(user is admin or mod)
print((user is admin or mod) and user is not banned_list or user is email)
#     True or False = True      
#     True and not False =>True = True 

