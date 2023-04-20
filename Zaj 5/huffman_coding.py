class HuffmanCoding:
    def __init__(self, input_string):
        self.input_string = input_string
        self.character_frequency_table = []
        self.appended_characters_to_frequency_table = []

    def create_frequency_table(self):
        for character in self.input_string:
            if character not in self.appended_characters_to_frequency_table:
                self.appended_characters_to_frequency_table.append(character)
                self.character_frequency_table.append([character, 1])
            else:
                character_index = self.appended_characters_to_frequency_table.index(character)
                self.character_frequency_table[character_index][1] += 1

    def return_appended_characters(self):
        return self.appended_characters_to_frequency_table