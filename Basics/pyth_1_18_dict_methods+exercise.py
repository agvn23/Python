### Methods ###

# Create an initial dictionary
d = {"name": "Alice", "age": 30, "city": "New York"}
print("Initial dictionary:", d)

# clear()
temp_d = d.copy()  # Copy to preserve original for further demonstration
temp_d.clear()
print("After clear():", temp_d)

# copy()
copied_d = d.copy()
print("Copied dictionary using copy():", copied_d)

# fromkeys()
keys = ["a", "b", "c"]
new_d = dict.fromkeys(keys, 0)
print("Dictionary from keys using fromkeys():", new_d)

# get()
name_value = d.get("name")
missing_value = d.get("missing_key", "Default")
print("Value of 'name' using get():", name_value)
print("Missing key returns default using get():", missing_value)

# items()
items_list = list(d.items())
print("Items as list of tuples:", items_list)

# keys()
keys_list = list(d.keys())
print("Keys as list:", keys_list)

# pop()
age = d.pop("age")
print("Popped 'age':", age)
print("Dictionary after pop():", d)

# popitem()
last_item = d.popitem()
print("Popped last item using popitem():", last_item)
print("Dictionary after popitem():", d)

# setdefault()
# Reset dictionary for further demonstration
d = {"name": "Alice", "age": 30}
age_value = d.setdefault("age", 40)  # 'age' key exists, so returns existing value
country_value = d.setdefault("country", "USA")  # 'country' key doesn't exist, so sets and returns "USA"
print("setdefault existing key 'age':", age_value)
print("setdefault new key 'country':", country_value)
print("Dictionary after setdefault():", d)

# update()
d.update({"city": "Boston", "occupation": "Engineer"})
print("After update():", d)

# values()
values_list = list(d.values())
print("Values as list:", values_list)

### Exercise ###

# 1. Create and Print a Dictionary
user_dict ={
    "name" : "james",
    "age" : 38,
    "city" : "london"
    }
print(user_dict)

#2. Access Dictionary Elements
print(user_dict["name"])
print(user_dict.get("email", "not found"))
print(user_dict.keys())
print(user_dict.values())
print(user_dict.items())


# 3. Check for Key Existence
if "age" in user_dict:
    print("age is in dictionary")
if "nonexsitent item" in user_dict:
    print("is not in the")    


# 4. Change and Update Dictionary Elements
user_dict.update({"occupation": "engineer"})
print(user_dict)

# 5. Add New Items to the Dictionary
user_dict["country"] = "UK"
print(user_dict)
user_dict.update({"hobby" : "running"})
print(user_dict)

# 6. Remove Items from the Dictionary
removed_age = user_dict.pop("age", None)
print(removed_age)
print(user_dict)

if "age" not in user_dict:
    print("age is not in the directory") 

# 7. Copy a Dictionary
copy_user_dict_method = user_dict.copy()
print(copy_user_dict_method)
copy_user_constructure = dict(user_dict)
print(copy_user_constructure)

user_dict["yearborn"] = "1999"
print(user_dict)
print(copy_user_constructure)
print(copy_user_dict_method)

# 8. Using setdefault()
real_hobby = user_dict.setdefault("hobby")
print(real_hobby)
football_team = user_dict.setdefault("football", "celtic")
print(football_team)
print(user_dict)

