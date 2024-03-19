import multiprocessing
import time


def square(n):
    return n ** 2


def sum_of_squares(start, end):
    return sum(square(num) for num in range(start, end))


if __name__ == '__main__':
    start_time = time.time()
    serial_result = sum_of_squares(0, 10000000)
    serial_time = (time.time() - start_time) * 1000

    start_time = time.time()
    with multiprocessing.Pool() as pool:
        parallel_result = sum(pool.map(square, range(10000000)))
    parallel_time = (time.time() - start_time) * 1000

    print(f"Serial processing time: {serial_time} ms")
    print(f"Parallel processing time: {parallel_time} ms")
