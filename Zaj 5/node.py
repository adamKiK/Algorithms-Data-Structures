class Node:
    def __init__(self, character=None):
        self.frequency = 0
        self.character = character
        self.left_node = None
        self.right_node = None
        self.encoding = None

    def set_character(self, character):
        self.character = character

    def set_frequency(self, new_frequancy):
        self.frequency = new_frequancy

    def return_frequency(self):
        return self.frequency

    def equal_characters(self, new_character):
        if self.character == new_character:
            return True
        else:
            return False

    def append_child_nodes(self, first_node, second_node):
        if first_node.frequency <= second_node.frequency:
            self.left_node = first_node
            self.right_node = second_node
        else:
            self.left_node = second_node
            self.right_node = first_node

        sum_child_frequency = first_node.frequency + second_node.frequency
        self.frequency = sum_child_frequency
