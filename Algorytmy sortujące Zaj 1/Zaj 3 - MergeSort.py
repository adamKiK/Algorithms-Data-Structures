def merge_sort(array):
    if len(array) > 1:
        # Define variables and arrays
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]

        merge_sort(left)
        merge_sort(right)

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


a = [193, 193, 193, 193, 408, 53, 392, 433, 74, 471, 257, 176, 197, 173, 40, 126, 181, 430, 158, 434]
print(sorted(a))
print(merge_sort(a))
