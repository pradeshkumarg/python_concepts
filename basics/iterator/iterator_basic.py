fruits = ["apple", "orange", "banana"]

i = fruits.__iter__() # or iter(fruits)

print(next(i)) # or i.__next__()
print(i.__next__())
print(i.__next__())