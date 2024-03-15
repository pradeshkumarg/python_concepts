set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

union = set1.union(set2)
intersection = set1.intersection(set2)

diff1 = set1.difference(set2)
diff2 = set2.difference(set1)

sd = set1.symmetric_difference(set2)

print("Ans: ", set1, set2, union, intersection, diff1, diff2, sd, sep="\n")

union = set1|set2
intersection = set1&set2

diff1 = set1 - set2
diff2 = set2 - set1

sd = set1 ^ set2

print("Ans: ", set1, set2, union, intersection, diff1, diff2, sd, sep="\n")

# Update with union
set1.update(set2)
print(set1)  # Output: {1, 2, 3, 4, 5}

set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1.intersection_update(set2)
print(set1)  # Output: {3}

set1 = {1, 2, 3}
set1.difference_update(set2)
print(set1)  # Output: {1, 2}

# set membership and iteration
numbers = {1, 2, 3, 4, 5}
# Membership test
print(3 in numbers)  # Output: True
print(6 not in numbers)  # Output: True

# Iteration
for num in numbers:
    print(num)