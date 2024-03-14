total = 0
def sum(a, b):
    total = a+b
    print("Total inside the function is ", total)
    return total


print("Sum of 2 and 4 is", sum(2, 4))
print("Sum of 4 and 2 is", sum(b=2, a=4))

print("Total outside the function is ", total)