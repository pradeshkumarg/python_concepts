import threading
import time

from advanced.decorators.decorators import time_it


def worker(num):
    print(f"Worker {num} started")
    time.sleep(1)  # Simulating some work
    print(f"Worker {num} finished")


if __name__ == "__main__":
    @time_it
    def threadHandling():
        # Create and start threads
        threads = []
        for i in range(5):
            thread = threading.Thread(target=worker, args=(i,))
            threads.append(thread)
            thread.start()

        # Wait for all threads to complete
        for thread in threads:
            thread.join()

        print("All workers have finished their tasks.")


    threadHandling()
