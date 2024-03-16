try:
    # check python built-in exceptions to see all the exceptions that can be raised
    raise MemoryError('memory error message')
except MemoryError as e:
    print(e)