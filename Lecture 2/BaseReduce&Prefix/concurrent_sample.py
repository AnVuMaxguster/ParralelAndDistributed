import concurrent.futures
import time

def do_something(sec):
    print(f"Sleeping for {sec} second...")
    time.sleep(sec)
    return "Done sleeping..."

def main():
    start = time.perf_counter()
    #--------------- Main work ---------------
    with concurrent.futures.ProcessPoolExecutor() as executor:
        # for _ in range(10):
        #     f = executor.submit(do_something, 1)

        results = [executor.submit(do_something, 1) for _ in range(10)] # List Comprehension: create a new list based on the values of an existing list.

        for f in concurrent.futures.as_completed(results):  
            print(f.result())                               # f.result(): return the return value of target function.
    #--------------- Main work ---------------
    end = time.perf_counter()
    print(f"Execution time: {end-start:.2f} second(s)")

if __name__ == "__main__":
    main()

