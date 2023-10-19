import multiprocessing
import time

from time import perf_counter

def do_something(sec):
    print(f"Sleeping for {sec} second...")
    time.sleep(sec)
    return f"Done sleeping...{sec}" # Load giá trị trả về vào hàng đợi 

def main():
    list = [5,7,2,6,1,4]

    start_time = perf_counter() # Start timer
    #--------------- Main work ---------------
    print(multiprocessing.cpu_count())
    pool = multiprocessing.Pool()
    tasks = pool.map_async(do_something, list)
    results = tasks.get()
    pool.close()
    pool.join()
    for result in results:
        print(result)
    #--------------- Main work ---------------
    end_time = perf_counter()   # Stop timer                   
    print(f"Execution time: {end_time-start_time} second(s)")

if __name__ == "__main__":
    main()