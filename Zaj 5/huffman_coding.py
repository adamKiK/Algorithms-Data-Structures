class HuffmanCoding:
    def __init__(self, input_string):
        self.input_string = input_string
        self.char_frequency_table = []
        self.distinct_chars_in_frequency_table = []

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

