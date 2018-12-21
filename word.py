
class Word:
    id = 0

    def __init__(self, english_word: chr, description: chr, polish_word: chr):
        self.english_word = english_word
        self.description = description
        self.polish_word = polish_word

        Word.id += 1
        self.id = Word.id

    def add_to_database(self):
        pass

    def print_info(self):
        print('English Word: ' + self.english_word + '\n' +
              'Description: ' + self.description + '\n' +
              'Polish Word: ' + self.polish_word + '\n' +
              'id: ' + str(self.id) + '\n')
