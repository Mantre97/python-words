import random
import sys
import requests
import pymongo
import word
from bs4 import BeautifulSoup


def scrape_words():
    """ Function scrapping English words and descriptions from website and translate them to Polish """
    list_of_words = []
    number = 1

    print('Scrapping words is in progress... Please wait a minute.')
    try:
        source = requests.get('https://www.vocabulary.com/lists/1976472').text
        soup = BeautifulSoup(source, 'lxml')

    except requests.exceptions.RequestException:
        print('There is problem with connection to base website. Program will be closed.')
        sys.exit()

    for table_row in soup.find_all('li', class_=['entry learnable', 'entry']):
        english_word = table_row.find('a', class_='word dynamictext').text
        description = table_row.find('div', class_='definition').text

        try:
            translator_source = requests.get(f'https://www.diki.pl/slownik-angielskiego?q={english_word}').text
            translator_soap = BeautifulSoup(translator_source, 'lxml')

            polish_word = translator_soap.find('div', class_='dictionaryEntity').ol.li.span.text.strip()

        except requests.exceptions.RequestException:
            print('There is problem with connection to website. Unable to translate word.')
            polish_word = 'Translation error!'

        except AttributeError:
            polish_word = 'Translation error!'

        list_of_words.append({'number': number,
                              'english_word': english_word,
                              'description': description,
                              'polish_word': polish_word})

        number += 1
    print('Scrapped all words.')
    return list_of_words


def add_to_database(list_of_words):
    """ Adding list of scraped words to database """
    my_client = pymongo.MongoClient('mongodb://localhost:27017/')
    my_db = my_client['python-words']
    if 'words' in my_db.list_collection_names():
        my_db['words'].drop()

    my_col = my_db['words']
    my_col.insert_many(list_of_words)

    print('Adding to database is completed.')


def length_of_collection():
    """ Return length of words collection """
    my_client = pymongo.MongoClient('mongodb://localhost:27017/')
    my_db = my_client['python-words']
    my_col = my_db['words']
    return my_col.count()


def find_word_by_number(number):
    """ Return record find in collection which has got number equal to argument """
    my_client = pymongo.MongoClient('mongodb://localhost:27017/')
    my_db = my_client['python-words']
    my_col = my_db['words']
    return my_col.find_one({'number': number})


def find_random_word():
    """ Return type Word object which is random word from database """
    random_word = find_word_by_number(random.randrange(1, length_of_collection() + 1))
    game_word = word.Word(random_word['number'],
                          random_word['english_word'],
                          random_word['description'],
                          random_word['polish_word'])
    return game_word
