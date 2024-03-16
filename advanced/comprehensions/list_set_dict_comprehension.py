numbers = list(range(1, 8))

print(numbers)

# get only even numbers
even = [i for i in numbers if i % 2 == 0]
print(even)

squares = [i ** 2 for i in numbers]
print(squares)

s = {1, 2, 3, 4, 5, 5, 4, 3, 2}
print(s)

even = {i for i in s if i % 2 == 0}
print(even)

cities = ["mumbai", "new york", "paris"]
countries = ["india", "usa", "france"]
z = zip(cities, countries)
print(z)

print(c for c in z)

d = {city: country for city, country in z}
print(d)
