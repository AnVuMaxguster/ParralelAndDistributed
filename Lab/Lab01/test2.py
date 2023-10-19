import multiprocessing
import time

# Function that sleeps for a+b seconds
def simple_cal(n):
    time.sleep(n)
    print(f"Done sleeping for {n}")

def main():
    pool = multiprocessing.Pool()

    # List of arguments (a, b) for each worker
    sec = [1, 2, 3, 4, 5]

    start = time.perf_counter()

    for n in sec:
        pool.apply_async(simple_cal, args=[n])

    pool.close()
    pool.join()
    pool.map(simple_cal, sec)
    pool.close()
    end = time.perf_counter()

    print(f"Finished in: {end - start}")

if __name__ == "__main__":
    main()