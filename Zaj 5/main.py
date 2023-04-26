import huffman_coding as hc
import node

input_text = 'Hello World'
node_array = []
huffman = hc.HuffmanCoding(input_text)
appended_char_table = huffman.return_appended_characters()
huffman.create_frequency_table()


def set_node_frequencies():
    distinct_characters_array_size = len(huffman.distinct_chars_in_frequency_table)
    for index in range(distinct_characters_array_size):
        character = huffman.distinct_chars_in_frequency_table[index]
        character_frequency = huffman.input_string.count(character)
        node_array.append(node.Node(character))
        node_array[index].set_frequency(character_frequency)


def __main__():
    set_node_frequencies()

    while len(node_array) > 1:
        lowest_frequency_index = 0
        lowest_value = node_array[lowest_frequency_index].return_frequency()
        second_lowest_frequency_index = 1

        for node_index in range(1, len(node_array)):
            if node_array[node_index].return_frequency() <= lowest_value:
                second_lowest_frequency_index = lowest_frequency_index
                lowest_frequency_index = node_index
                lowest_value = node_array[lowest_frequency_index].return_frequency()

        node_array.append(node.Node())
        node_array[-1].append_child_nodes(node_array[lowest_frequency_index], node_array[second_lowest_frequency_index])

        if lowest_frequency_index > second_lowest_frequency_index:
            del node_array[lowest_frequency_index]
            del node_array[second_lowest_frequency_index]
        else:
            del node_array[second_lowest_frequency_index]
            del node_array[lowest_frequency_index]


    return 0


if __name__ == '__main__':
    __main__()
