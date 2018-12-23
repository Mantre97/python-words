import random
import sys

import scrapewords
import word

list_of_words = scrapewords.scrape_words()
scrapewords.add_to_database(list_of_words)

random_word = scrapewords.find_word_by_number(random.randrange(1, scrapewords.length_of_collection() + 1))
game_word = word.Word(random_word['number'],
                      random_word['english_word'],
                      random_word['description'],
                      random_word['polish_word'])

life = 3
list_of_shots = []
word = game_word.hide_letters()
print('Description: ' + game_word.description)
print(word + '  Life: ' + str(life))
while True:
    print('Choose letter:', end=' ')
    shot = input()
    if shot in list_of_shots:
        print('You have already chosen this letter. Try others!')
        continue
    else:
        list_of_shots.append(shot)

    if game_word.is_letter_in_word(shot, word):
        word = game_word.show_letters(shot, word)
        print('Description: ' + game_word.description)
        print(word + '  Life: ' + str(life))
    else:
        life -= 1
        print(f'There is no "{shot}" in this word!    Life: {life}')
        if life == 0:
            print('GAME OVER!', end='\n\n')
            game_word.print_info()
            sys.exit()
