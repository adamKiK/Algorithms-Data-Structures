import sys

# Counting Sort
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


# Merge Sort
def mergeSort(array):
    if len(array) > 1:
        # Define variables and arrays
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]

        # Use recursion to sort both arrays
        mergeSort(left)
        mergeSort(right)

        i = j = k = 0
        left_size = len(left)
        right_size = len(right)

        while i < left_size and j < right_size:
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        while i < left_size:
            array[k] = left[i]
            i += 1
            k += 1

        while j < right_size:
            array[k] = right[j]
            j += 1
            k += 1
    return array


# Quick Sort
def quickSort(array):
    if len(array) <= 1:
        return array

    pivot = array[len(array) // 2]
    left, middle, right = [], [], []

    for num in array:
        if num < pivot:
            left.append(num)
        elif num == pivot:
            middle.append(num)
        else:
            right.append(num)

    return quickSort(left) + middle + quickSort(right)
