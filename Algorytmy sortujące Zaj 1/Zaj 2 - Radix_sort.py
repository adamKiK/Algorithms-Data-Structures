def counting_sort(arr, place):
    SIZE = len(arr)
    count = [0] * 10
    sorted_arr = [0] * SIZE

    # Count each occurrence in input set
    for i in range(SIZE):
        index = arr[i] // place
        count[index % 10] += 1

    # Cumulate count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Place the elements in output array after finding the index of each element of original array in count array
    for s in range(SIZE - 1, -1, -1):
        index = arr[s] // place
        sorted_arr[count[index % 10] - 1] = arr[s]
        count[index % 10] -= 1

    for i in range(0, SIZE):
        arr[i] = sorted_arr[i]

def radix(arr):
    max_element = max(arr)

    place = 1
    while max_element // place > 0:
        counting_sort(arr, place)
        place *= 10

    return arr

a = [193, 162, 29, 25, 408, 53, 392, 433, 74, 471, 257, 176, 197, 173, 40, 126, 181, 430, 158, 434]

print(radix(a))