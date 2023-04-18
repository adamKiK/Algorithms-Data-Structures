array = [13, 11, 17, 8, 7, 5, 18, 16, 20, 14, 4, 2, 1, 3, 12, 9, 10, 15, 19, 6]


class BinarySearchTree:
    def __init__(self, input_array):
        # self.input_value = None
        self.input_array = input_array
        self.searched_value = None
        self.output_index = 0
        self.output_array = [None] * len(self.input_array)

    def search_value_index(self, searched_value):
        self.searched_value = searched_value
        return self.return_equal_value_index()

    def return_equal_value_index(self, root_node_index=0):
        self.output_index = root_node_index
        self.return_next_free_or_equal_index()

    def is_valid_node(self, child_node_index):
        next_child_node_index = child_node_index * 2
        if self.searched_value > self.output_array[child_node_index]:
            next_child_node_index += 2
        else:
            next_child_node_index += 1

        child_node_is_not_none = self.output_array[child_node_index] is not None
        next_child_node_is_not_none = self.output_array[next_child_node_index] is not None

        if child_node_is_not_none and next_child_node_is_not_none:
            return True
        else:
            return False

    def return_next_free_or_equal_index(self, root_node_index=0):
        self.output_index = root_node_index
        root_node_value = self.output_array[root_node_index]
        left_child_node_index = root_node_index * 2 + 1
        right_child_node_index = root_node_index * 2 + 2

        if self.is_valid_node(left_child_node_index) and self.searched_value < root_node_value:
            return self.return_equal_value_index(left_child_node_index)
        elif self.is_valid_node(right_child_node_index) and self.searched_value > root_node_value:
            return self.return_equal_value_index(right_child_node_index)
        else:
            return self.output_index

    def create_binary_search_tree(self):
        self.create_first_tree_node()
        start_index = 1

        for value_index in range(start_index, len(self.input_array)):
            new_input_value = self.input_array[value_index]
            self.insert_new_value(new_input_value)
        pass

    def create_first_tree_node(self):
        self.output_array[0] = self.input_array[0]

    def insert_new_value(self, input_value):
        self.searched_value = input_value
        new_value_index = self.return_next_free_or_equal_index()
        self.output_array[new_value_index] = input_value


bst = BinarySearchTree(array)
bst.create_binary_search_tree()
print(bst.output_array)
