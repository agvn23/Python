### Valid Parentheses ###

# You have a string s composed only of the 
# characters (, ), {, }, [ and ]. 
# Determine if the bracket arrangement in this string is valid. 
# Specifically, a valid string must meet the following criteria:

# Each opening bracket has a corresponding closing bracket 
# of the same type.
# Brackets are closed in the correct order.
# Every closing bracket matches an earlier opening bracket 
# of the same type.

# Examples
#s = "()"    # output: True
# input s = "(])"
# input s = "]()"
# input s = "()[]{}" output: True
# input s = "(]"     output: False
# input s = "([])".  output: True

#mapping={
#         ")":"(",
#         "]":"[",
#         "}":"{" 
#        }                    
# create dict key:value     
#def is_valid(s):
# creat stack (empty list)
#    stack = []
# take first item from input + check if in dict if not goes in stack
#     for i in range(len(s)):
#         #new = s[i][0]
#         #if i not in mapping:
#         for j in range(len(mapping)):
#             if i != j:
#                 return False
#             top = stack.pop()
#             if mapping != top:
#                 return False
#             else:
#                 stack.append(i)
#         if stack:
#             return False
#         else:
#             return True
        
# print(is_valid(s))        

# Anoj Solution

def is_valid(s):
    stack = []                                   # create empty stack/list
    mapping = {")":"(", "]":"[", "}":"{"}        # create dict

    for char in s:                               # take item to compare
        if char in mapping:                          # compare with dict keys
            #if stack:                                    # if in stack   
            #    top = stack.pop()                            # if True remove from stack pop(default -1)         
            #else:                                        # if empty
            #    top = "#"                                    # 
            top = stack.pop() if stack else None # do stack.pop if stack exists
            
            if mapping[char] != top:                  # if dict key and != 
                return False                              # false

        else:
            stack:append(char)                   # if not dict key add to stack

    return True        


# ex1 takes ( not in dict goes in stack
#     take next ) in dict  check last stack input ( 
#     if dict key = dict value = True remove ( from stack
#     and continue 
#ex2 ( not dict goes stack
#     ] in dict == last stack ( = False
#     
# Test cases
print(is_valid("()"))       # True
print(is_valid("()[]{}"))   # True
print(is_valid("(]"))
print(is_valid("([)]"))
print(is_valid("()"))
print(is_valid(")"))  # False
print(is_valid("()"))  # True
print(is_valid("()[]{}"))  # True
print(is_valid("(]"))  # False
print(is_valid("([)]"))  # False
print(is_valid("{[]}"))  # True

#solution 2

# class Solution:
#     def is_valid_2(self, s: str) -> bool:
#         close_to_open = {
#             ")":"(",
#             "]":"[",
#             "}":"{" 
#         }
#         stack = []

#         for bracket in s:
#             if bracket in close_to_open:
#                 if not stack:
#                     return False
#                 top = stack.pop() 
#                 if close_to_open[brackt] != top:
#                     return False
#             else:
#                 stack.append(bracket)   

#         if stack:
#             return False
#         else:
#             return True