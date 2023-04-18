output = [0] * 20
array = [11, 16, 17, 8, 5, 10, 20, 15, 7, 19, 12, 18, 6, 9, 4, 3, 14, 13, 1, 2]
heap_array = [25, 15, 10, 12, 11, 13, 14]


class Heap:
    def __init__(self, input_array):
        self.array = input_array
        self.array_size = len(input_array)

    def swap(self, first_value_index, second_value_index):
        temporary_value = self.array[first_value_index]
        self.array[first_value_index] = self.array[second_value_index]
        self.array[second_value_index] = temporary_value

    def decide_to_swap(self, root_node_index, child_index):
        root_node_value = self.array[root_node_index]
        child_value = self.array[child_index]
        if root_node_value < child_value:
            self.swap(root_node_index, child_index)
            self.heapify(child_index)

    def heapify(self, root_node_index):
        left_child_index = root_node_index * 2 + 1
        right_child_index = root_node_index * 2 + 2

        if right_child_index < self.array_size:
            self.decide_to_swap(root_node_index, left_child_index)
            self.decide_to_swap(root_node_index, right_child_index)

    def max_heap(self, max_heap_begin_index):
        start_index = max_heap_begin_index // 2 - 1
        stop_index = -1
        for node_index in range(start_index, stop_index, -1):
            self.heapify(node_index)

    def heap_sort(self):
        zero_index = 0
        for last_unsorted_index in range(self.array_size - 1, -1, -1):
            self.max_heap(last_unsorted_index)
            self.swap(zero_index, last_unsorted_index)

heap = Heap(array)
heap.heap_sort()
print(heap.array)
