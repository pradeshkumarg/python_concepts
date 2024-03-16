import time


def cal_square(numbers):
    start = time.time()
    result = [i * i for i in numbers]
    end = time.time()
    print(f"cal_square took {(end - start) * 1000} ms")
    return result


def cal_cube(numbers):
    start = time.time()
    result = [i ** 3 for i in numbers]
    end = time.time()
    print(f"cal_cube took {(end - start) * 1000} ms")
    return result


# with decorator
def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {(end - start) * 1000} ms")
        return result

    return wrapper


@time_it
def cal_power_of_4(nums):
    result = [i ** 4 for i in nums]
    return result


if __name__ == "__main__":
    """
        without decorator - time calculation is a side-effect // analogous to an annotation in Java
    """
    numbers = range(1, 100000)
    output_square = cal_square(numbers)
    output_cube = cal_cube(numbers)

    r = cal_power_of_4(numbers)
