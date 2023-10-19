import multiprocessing
import time

# Function that sleeps for a+b seconds
def simple_cal(a, b):
    time.sleep(a+b)
    print(f"Sleeped for {a+b} secs")
    return a+b

def main():
    pool = multiprocessing.Pool(processes=4)

    # List of arguments (a, b) for each worker
    argument_list = [(1, 2), (3, 4), (2, 3), (4, 5)]

    results = pool.starmap(simple_cal, argument_list)

    for r in results:
        print(r)

    print("All tasks are complete")

if __name__ == "__main__":
    main()