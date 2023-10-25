import multiprocessing as mp
import sys
from time import perf_counter

def divide_integer_evenly(number, n):
    base_value = number // n
    remainder = number % n
    result = [base_value] * n

    for i in range(remainder):
        result[i] += 1
    
    return result

def matrix_mul(matrix_a, matrix_b):
    result = [[0 for _ in range(len(matrix_a))] for _ in range(len(matrix_a))]

    # Perform matrix multiplication
    for i in range(len(matrix_a)):
        for j in range(len(matrix_a)):
            for k in range(len(matrix_a)):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]

    return result

def binary_exponentiation(base, exponent):
    result = [[1,0],[0,1]]
    while exponent > 0:
        # If exponent is odd, multiply the result by the base
        if exponent % 2 == 1:
            result = matrix_mul(result, base)
        # Square the base and halve the exponent
        base = matrix_mul(base, base)
        exponent //= 2
    return result

def task(base_matrix, n):
    return binary_exponentiation(base_matrix, n)

def fibo_num_at_n(base_matrix, n):
    chunks = divide_integer_evenly(n-1, mp.cpu_count())

    arg_list = [(base_matrix, n) for n in chunks]

    pool = mp.Pool()
    results = pool.starmap(task, arg_list)

    fibo_num = [[1,0],[0,1]]
    for result in results:
        fibo_num = matrix_mul(fibo_num, result)
    
    return fibo_num[0][0]

def main():
    sys.set_int_max_str_digits(1000000)

    # USER INPUT
    print("Enter the position of the Fibbonaci number: ", end=" ")
    n = int(input())
    print()
    print("Calculating ...")
    print()

    # CREATE BASE MATRIX
    base_matrix = [[1,1],[1,0]]

    start_time = perf_counter() # Start timer
    #--------------- Main work ---------------
    result = fibo_num_at_n(base_matrix, n)
    #--------------- Main work ---------------
    end_time = perf_counter()   # Stop timer

    # PRINT
    print(f"Fibbonaci number at position {n}: {result}")
    print()
    print(f"Execution time: {end_time-start_time} second(s)")


if __name__ == "__main__":
    main()