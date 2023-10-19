import multiprocessing
import random
from time import perf_counter

def subprocess_element_cal(matrix_a, matrix_b, n, row_a):
    row = []
    for j in range(0,n):
        temp = 0
        for i in range(0,n):
            temp +=matrix_a[row_a][i]*matrix_b[i][j]
        row.append(temp)
    return row

def matrix_mul_pal(matrix_a, matrix_b, n):

    pool = multiprocessing.Pool()

    arg_list = [(matrix_a, matrix_b, n, row_a) for row_a in range(0,n) ]

    rows = pool.starmap(subprocess_element_cal, arg_list)

    matrix_c = []
    for r in rows:
        matrix_c.append(r)
    return matrix_c
            
def main():
    # USER INPUT
    print("Enter the size n of the square matrices:", end=" ")
    n = int(input())
    print(f"Creating two {n}x{n} matrices...")

    # CREATE MATRIX CASUALLY
    matrix_a = [[random.randint(1,5) for _ in range(n)] for _ in range(n)]
    matrix_b = [[random.randint(1,5) for _ in range(n)] for _ in range(n)]

    print()
    print("Matrix A:")
    # print(matrix_a)
    print("Matrix B:")
    # print(matrix_b)

    # CREATE MATRIX W/ NUMPY

    print("Done ! Calculating...")

    start_time = perf_counter() # Start timer
    #--------------- Main work ---------------
    result = matrix_mul_pal(matrix_a, matrix_b, n)
    #--------------- Main work ---------------
    end_time = perf_counter()   # Stop timer

    # PRINT
    print()
    print("Matrix A * Maxtrix B: ")
    # print(result)
    print()
    print(f"Execution time: {end_time-start_time} second(s)")

if __name__ == "__main__":
    main()


