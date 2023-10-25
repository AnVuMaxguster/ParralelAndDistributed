import multiprocessing as mp
import math
import numpy as np
from time import perf_counter

def closest_number_divisible_by_n(number, n):
    closest_multiple = (number // n) * n  
    if closest_multiple < number:
        closest_multiple += n

    return closest_multiple

def matrix_mul(matrix_a, matrix_b):
    return np.sum(matrix_a[:, :, np.newaxis] * matrix_b[np.newaxis, :, :], axis=1)

def matrix_mul_block(matrix_a, matrix_b, n, block_size, shift_repeat, row, column):
    matrix_c = matrix_mul(matrix_a[row:row+block_size, column:column+block_size] , matrix_b[row:row+block_size, column:column+block_size])

    for _ in range(shift_repeat):
        for i in range(0, n, block_size): # Left-shift ith block ith times
            matrix_a[i:i+block_size, :] = np.roll(matrix_a[i:i+block_size, :], -block_size, axis=1) # Left-shift ith block of matrix A 1 times
            matrix_b[:, i:i+block_size] = np.roll(matrix_b[:, i:i+block_size], -block_size, axis=0) # Shift-up ith block of matrix B 1 times
        
        partial_c = matrix_mul(matrix_a[row:row+block_size, column:column+block_size] , matrix_b[row:row+block_size, column:column+block_size])
        matrix_c = matrix_c + partial_c

    return matrix_c

def parallel_multiply_matrices(matrix_a, matrix_b):
    n = len(matrix_a)
    sqrt_cpu = round(math.sqrt(mp.cpu_count()))
    new_n = closest_number_divisible_by_n(n, sqrt_cpu)
    block_size = int(new_n / sqrt_cpu)

    # ADD ZEROS TO FILL UP ( IF NECESSARY )
    if new_n != n:
        matrix_a = np.pad(matrix_a, ((0, 0), (0, new_n - n)), mode='constant')
        matrix_b = np.pad(matrix_b, ((0, 0), (0, new_n - n)), mode='constant')
        zeros = np.zeros((new_n - n, matrix_a.shape[1]), dtype=int)
        matrix_a = np.vstack((matrix_a, zeros))
        matrix_b = np.vstack((matrix_b, zeros))

    # INITIAL SHIFT
    for i in range(0, new_n, block_size): # Left-shift ith block ith times
        matrix_a[i:i+block_size, :] = np.roll(matrix_a[i:i+block_size, :], -i, axis=1) # Left-shift ith block of matrix A ith times
        matrix_b[:, i:i+block_size] = np.roll(matrix_b[:, i:i+block_size], -i, axis=0) # Shift-up ith block of matrix B ith times

    # SAVING BLOCK COORDINATES
    blocks = [ ( matrix_a, matrix_b, new_n, block_size, sqrt_cpu - 1, row, column ) for row in range(0, new_n, block_size) for column in range(0, new_n, block_size) ]

    # SPLITTING & CALCULATING ( MULTIPROCESSING )
    pool = mp.Pool()
    results = pool.starmap(matrix_mul_block, blocks)

    # REASSEMBLE BLOCKS INTO RESULT MATRIX
    join = []
    temp = []
    for index,result in enumerate(results):
        temp.append(result)
        if (index + 1) % sqrt_cpu == 0:
            join.append(temp[:])
            temp.clear()
    
    matrix_c = np.block(join)

    # CLEANING UP ZEROS ( IF NECESSARY )
    if new_n != n:
        matrix_c = np.delete(matrix_c, np.s_[-(new_n-n):], axis=1)
        matrix_c = np.delete(matrix_c, np.s_[-(new_n-n):], axis=0)
        
    return matrix_c

def main():
    # USER INPUT
    print("Enter the size n of the square matrices:", end=" ")
    n = int(input())
    print(f"Creating two {n}x{n} matrices...")

    # CREATE BASE MATRIX
    matrix_a = np.random.randint(1, 11, (n, n))
    matrix_b = np.random.randint(1, 11, (n, n))

    print()
    print("Matrix A:")
    print(matrix_a)
    print("Matrix B:")
    print(matrix_b)

    # CREATE MATRIX USING NUMPY

    print("Done ! Calculating...")

    start_time = perf_counter() # Start timer
    #--------------- Main work ---------------
    parallel_multiply_matrices(matrix_a, matrix_b)
    #--------------- Main work ---------------
    end_time = perf_counter()   # Stop timer

    # PRINT
    # print()
    # print("Matrix A * Maxtrix B: ")
    # print(result)
    # print()
    print(f"Execution time: {end_time-start_time} second(s)")

if __name__ == "__main__":
    main()


