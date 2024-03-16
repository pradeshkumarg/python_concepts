def myfunc(n):
  return lambda a : a * n

my_doubler = myfunc(2)

my_tripler = myfunc(3)

print(my_doubler(11))

print(my_tripler(3))

