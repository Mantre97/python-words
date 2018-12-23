import scrapewords


list_of_words = scrapewords.scrape_words()
scrapewords.add_to_database(list_of_words)

score = 0
option = ''
while option != 'n':
    life = 3
    list_of_shots = []

    game_word = scrapewords.find_random_word()
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
            if word == game_word.english_word:
                score += 1
                print(f'\nWIN! Your score: {score}\n')
                game_word.print_info()
                print('\nWould you like to play again? (y/n)')
                option = input()
                break
            print('Description: ' + game_word.description)
            print(f'{word}  Life: {life}')
        else:
            life -= 1
            print(f'There is no "{shot}" in this word!    Life: {life}')
            if life == 0:
                score -= 1
                print(f'\nGAME OVER! Your score: {score}\n')
                game_word.print_info()
                print('\nWould you like to play again? (y/n)')
                option = input()
                break
