# Sorting Lists with Custom Keys
students = [('Alice', 90), ('Bob', 85), ('Charlie', 92)]
print(
    sorted(students, key=lambda x: x[1])
)

# Using Lambda Functions with functools.reduce()
from functools import reduce
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x,y : x*y, numbers)
print(
    product
)

# Creating Small, One-Time-Use Functions
max_value = (lambda x, y: x if x > y else y)(5, 7)
print(max_value)

# Implementing Simple Event Handlers
# import tkinter as tk
# def on_click():
#     print("Button clicked!")
#
# root = tk.Tk()
# button = tk.Button(root, text="Click me!", command=lambda: on_click())
# button.pack()
# root.mainloop()


import requests
from concurrent.futures import ThreadPoolExecutor

urls = ["https://www.example.com", "https://www.example.org", "https://www.example.net"]
results = []

with ThreadPoolExecutor() as executor:
    futures = [executor.submit(lambda url: requests.get(url), url) for url in urls]

    for future in futures:
        results.append(future.result())

import json
for result in results:
    print(result.url, result.headers ,result.status_code, sep="\n")