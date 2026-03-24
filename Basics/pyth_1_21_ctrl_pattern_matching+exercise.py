### Pattern Matching ###

# Simple case
day_number = 3

match day_number:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case _:
        print("Weekend or an invalid day number")

# Using pattern matching with more complex data, for example a set of coordinates
point = (0, 0) 
#point = (1, 0)
#point = (0, 1)
#point = (1, 2)

match point:
    case (0, 0):
        print("Point is at the origin.")
    case (0, y):
        print(f"Point is on the Y-axis at y={y}.")
    case (x, 0):
        print(f"Point is on the X-axis at x={x}.")
    case (x, y):
        print(f"Point is at coordinates x={x}, y={y}.")

### Exercise ###

# 1. Basic If Condition
number = 0

if number >0:
    print(f"the number {number} is positive.")
elif number <0:
    print(f"the number {number} is negative.")
else:
    print(f"the number {number} is zero.")        

# 2. Grade Calculator
score = 59

if score >= 90:
    print(f"the score {score} is a Grade: A.")
elif score >= 80:
    print(f"the score {score} is a Grade. B.")
elif score >= 70:
    print(f"the score {score} is a Grade: C.") 
elif score >= 60:
    print(f"the score {score} is a Grade: D") 
else:
    print(f"the score {score} is a Grade: F")    

# 3. Ternary Operator Practice
age = 11
verification = "adult" if age >= 18 else "minor"
print(f"age verification: ", verification)

# 4. For Loop over a List
cars = ["BMW", "VW", "Mercedes", "Porsche"]
for items in cars:
    print(f"car company: {items}")
print()    

# 5. For Loop with Conditions
#numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
count = 0
while count < 10:
    count += 1
    if count % 2 == 1:
        continue
    print(f"even number:", count)
print("Finished skipping odd numbers.\n")

# 6. While Loop Summation
total_sum = 0 
num = 1
while num <= 100:
    total_sum += num
    num += 1
print(total_sum)    

# 7. Break out of a Loop
for digits in range(1, 11):
    if digits == 7:
        break
    else:
        print(digits)

# 8. Nested Loops
peoples = ["Alice", "Beth", "Clare", "Debbie"]
pets = ["cats", "Dogs", "Fish", "Mice"]


for people in peoples:
    for pet in pets:
        print(f"{people} and {pet}")

# 9. Loop with Else Clause
instrument = "bass"
items =["piano", "guitar", "drums"]
if instrument in items:
    print(f"{instrument} is in the list")
else:
    print(f"{instrument} is not in the list")

# 10. Pass Statement Usage
a = 33
b = 200

if b > a:
  pass

# 11. Pattern matching
fruits = ["ananas", "banana", "cherry"]
veg = ["aubergin", "beans", "cabbage"]
meats = ["beef", "chicken", "pork"]
fruits.append ("orange")
veg.append ("onions")
meats.append ("turkey")
print(fruits)

match fruits:
    case item if item in fruits:
        return f"{item} is a fruit,"
    case item if {item} in veg:
        return f"{item} is a veg."
    case item if {item} in meats:
        return f"{item} is a meat"
    case _:
        return f"{item} is anything else."
    
item = "banana"    
        
#-----------SOLUTIONS-----------

# 1. Basic If Condition
print("task 1")

num = 0
if num < 0:
    print("number is negative")
elif num == 0:
    print("number is 0")
else: 
    print("number is positive")
    
print("task 2")

# 2. Grade Calculator
score = 80

if score > 90:
    print("A")
elif score > 80:
    print("B")
elif score > 70:
    print("C")
elif score > 60:
    print("D")
elif score > 50:
    print("E")
else:
    print("F")
    
# 3. Ternary Operator Practice
print("task 3")
age = 13
status = "not defined yet"

status = "adult" if age >= 18 else "minor"
print(status)

# 4. For Loop over a List
print("task 4")
vehicles = ["bicycle", "car", "train", "plane", "ship"]

for vehicle in vehicles:
    print(f"Today I am taking the {vehicle}.")
    
# 5. For Loop with Conditions
print("task 5")
for i in range(1,11):
    if i % 2 == 0:
        print(i)
        
# 6. While Loop Summation        
start = 0
sum = 0

while start <= 100:
    sum += start
    start += 1

print(sum)

# 7. Break out of a Loop
word_list = ["car", "fish", "watch", "dinosaur", "elephant", "tower"]

index = 0
for word in word_list:
    if len(word) > 5:
        break
    index +=1
    
print(index)
print(word_list[index])

# 8. Nested Loops
print("task 8")
people = ["Hannah", "John", "Karl"]
pets = ["Lucie", "Rex", "Mr. Whiskers"]

for person in people:
    for pet in pets:
        print(f"{person} loves {pet}")
        
# 9. Loop with Else Clause
print("task 9")
for item in people:
    if item == "Jim":
        print("Hello Jim")
        break
else:
    print("Hello Guest")
    
# 10. Pass Statement Usage
print("task 10")
for item in []:
    pass

# 11. Pattern matching
print("task 11")

fruits = ["apple", "banana", "orange", "mango"]
veggies = ["carrot", "broccoli", "spinach", "pepper"]
meat = ["chicken", "beef", "pork", "lamb"]

item = "mango"

match item:
    case _ if item in fruits:
        print(f"{item.capitalize()} is a fruit")
    case _ if item in veggies:
        print(f"{item.capitalize()} is a vegetable")
    case _ if item in meat:
        print(f"{item.capitalize()} is a meat product")   
    case _:
        print(f"{item.capitalize()} does not match any known category.")