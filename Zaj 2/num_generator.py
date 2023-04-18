import numpy as np
import time
import matplotlib.pyplot as plt

# Defining constant values
MIN_INT = -5000
MAX_INT = 5000
size = 100
PERF_TEST_REPEAT = 100

TEST_SIZES = [100, 500, 1000, 5000]
mean_times = []


def random_ints(minim, maxim, vect_size):
    rng = np.random.default_rng(12345)
    rints = rng.integers(low=minim, high=maxim, size=vect_size) # Create random array of numbers in range MIN_INT -> MAX_INT of size SIZE
    return rints


def selection_sort(x):
    for i in range(len(x)):
        smallest = x[i]
        for j in range(i,len(x)):
            if x[j] < smallest:
                smallest = x[j]
                x[j] = x[i]
                x[i] = smallest
    return x


def insertion_sort(x):
    i = 0
    while i < (len(x)-1): # Indeksowanie od zera, więc długosc listy -1
        if x[i+1] < x[i]:
            temp_val = x[i]
            x[i] = x[i+1]
            x[i+1] = temp_val
            i = 0
        else:
            i += 1
    return x


def bubble_sort(x):
    for i in range(len(x)):
        changed = False
        for j in range(0,len(x)-i-1):
            if x[j+1] < x[j]:
                temp_val = x[j]
                x[j] = x[j+1]
                x[j+1] = temp_val
                changed = True
        if changed != True:
            break
    return x


for k in range(3):
    mean_times_row = [0]
    for vector_size in TEST_SIZES:
        delta_time = []
        for j in range(PERF_TEST_REPEAT):
            r_vector = random_ints(MIN_INT, MAX_INT, vector_size)  # Create vector of random integers
            start_time = time.time()    # Note the value of time before the beginning of sorting

            if k == 0:
                selection_sort(r_vector)    # In first iteration run Selection Sort
            elif k == 1:
                insertion_sort(r_vector)    # In second iteration run Insertion Sort
            else:
                bubble_sort(r_vector)   # In third iteration run Bubble Sort

            delta_time.append(float(time.time() - start_time))   # Calculate difference between start and stop
        mean_times_row.append(float(sum(delta_time)/len(delta_time)))  # Calculate mean algorithm running time of one size and add
    mean_times.append(mean_times_row)   # Append mean running times of one algorithm

fig = plt.figure()
ax1 = fig.add_subplot(221)
plt.plot([0, 100, 500, 1000, 5000], mean_times[0])
ax2 = fig.add_subplot(222)
plt.plot([0, 100, 500, 1000, 5000], mean_times[1])
ax3 = fig.add_subplot(223)
plt.plot([0, 100, 500, 1000, 5000], mean_times[2])
ax4 = fig.add_subplot(224)
ax1.title.set_text('Selection Sort')
ax2.title.set_text('Insertion Sort')
ax3.title.set_text('Bubble Sort')
ax4.title.set_text('PUSTY')
plt.show()