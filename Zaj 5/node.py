class Node:
    def __init__(self, character=None):
        self.frequency = 0
        self.character = character
        self.left_node = None
        self.right_node = None
        self.encoding = None

    def set_encoding(self, encoding):
        self.encoding = encoding

    def set_char(self, character):
        self.character = character

    def set_frequency(self, new_frequency):
        self.frequency = new_frequency

    def has_char(self):
        if self.character is not None:
            return self.character
        else:
            return False

    def get_frequency(self):
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
