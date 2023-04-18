import time
import numpy
import SortingClass
import numpy as np
import matplotlib.pyplot as plt

# Defining constant values
MIN_INT = 0
MAX_INT = 5000
size = 100
PERF_TEST_REPEAT = 100

TEST_SIZES = [100, 300, 500, 1000, 3000, 5000]
mean_times = []

for i in range(3):
    mean_times_row = [0]
    for vector_size in TEST_SIZES:
        delta_time = []
        for j in range(PERF_TEST_REPEAT):
            r_vector = np.random.randint(MIN_INT, MAX_INT, vector_size)  # Create vector of random integers
            start_time = time.time()    # Note the value of time before the beginning of sorting

            if i == 0:
                SortingClass.countingSort(r_vector)    # In second iteration run Counting Sort
            elif i == 1:
                SortingClass.mergeSort(r_vector)    # In first iteration run Merge Sort
            else:
                SortingClass.quickSort(r_vector)   # In third iteration run Quick Sort

            # Calculate difference between start and stop
            delta_time.append(time.time() - start_time)

        # Calculate mean algorithm running time of one size and add
        mean_times_row.append(numpy.mean(delta_time))

    # Append mean running times of one algorithm
    mean_times.append(mean_times_row)

# Implement worst and best case scenarios for the sorting algorithms
best_times, worst_times = [], []

i = 0
for i in range(3):
    best_temp, worst_temp = [0], [0]
    for vector_size in TEST_SIZES:
        best_vector = [0] * vector_size
        worst_vector = [j for j in range(vector_size)]
        worst_vector = worst_vector[::-1]

        start_time = time.time()

        # Conditional sorting algorithm selection
        if i == 0:
            SortingClass.countingSort(best_vector)
        elif i == 1:
            SortingClass.mergeSort(best_vector)
        else:
            SortingClass.quickSort(best_vector)
        delta_time = time.time() - start_time

        best_temp.append(delta_time)

        start_time = time.time()
        # Conditional sorting algorithm selection
        if i == 0:
            SortingClass.countingSort(worst_vector)
        elif i == 1:
            SortingClass.mergeSort(worst_vector)
        else:
            SortingClass.quickSort(worst_vector)
        delta_time = time.time() - start_time

        worst_temp.append(delta_time)

    best_times.append(best_temp)
    worst_times.append(worst_temp)

# Constructing final plot

x_sizes = [0, 100, 300, 500, 1000, 3000, 5000]

fig = plt.figure()
ax1 = fig.add_subplot(221)
plt.plot(x_sizes, mean_times[0], label="Counting", linestyle="-", color="y", linewidth=2)
plt.plot(x_sizes, best_times[0], label="Best", color="g")
plt.plot(x_sizes, worst_times[0], label="Worst", color="r")
plt.legend()
ax1.set_ylabel("Time [s]")
ax1.set_xlabel("Array size")

ax2 = fig.add_subplot(222)
plt.plot(x_sizes, mean_times[1], label="Merge", linestyle="--", color="m", linewidth=2)
plt.plot(x_sizes, best_times[1], label="Best", color="g")
plt.plot(x_sizes, worst_times[1], label="Worst", color="r")
plt.legend()
ax2.set_ylabel("Time [s]")
ax2.set_xlabel("Array size")

ax3 = fig.add_subplot(223)
plt.plot(x_sizes, mean_times[2], label="Quick", linestyle=":", color="c", linewidth=2)
plt.plot(x_sizes, best_times[2], label="Best", color="g")
plt.plot(x_sizes, worst_times[2], label="Worst", color="r")
plt.legend()
ax3.set_ylabel("Time [s]")
ax3.set_xlabel("Array size")

ax4 = fig.add_subplot(224)
plt.plot(x_sizes, mean_times[0], label="Counting", linestyle="-", color="y")
plt.plot(x_sizes, mean_times[1], label="Merge", linestyle="--", color="m")
plt.plot(x_sizes, mean_times[2], label="Quick", linestyle=":", color="c")
ax4.set_ylabel("Time [s]")
ax4.set_xlabel("Array size")

ax1.title.set_text('Counting Sort')
ax2.title.set_text('Merge Sort')
ax3.title.set_text('Quick Sort')
ax4.title.set_text('Sort Comparison')

plt.legend()
plt.show()
