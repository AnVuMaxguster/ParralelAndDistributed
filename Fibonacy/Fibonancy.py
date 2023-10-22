import multiprocessing
import time

def calculate_fibonacci(n):
    a, b = 0, 1
    for i in range(2, n):
        a, b = b, a + b
    return b

def main():
    n = 10
    num_processes = 12 
    with multiprocessing.Pool(processes=num_processes) as pool:
        results = list(pool.map(calculate_fibonacci, range(2, n)))
    print("Fibonacci sequence:")
    for i, result in enumerate(results):
        print(f"Fibonacci({i + 2}) = {result}")

if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    ex_time = end_time - start_time
    print(ex_time)

