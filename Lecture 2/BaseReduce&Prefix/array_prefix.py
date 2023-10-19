from time import perf_counter

def prefix_sum_elements(array):
    for index,_ in enumerate(array[1:], start=1):    # enumerate: lấy cặp index,value từ list
        array[index] += array[index-1]

def main():
    # USER INPUT
    print("Enter the starting value of the array:", end=" ")
    first = int(input())
    print("Enter the ending value of the array:", end=" ")
    last = int(input ())
    print()

    # INIT ARRAY
    array = list(range(first,last+1))

    start_time = perf_counter() # Start timer
    #--------------- Main work ---------------
    prefix_sum_elements(array)                   
    #--------------- Main work ---------------
    end_time = perf_counter()   # Stop timer
    
    # PRINT 
    print(f"Prefix sum result: {array}")
    print(f"Execution time: {end_time-start_time} second(s)")

if __name__ == "__main__":
    main()