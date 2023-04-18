import random
import time

def countingSort(array):
    # Define variables and arrays
    count_array_len = max(array) + 1    # Length of the counting array
    count_array = [0] * count_array_len
    output_array = [0] * len(array)

    # Count occurrences of numbers from array
    for num in array:
        count_array[num] += 1

    # Cumulative sum of count_array
    for i in range(1, count_array_len):
        count_array[i] += count_array[i-1]

    # Sorting loop (sorted indexes of values are calculated from cumulative array
    for num in array:
        output_array[count_array[num]-1] = num
        count_array[num] -= 1   # Decrease value by 1 to populate earlier indexes

    return output_array
# Function to test counting sort for worst case scenario

def test_counting_sort_worst_case(size):
    # Create array of worst case scenario
    arr = [i*(5000//size) for i in range(size)]

    # Start timer
    start_time = time.time()

    # Sort the array using Counting Sort
    sorted_arr = countingSort(arr)

    # End timer
    end_time = time.time()

    # Check if the array is sorted correctly
    for i in range(len(sorted_arr)-1):
        if sorted_arr[i] > sorted_arr[i+1]:
            print("Error: Array not sorted correctly!")
            return

    # Print time taken for sorting
    print("Worst Case - Size:", size, "- Time taken:", end_time - start_time)
# Function to test counting sort for best case scenario

def test_counting_sort_best_case(size):
    # Create array of best case scenario
    arr = [i for i in range(size)]

    # Start timer
    start_time = time.time()

    # Sort the array using Counting Sort
    sorted_arr = countingSort(arr)

    # End timer
    end_time = time.time()

    # Check if the array is sorted correctly
    for i in range(len(sorted_arr)-1):
        if sorted_arr[i] > sorted_arr[i+1]:
            print("Error: Array not sorted correctly!")
            return

    # Print time taken for sorting
    print("Best Case - Size:", size, "- Time taken:", end_time - start_time)
# Function to test counting sort for mean case scenario

def test_counting_sort_mean_case(size):
    # Create array of random integers
    arr = [random.randint(0,5000) for i in range(size)]

    # Start timer
    start_time = time.time()

    # Sort the array using Counting Sort
    sorted_arr = countingSort(arr)

    # End timer
    end_time = time.time()

    # Check if the array is sorted correctly
    for i in range(len(sorted_arr)-1):
        if sorted_arr[i] > sorted_arr[i+1]:
            print("Error: Array not sorted correctly!")
            return

    # Print time taken for sorting
    print("Mean Case - Size:", size, "- Time taken:", end_time - start_time)
# Test worst, best and mean case scenarios for different array sizes
sizes = [100, 500, 1000, 3000, 5000]

for size in sizes:
    test_counting_sort_worst_case(size)
    test_counting_sort_best_case(size)
    test_counting_sort_mean_case(size)
