list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter out even numbers
a = lambda x: x%2 != 0

print(
    list(
        filter(a, list1)
    )
)

square = lambda x: x ** 2
print(
    list(map(square, list1))
)