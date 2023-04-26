import node


class HuffmanCoding:
    def __init__(self, input_string):
        self.encoded_text = None
        self.input_string = input_string
        self.char_frequency_table = []
        self.distinct_chars_in_frequency_table = []
        self.node_array = []
        self.lowest_frequency_index = 0
        self.second_lowest_frequency_index = 1
        self.top_tree_node = None
        self.encode_dict = dict()
        self.decode_dict = dict()

    def get_top_tree_node(self):
        return self.top_tree_node

    def create_frequency_table(self):
        for character in self.input_string:
            if character not in self.distinct_chars_in_frequency_table:
                self.distinct_chars_in_frequency_table.append(character)
                self.char_frequency_table.append([character, 1])
            else:
                character_index = self.distinct_chars_in_frequency_table.index(character)
                self.char_frequency_table[character_index][1] += 1

    def return_appended_characters(self):
        return self.distinct_chars_in_frequency_table

    def set_node_frequencies(self):
        distinct_characters_array_size = len(self.distinct_chars_in_frequency_table)
        for index in range(distinct_characters_array_size):
            character = self.distinct_chars_in_frequency_table[index]
            character_frequency = self.input_string.count(character)
            self.node_array.append(node.Node(character))
            self.node_array[index].set_frequency(character_frequency)

    def set_nodes_least_frequency_indexes(self):
        self.lowest_frequency_index = 0
        self.second_lowest_frequency_index = 1
        lowest_value = self.node_array[self.lowest_frequency_index].get_frequency()

        for node_index in range(1, len(self.node_array)):
            if self.node_array[node_index].get_frequency() <= lowest_value:
                self.second_lowest_frequency_index = self.lowest_frequency_index
                self.lowest_frequency_index = node_index
                lowest_value = self.node_array[self.lowest_frequency_index].get_frequency()

    def delete_linked_child_nodes(self):
        if self.lowest_frequency_index > self.second_lowest_frequency_index:
            del self.node_array[self.lowest_frequency_index]
            del self.node_array[self.second_lowest_frequency_index]
        else:
            del self.node_array[self.second_lowest_frequency_index]
            del self.node_array[self.lowest_frequency_index]

    def create_parent_children_structure(self):
        self.node_array.append(node.Node())
        self.node_array[-1].append_child_nodes(self.node_array[self.lowest_frequency_index],
                                               self.node_array[self.second_lowest_frequency_index])

    def create_huffman_tree(self):
        self.create_frequency_table()
        self.set_node_frequencies()
        node_array_size = len(self.node_array)

        while node_array_size > 1:
            self.set_nodes_least_frequency_indexes()
            self.create_parent_children_structure()
            self.delete_linked_child_nodes()
            node_array_size -= 1

        self.top_tree_node = self.node_array[0]

    def encode_tree(self, parent_node, encoding=""):
        encoding += "0"
        if parent_node.left_node.has_char():
            parent_node.left_node.set_encoding(encoding)
            self.add_to_dictionaries(parent_node.left_node)
        else:
            self.encode_tree(parent_node.left_node, encoding)

        encoding = encoding[:-1] + "1"
        if parent_node.right_node.has_char():
            parent_node.right_node.set_encoding(encoding)
            self.add_to_dictionaries(parent_node.right_node)
        else:
            self.encode_tree(parent_node.right_node, encoding)

    def add_to_dictionaries(self, added_node):
        self.add_to_encode_dict(added_node)
        self.add_to_decode_dict(added_node)

    def add_to_encode_dict(self, added_node):
        self.encode_dict[added_node.get_char()] = added_node.get_encoding()

    def add_to_decode_dict(self, added_node):
        self.decode_dict[added_node.get_encoding()] = added_node.get_char()

    def encode_text(self):
        output_string = ""
        for char in self.input_string:
            output_string += self.encode_dict[char]
        self.encoded_text = output_string
        return output_string

    def decode_text(self):
        symbol = ""
        output_string = ""
        for char in self.encoded_text:
            symbol += char
            if symbol in self.decode_dict:
                output_string += self.decode_dict[symbol]
                symbol = ""
        return output_string
