class Heap:
    def __init__(self, input_array: []):
        self.input_array = input_array
        self.sorted_array = [0] * len(self.input_array)

    def swap(self, first_value_index, second_value_index):
        temporary_value = self.input_array[first_value_index]
        self.input_array[first_value_index] = self.input_array[second_value_index]
        self.input_array[second_value_index] = temporary_value

    def decide_to_swap(self, root_node_index, child_index):
        root_node_value = self.input_array[root_node_index]
        child_value = self.input_array[child_index]
        if root_node_value < child_value:
            self.swap(root_node_index, child_index)
            self.heapify(child_index)

    def heapify(self, root_node_index):
        left_child_index = root_node_index * 2 + 1
        right_child_index = root_node_index * 2 + 2

        if left_child_index < len(self.input_array):
            self.decide_to_swap(root_node_index, left_child_index)

        if right_child_index < len(self.input_array):
            self.decide_to_swap(root_node_index, right_child_index)

    def max_heap(self, max_heap_begin_index):
        start_index = max_heap_begin_index // 2 - 1
        stop_index = -1
        for node_index in range(start_index, stop_index, -1):
            self.heapify(node_index)

    def heap_sort(self):
        zero_index = 0
        array_size = len(self.input_array)
        for last_unsorted_index in range(array_size - 1, -1, -1):
            self.max_heap(last_unsorted_index)
            self.swap(zero_index, last_unsorted_index)
            last_sorted_value = self.input_array.pop()
            self.sorted_array[last_unsorted_index] = last_sorted_value
            