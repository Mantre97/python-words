import random


class Word:
    def __init__(self, number: int, english_word: chr, description: chr, polish_word: chr):
        self.number = number
        self.english_word = english_word
        self.description = description
        self.polish_word = polish_word

    def print_info(self):
        """ Method print all fields of object """
        print('Number: ' + str(self.number) + '\n' +
              'English Word: ' + self.english_word + '\n' +
              'Description: ' + self.description + '\n' +
              'Polish Word: ' + self.polish_word + '\n')

    def hide_letters(self):
        """ Method hide few random letters of word depends on word's length """
        length = len(self.english_word)
        num_to_stay = length // 3
        stay = []

        # Make list of position of characters that you want to hide
        while num_to_stay != len(stay):
            letter_ptr = random.randrange(0, length)
            if letter_ptr not in stay:
                stay.append(letter_ptr)

        # Hash letters which aren't in stay list
        new_word = []
        for i in range(0, length):
            if i in stay:
                new_word.append(self.english_word[i])
            else:
                new_word.append('-')

        return ''.join(new_word)

    def is_letter_in_word(self, letter, word):
        """ Return True if letter is in word or False if isn't """
        for i in range(0, len(self.english_word)):
            if word[i] != self.english_word[i] and letter == self.english_word[i]:
                return True

        return False

    def show_letters(self, letter, word):
        """ When in word is letter return string with that letter """
        for i in range(0, len(self.english_word)):
            if word[i] != self.english_word[i] and letter == self.english_word[i]:
                list_word = list(word)
                list_word[i] = letter
                word = ''.join(list_word)

        return word
