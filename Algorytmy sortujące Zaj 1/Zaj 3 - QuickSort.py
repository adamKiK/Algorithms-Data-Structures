def quick_sort(array, low, high):
    if low < high:
        q = partition(array, low, high)
        quick_sort(array, low, q - 1)
        quick_sort(array, q + 1, high)


def partition(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            temp_val = array[i]
            array[i] = array[j]
            array[j] = temp_val
    temp_val = array[i + 1]
    array[i + 1] = array[high]
    array[high] = temp_val
    return i + 1

a = [193, 193, 193, 193, 408, 53, 392, 433, 74, 471, 257, 176, 197, 173, 40, 126, 181, 430, 158, 434]
size = len(a) - 1
print(sorted(a))
quick_sort(a, 0, size)
print(a)
