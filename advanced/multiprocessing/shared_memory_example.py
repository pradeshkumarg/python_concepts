import multiprocessing


def cal_square(nums, res, v):
    v.value = 3.14
    for idx, item in enumerate(nums):
        res[idx] = item ** 2


if __name__ == '__main__':
    numbers = [2, 3, 4, 5]
    result = multiprocessing.Array('i', 4)  # datatype, size
    v = multiprocessing.Value('d')  # double

    p = multiprocessing.Process(target=cal_square, args=(numbers, result, v))

    p.start()
    p.join()

    print(result[:])

    print(v)
