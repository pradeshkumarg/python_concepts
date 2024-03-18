import multiprocessing


def cal_square(nums, q):
    for n in nums:
        q.put(n ** 2)


if __name__ == '__main__':
    numbers = [2, 3, 4, 5]

    q = multiprocessing.Queue()

    p = multiprocessing.Process(target=cal_square, args=(numbers, q))

    p.start()
    p.join()

    while not q.empty():
        print(q.get())
