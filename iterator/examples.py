"""
Examples of iterator

list
tuple
set
string
dictionary
file
"""

for i in ["a", "b", "c"]:
    print(i, end=" ")
print()

for i in ("a", "b", "c"):
    print(i, end=" ")
print()

for i in {"a", "b", "c", "d", "c"}:
    print(i, end=" ")
print()

for c in "Pradesh":
    print(c, end=" ")
print()

for key in {"key1": "value1", "key2": "value2"}:
    print(key, end=" ")
print()

file = open("/tmp/test.txt", "r")
for line in file:
    print(line)
print()