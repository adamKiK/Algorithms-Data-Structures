import random
import time
import matplotlib.pyplot as plt


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


# Generate arrays of different sizes
sizes = [100, 300, 500, 1000]

# Store the mean, worst, and best-case running times for each array size
mean_times = []
worst_times = []
best_times = []

for size in sizes:
    arr = [random.randint(1, 1000) for i in range(size)]

    # Calculate the mean running time
    start_time = time.time()
    for i in range(10):
        merge_sort(arr)
    mean_time = (time.time() - start_time) / 10
    mean_times.append(mean_time)

    # Calculate the worst-case running time
    start_time = time.time()
    for i in range(10):
        merge_sort(arr[::-1])
    worst_time = (time.time() - start_time) / 10
    worst_times.append(worst_time)

    # Calculate the best-case running time
    start_time = time.time()
    for i in range(10):
        merge_sort(sorted(arr))
    best_time = (time.time() - start_time) / 10
    best_times.append(best_time)

# Plot the data
plt.plot(sizes, mean_times, label='Mean')
plt.plot(sizes, worst_times, label='Worst')
plt.plot(sizes, best_times, label='Best')
plt.legend()
plt.xlabel('Array size')
plt.ylabel('Running time (seconds)')
plt.title('Comparison of Merge Sort Algorithm Running Times')
plt.show()