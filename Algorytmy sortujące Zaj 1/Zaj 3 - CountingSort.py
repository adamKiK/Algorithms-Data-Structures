def counting_sort(array):
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


a = [193, 193, 193, 193, 408, 53, 392, 433, 74, 471, 257, 176, 197, 173, 40, 126, 181, 430, 158, 434]

print(counting_sort(a))
print(sorted(a))