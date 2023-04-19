import random

import heap
import binary_search_tree
import time
import numpy as np
import matplotlib.pyplot as plt

""" HEAPSORT TEST """
MIN_HEAP_INT = 0
MAX_HEAP_INT = 5000
REPEAT_TIMES = 100
TEST_SIZES = [100, 200]

heap_recorded_execution_times_vector = [0]
for array_size in TEST_SIZES:
    delta_time = []
    for i in range(REPEAT_TIMES):
        random_int_vector = list(np.random.randint(MIN_HEAP_INT, MAX_HEAP_INT, array_size))
        start_time = time.time()
        heap.Heap(random_int_vector).heap_sort()
        delta_time.append(time.time() - start_time)
    heap_recorded_execution_times_vector.append(np.mean(delta_time))

""" BST TEST """
NUMBER_OF_VALUES_TO_SEARCH = 10
bst_recorded_execution_times_vector = [0]

for array_size in TEST_SIZES:
    delta_time = []
    random_int_vector = [i for i in range(1, array_size)]
    for i in range(REPEAT_TIMES):
        random.shuffle(random_int_vector)
        bst = binary_search_tree.BinarySearchTree(random_int_vector[0])
        for number in random_int_vector[1::]:
            bst.insert(number)
        values_to_search = random.sample(random_int_vector, NUMBER_OF_VALUES_TO_SEARCH)
        start_time = time.time()
        for number in values_to_search:
            print(bst.search(number))
        delta_time.append((time.time() - start_time)/10)
    bst_recorded_execution_times_vector.append(np.mean(delta_time))

""" CREATE PLOT """

x_sizes = [0, 100, 200]

fig = plt.figure()
ax1 = fig.add_subplot(211)
plt.plot(x_sizes, heap_recorded_execution_times_vector, label="Heapsort", linestyle="-", color="y", linewidth=2)
plt.legend()
ax1.set_ylabel("Time [s]")
ax1.set_xlabel("Array size")

ax2 = fig.add_subplot(212)
plt.plot(x_sizes, bst_recorded_execution_times_vector, label="Binary Search Tree", linestyle="--", color="m", linewidth=2)
plt.legend()
ax2.set_ylabel("Time [s]")
ax2.set_xlabel("Array size")

ax1.title.set_text('Heapsort')
ax2.title.set_text('Binary Search Tree')

plt.legend()
plt.show()
