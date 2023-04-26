import huffman_coding as hc
import time
import matplotlib.pyplot as plt

files_to_check_paths = ["D:\Projects\Algorytmy i struktury danych\Zaj 5\Test_Files\\1_wers.txt",
                        "D:\Projects\Algorytmy i struktury danych\Zaj 5\Test_Files\\3_wersy.txt",
                        "D:\Projects\Algorytmy i struktury danych\Zaj 5\Test_Files\\10_wersow.txt",
                        "D:\Projects\Algorytmy i struktury danych\Zaj 5\Test_Files\\25_wersow.txt",
                        "D:\Projects\Algorytmy i struktury danych\Zaj 5\Test_Files\\50_wersow.txt"]

text_size_array = []
encoding_time_array = []
decoding_time_array = []
original_size_array = []
compressed_size_array = []
compression_percent_array = []


def huffman_cycle(input_file):
    results = dict()
    with open(input_file, "r") as input_textfile:
        input_text = input_textfile.read()

    huffman = hc.HuffmanCoding(input_text)
    huffman.create_huffman_tree()
    top_parent_node = huffman.get_top_tree_node()
    huffman.encode_tree(top_parent_node)

    encoding_time_start = time.perf_counter_ns()
    huffman.encode_text()
    encoding_delta_time = (time.perf_counter_ns() - encoding_time_start) / 1000000

    decoding_time_start = time.perf_counter_ns()
    huffman.decode_text()
    decoding_delta_time = (time.perf_counter_ns() - decoding_time_start) / 1000000

    original_bit_number = huffman.original_bits_number
    compressed_bit_number = huffman.compressed_bit_number
    compression_percent = round((compressed_bit_number/original_bit_number)*100.00, 2)
    results["encoding_time"] = encoding_delta_time
    results["decoding_time"] = decoding_delta_time
    results["origin_size"] = huffman.original_bits_number
    results["compressed_size"] = huffman.compressed_bit_number
    results["text_length"] = len(huffman.input_string)
    results["compression_%"] = compression_percent

    return results


def create_plots():
    fig = plt.figure()
    ax1 = fig.add_subplot(221)
    plt.plot(text_size_array, original_size_array, label="Original size", color="r", linewidth=2)
    plt.plot(text_size_array, compressed_size_array, label="Compressed size", color="g", linewidth=2)
    plt.legend()
    ax1.set_ylabel("Memory Use [bit]")
    ax1.set_xlabel("Text size")

    ax2 = fig.add_subplot(222)
    plt.plot(text_size_array, encoding_time_array)
    ax2.set_ylabel("Time [ms]")
    ax2.set_xlabel("Text size")

    ax3 = fig.add_subplot(223)
    plt.plot(text_size_array, decoding_time_array)
    ax3.set_ylabel("Time [ms]")
    ax3.set_xlabel("Text size")

    ax4 = fig.add_subplot(224)
    plt.plot(text_size_array, compression_percent_array)
    ax4.set_ylabel("Compression level [%]")
    ax4.set_xlabel("Text size")

    ax1.title.set_text('Size comparison')
    ax2.title.set_text('Encoding time')
    ax3.title.set_text('Decoding time')
    ax4.title.set_text('Compression level')

    fig.suptitle("Huffmann's Coding Results")
    plt.show()


def __main__():
    iteration_number = 0
    for file_path in files_to_check_paths:
        results = huffman_cycle(file_path)

        text_size_array.append(results["text_length"])
        encoding_time_array.append(results["encoding_time"])
        decoding_time_array.append(results["decoding_time"])
        original_size_array.append(results["origin_size"])
        compressed_size_array.append(results["compressed_size"])
        compression_percent_array.append(results["compression_%"])

        iteration_number += 1

    create_plots()
    return 0


if __name__ == '__main__':
    __main__()
