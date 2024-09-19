import time
import random
import matplotlib.pyplot as plt
from InsertionSort import insertionSort
 

def measure_time(algorithm, A):
    start_time = time.time()
    algorithm(A)
    end_time = time.time()
    return end_time - start_time

def analyze_complexity(algorithm, input_sizes):
    times = []
    for size in input_sizes:
        A = random.sample(range(size * 10), size)
        exec_time = measure_time(algorithm, A)
        times.append(exec_time)

    plt.plot(input_sizes, times, label=algorithm.__name__)
    plt.xlabel('Input Size')
    plt.ylabel('Execution Time (seconds)')
    plt.title(f'Time Complexity of {algorithm.__name__}')
    plt.legend()
    plt.show()

input_sizes = [100, 500, 1000, 5000, 10000]
analyze_complexity(insertionSort, input_sizes)
