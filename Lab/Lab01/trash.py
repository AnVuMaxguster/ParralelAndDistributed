import multiprocessing as mp
import random
import math
import numpy as np
from time import perf_counter

def closest_number_divisible_by_n(number, n):
    closest_multiple = (number // n) * n  
    if closest_multiple < number:
        closest_multiple += n

    return closest_multiple

def regular_matrix_mul(matrix_a, matrix_b, N, n, row_a, column_a, row_b, column_b):
    matrix_c = []
    row_c = []

    for i in range(row_a, row_a + n):
        if i < N:
            for j in range(column_b, column_b + n):
                if j < N:
                    temp = 0
                    l = row_b
                    for k in range(column_a, column_a + n):
                        if k < N:
                            temp += matrix_a[i][k]*matrix_b[l][j]
                            l += 1
                    row_c.append(temp)
            matrix_c.append(row_c[:])
            row_c.clear()

    return matrix_c

def matrix_mul_block(matrix_a, matrix_b, N, n, block_size, shift_repeat, row, column): # For each 1 Block of A x 1 Block of B
    # INITIAL SHIFT:
    if row!=0: 
        column_a = ( column + row ) % n # Shift row left i times
    else:
        column_a = column

    if column!=0: 
        row_b = ( column + row ) % n # Shift column up j times
    else:
        row_b = row
    
    # INITIAL MULTIPLICATION:
    result_block = regular_matrix_mul(matrix_a, matrix_b, N, block_size, row, column_a, row_b, column)

    for _ in range(shift_repeat - 1):
        column_a = ( column_a + block_size ) % n 
        row_b = ( row_b + block_size ) % n 
        rotate_mul = regular_matrix_mul(matrix_a, matrix_b, N, block_size, row, column_a, row_b, column)
        result_block = result_block + rotate_mul

    return result_block

def parallel_multiply_matrices(matrix_a, matrix_b):
    n = len(matrix_a)
    sqrt_cpu = round(math.sqrt(mp.cpu_count()))
    new_n = closest_number_divisible_by_n(n, sqrt_cpu)
    block_size = int(new_n / sqrt_cpu)

    # SAVING BLOCK COORDINATES
    blocks = [(matrix_a, matrix_b, n, new_n, block_size, sqrt_cpu, row, column) for row in range(0, new_n, block_size) for column in range(0, new_n, block_size)]

    pool = mp.Pool()

    # SPLITTING & CALCULATING ( MULTIPROCESSING )
    results = pool.starmap(matrix_mul_block, blocks)

    # REASSEMBLE BLOCKS INTO RESULT MATRIX
    matrix_c = [[] for _ in range(n)]

    row = 0 
    for index,result in enumerate(results):
        if index!=0 and index % sqrt_cpu == 0:
            row += block_size
        for i,r in enumerate(result):
            matrix_c[row+i].extend(r)
    
    print(matrix_c)
    # return matrix_c

def main():
    # USER INPUT
    print("Enter the size n of the square matrices:", end=" ")
    n = int(input())
    print(f"Creating two {n}x{n} matrices...")

    # CREATE RANDOM SQUARE MATRICES
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

if _name_ == "_main_":
    main()