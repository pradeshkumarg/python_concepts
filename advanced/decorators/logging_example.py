import logging


def log_function_call(func):
    def wrapper(*args, **kwargs):
        logging.basicConfig(level=logging.INFO)
        logging.info(f"Calling function: {func.__name__}")
        res = func(*args, **kwargs)
        logging.info(f"Function {func.__name__} returned: {res}")
        return res

    return wrapper


@log_function_call
def add_numbers(a, b):
    return a + b


result = add_numbers(2, 3)
