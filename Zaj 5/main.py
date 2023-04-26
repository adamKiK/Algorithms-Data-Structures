import huffman_coding as hc


def __main__():
    input_text = 'Hello World'
    huffman = hc.HuffmanCoding(input_text)
    huffman.create_huffman_tree()
    top_tree_node = huffman.get_top_tree_node()
    huffman.encode_tree(top_tree_node)
    print(huffman.encode_text())
    print(huffman.decode_text())
    return 0


if __name__ == '__main__':
    __main__()
