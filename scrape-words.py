import sys
import requests
from bs4 import BeautifulSoup

try:
    source = requests.get('https://www.vocabulary.com/lists/1976472').text
    soup = BeautifulSoup(source, 'lxml')

except requests.exceptions.RequestException:
    print('There is problem with connection to base website. Program will be closed.')
    sys.exit()

table_row = soup.find('li', class_='entry learnable')

for table_row in soup.find_all('li', class_='entry learnable'):
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

    print(english_word + ' - ' + description + ' - ' + polish_word)
