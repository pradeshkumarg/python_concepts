import multiprocessing
import time


def compute_square(nums):
    result = []
    for n in nums:
        time.sleep(0.2)  # Simulating a computationally intensive operation
        result.append(n ** 2)
    print(f"Result from process: {result}")
    return result


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Create a pool of worker processes
    pool = multiprocessing.Pool(processes=4)

    # Split the list of numbers into chunks
    chunk_size = len(numbers) // 4
    chunks = [numbers[i:i + chunk_size] for i in range(0, len(numbers), chunk_size)]

    # Apply the compute_square function to each chunk in parallel
    results = pool.map(compute_square, chunks)

    # Close the pool and wait for the tasks to finish
    pool.close()
    pool.join()

    # Flatten the results from each process
    final_result = [item for sublist in results for item in sublist]
    print(f"Final result: {final_result}")
