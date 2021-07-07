import time
import numpy as np


# calculates the nth Fibonacci number F_n (assuming F_1 = 1 and F_2 = 2) recursively
def fib(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return fib(n - 1) + fib(n - 2)


# determines the largest j such that j = 3i - 1 with n as an upper bound for j.
def get_largest_even_fib_index_component(n):
    return n // 3


# a presumably inefficient solution (calculates fib(3n-1) twice for each n
def inefficient_solution():
    start_time = time.time()
    n = 1
    sum = 0
    while fib(3 * n - 1) < 4000000:
        sum += fib(3 * n - 1)
        n += 1
    # print(sum)
    inefficient_solution_time = time.time() - start_time
    # print("inefficient solution time: " + str(inefficient_solution_time))
    return inefficient_solution_time


# an iterative solution - first find largest possible index and then only calculate fib(m) once for each iteration in a for loop
# noticing that fib(3n-1) are the even Fibonacci numbers.
def iterative_solution():
    start_time = time.time()
    # # find largest m such that fib(m) < 4 million
    upper_bound = 4000000
    m = 1
    # while next even fib < upper_bound:
    while fib(m) < upper_bound:
        m = m + 1
    largest_fib_index = m
    # print("largest fib index: " + str(largest_fib_index))

    largest_even_fib_index_component = get_largest_even_fib_index_component(largest_fib_index)

    sum = 0
    for n in range(1, largest_even_fib_index_component + 1):
        next_even_fib = fib(3 * n - 1)
        sum += next_even_fib
    # print(sum)
    iterative_solution_time = time.time() - start_time
    # print("iterative solution time: " + str(iterative_solution_time))
    return iterative_solution_time


def possibly_more_efficient_solution():
    start_time = time.time()
    n = 1
    sum = 0

    while (fibby := fib(3 * n - 1)) < 4000000:
        sum += fibby
        n += 1
    # print(sum)
    solution_time = time.time() - start_time
    # print("slightly more efficient solution time: " + str(solution_time))
    return solution_time


def possibly_more_efficient_solution_numpy():
    start_time = time.time()
    n = 1
    sum = 0
    while np.less(fibby := fib(3 * n - 1), 4000000):
        sum += fibby
        n += 1
    # print(sum)
    solution_time = time.time() - start_time
    # print("slightly more efficient solution time: " + str(solution_time))
    return solution_time


def get_avg_solution_times(reps):
    avg_inefficient_time = sum([inefficient_solution() for i in range(1, reps + 1)]) / reps
    avg_possibly_more_efficient_time = sum([possibly_more_efficient_solution() for i in range(1, reps + 1)]) / reps
    avg_iterative_time = sum([iterative_solution() for i in range(1, reps + 1)]) / reps
    avg_numpy_time = sum([possibly_more_efficient_solution_numpy() for i in range(1, reps + 1)]) / reps

    print(str(avg_inefficient_time) + " average inefficient solution time with " + str(reps) + " reps.")
    print(str(avg_possibly_more_efficient_time)+ " average possibly more efficient solution time with " + str(reps) + " reps.")
    print(str(avg_numpy_time) + " average numpy solution time with " + str(reps) + " reps.")
    print(str(avg_iterative_time) + " average iterative solution time with " + str(reps) + " reps.")


if __name__ == '__main__':
    get_avg_solution_times(100)


