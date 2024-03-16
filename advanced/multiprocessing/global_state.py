from multiprocessing import Process

results = []


def cal_square(numbers):
    # global squares
    results = []
    for i in numbers:
        results.append(i ** 2)
    return results


def cal_square1(numbers):
    global results
    for i in numbers:
        results.append(i ** 2)
    return results


if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]
    print(results)
    print(cal_square(numbers))
    # print(cal_square1(numbers))
    # print(results)

    p1 = Process(target=cal_square1, args=(numbers,))
    p1.start()
    p1.join()

    """
    since it's executed by a different process, it has it's own memory and it doesn't update
    the variable of the parent process.
    
    Hence the global results would be [] 
    """
    print(results)