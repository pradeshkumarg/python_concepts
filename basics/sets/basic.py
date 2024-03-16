# Creating an empty set
import json

empty_set = set()

# Creating a set from a list
fruits = set(['apple', 'banana', 'cherry', 'apple'])
print(fruits)  # Output: {'banana', 'apple', 'cherry'}

# convert a set to json
print(json.dumps(list(fruits)))