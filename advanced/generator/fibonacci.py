"""
Generators -> analogous to Streams in Java
Advantage of using Generators
1. Need not use iter() and next() methods
2. Need not raise StopIteration exeption
"""


def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


for i in fib():
    if i > 50:
        break
    print(i)
