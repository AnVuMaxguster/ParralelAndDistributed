import multiprocessing
import math
from time import perf_counter

def add_leftsum(array, leftsum):
    for i in range(0,len(array)):
        array[i] +=leftsum
    return array

def chunk_split(array, n):
    for i in range(0, len(array), n):
        yield array[i:i + n]

def sub_prefix_sum(array):
    for i in range(1,len(array)):
        array[i] += array[i-1]
    return array

def parallel_prefix_sum(matrix_a):
    # chunk_size = round(math.log2(len(array)))
    chunk_size = len(matrix_a) // multiprocessing.cpu_count()

    if chunk_size < 1:
        return sub_prefix_sum(matrix_a)
    
    chunks = chunk_split(matrix_a,chunk_size)

    # Define pool of worker processes ( default quantity = no. of system CPU cores)
    pool = multiprocessing.Pool()

    # Step 1
    sub_prefix = pool.map_async(sub_prefix_sum, chunks)
    sub_prefix_array = sub_prefix.get()

    # Step 2
    sub_left_sum = []
    for a in sub_prefix_array:
        sub_left_sum.append(a[len(a)-1])
    sub_left_sum_result = pool.apply(sub_prefix_sum, args=[sub_left_sum])

    # Step 3
    final_array = sub_prefix_array[0]
    results = [pool.apply_async(add_leftsum, args=[sub_prefix_array[i+1], sub_left_sum_result[i]]) for i in range(0, len(sub_prefix_array)-1)]
    final_sub_array = [result.get() for result in results]

    for a in final_sub_array:
        for n in a:
            final_array.append(n) 

    pool.close()

    return final_array
    
def main():
    # USER INPUT
    print("Enter the starting value of the array:", end=" ")
    first = int(input())
    print("Enter the ending value of the array:", end=" ")
    last = int(input ())
    print()

    # INIT ARRAY
    # array = list(range(first,last+1))
    array = [89, 47, 63, 12, 31, 58, 5, 73, 94, 77, 38, 42, 20, 9, 65, 83, 15]


    start_time = perf_counter() # Start timer
    #--------------- Main work ---------------
    pre_su = parallel_prefix_sum(array)                   
    #--------------- Main work ---------------
    end_time = perf_counter()   # Stop timer
    
    # PRINT 
    print(f"Prefix sum result: {pre_su}")
    print(f"Execution time: {end_time-start_time} second(s)")

if __name__ == "__main__":
    main()