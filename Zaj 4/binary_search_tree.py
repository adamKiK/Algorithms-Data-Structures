class BinarySearchTree:
    def __init__(self, initial_value):
        self.node_value = initial_value
        self.left_child_node = None
        self.right_child_node = None

    def search(self, searched_value):
        if self.node_value == searched_value:
            return self.node_value
        elif searched_value < self.node_value:
            return self.left_child_node.search(searched_value)
        else:
            return self.right_child_node.search(searched_value)

    def choose_child_to_insert(self, inserted_value):
        if inserted_value < self.node_value:
            if self.left_child_node is None:
                self.left_child_node = BinarySearchTree(inserted_value)
            else:
                self.left_child_node.insert(inserted_value)
        else:
            if self.right_child_node is None:
                self.right_child_node = BinarySearchTree(inserted_value)
            else:
                self.right_child_node.insert(inserted_value)

    def insert(self, inserted_value):
        self.choose_child_to_insert(inserted_value)
