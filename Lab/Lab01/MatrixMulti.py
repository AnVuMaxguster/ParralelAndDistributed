import multiprocessing
import random
from time import perf_counter

def matrix_mul(matrix_a, matrix_b, n):
    matrix_c = []
    row_c = []
    for i in range(n):
        for k in range(n):
            temp = 0

            for j in range(n):
                temp += matrix_a[i][j]*matrix_b[j][k]

            row_c.append(temp)

        matrix_c.append(row_c[:]) # Append a copy of row_c. If we append just row_c, it will only be a referece to row_c -> Clearing row_c will remove it out of matrix c as well.
        row_c.clear()

    return matrix_c


def main():
    # USER INPUT
    print("Enter the size n of the square matrices:", end=" ")
    n = int(input())
    print(f"Creating two {n}x{n} matrices...")

    # CREATE MATRIX CASUALLY
    # matrix_a = [[random.randint(1,100) for _ in range(n)] for _ in range(n)]
    # matrix_b = [[random.randint(1,100) for _ in range(n)] for _ in range(n)]

    matrix_a = [[5, 4, 2, 3, 2], [4, 3, 5, 5, 5], [5, 4, 4, 4, 5], [5, 3, 3, 4, 3], [2, 1, 3, 2, 3]]
    matrix_b = [[2, 4, 2, 2, 4], [4, 4, 4, 5, 4], [4, 5, 1, 2, 5], [5, 1, 2, 4, 2], [3, 4, 3, 2, 3]]

    print()
    print("Matrix A:")
    print(matrix_a)
    print("Matrix B:")
    print(matrix_b)

    # CREATE MATRIX W/ NUMPY

    print("Done ! Calculating...")

    start_time = perf_counter() # Start timer
    #--------------- Main work ---------------
    result = matrix_mul(matrix_a, matrix_b, n)
    #--------------- Main work ---------------
    end_time = perf_counter()   # Stop timer

    # PRINT
    print()
    print("Matrix A * Maxtrix B: ")
    print(result)
    print()
    print(f"Execution time: {end_time-start_time} second(s)")

if __name__ == "__main__":
    main()


