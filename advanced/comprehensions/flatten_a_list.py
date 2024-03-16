chunks = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]

result = [item for chunk in chunks for item in chunk]

print(result)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
