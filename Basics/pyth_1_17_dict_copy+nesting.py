### Copying ###

# Original dictionary
original_dict = {
    "name": "Alice",
    "age": 30,
    "hobbies": ["reading", "cycling"]
}

print("Original dictionary:", original_dict)

# 1. Copying using copy() method
copy_dict_method = original_dict.copy()
print("\nCopied dictionary using copy():", copy_dict_method)

# 2. Copying using dict() constructor
copy_dict_constructor = dict(original_dict)
print("Copied dictionary using dict():", copy_dict_constructor)

# Verify that they are separate objects
print("\nAre original and copy_dict_method the same object?", original_dict is copy_dict_method)
print("Are original and copy_dict_constructor the same object?", original_dict is copy_dict_constructor)

# Modify original at top level
original_dict["age"] = 31
print("\nAfter modifying original_dict['age'] to 31:")
print("Original dictionary:", original_dict)
print("copy_dict_method:", copy_dict_method)
print("copy_dict_constructor:", copy_dict_constructor)

# Modify a mutable value inside the dictionary (list under "hobbies")
original_dict["hobbies"].append("painting")
print("\nAfter appending 'painting' to original_dict['hobbies']:")
print("Original dictionary:", original_dict)
print("copy_dict_method:", copy_dict_method)
print("copy_dict_constructor:", copy_dict_constructor)

# Observations:
# - The 'age' change only affected the original dictionary because it's a top-level change.
# - The change in 'hobbies' is reflected in the copies as well because
#   they share references to the same mutable list (shallow copy behavior).

### Nesting ###

# Creating a nested dictionary
person = {
    "name": "Alice",
    "age": 30,
    "address": {
        "street": "123 Maple Street",
        "city": "New York",
        "zipcode": "10001",
        "coordinates": {
            "latitude": 40.7128,
            "longitude": -74.0060
        }
    },
    "occupation": "Engineer"
}

# Accessing top-level elements
print("Name:", person["name"])
print("Age:", person["age"])

# Accessing nested dictionary elements
address = person["address"]
print("\nAddress:", address)

city = person["address"]["city"]
print("City:", city)

zipcode = person["address"]["zipcode"]
print("Zipcode:", zipcode)

# Accessing deeper nested elements
latitude = person["address"]["coordinates"]["latitude"]
longitude = person["address"]["coordinates"]["longitude"]
print("Coordinates:", latitude, longitude)

# Using get() to safely access nested values
# This example tries to access a non-existent key with a default value
country = person.get("address", {}).get("country", "Country not specified")
print("Country:", country)

# Using get() for deep nested retrieval with potential missing keys
# Notice we use cascading get() calls, each with default empty dict {}
lat_safe = person.get("address", {}).get("coordinates", {}).get("latitude", "No latitude")
print("Safe Latitude Access:", lat_safe)
