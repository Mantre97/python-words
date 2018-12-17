from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.vocabulary.com/lists/1976472').text

soup = BeautifulSoup(source, 'lxml')

table_row = soup.find('li', class_='entry learnable')

for table_row in soup.find_all('li', class_='entry learnable'):
    word = table_row.find('a', class_='word dynamictext').text
    description = table_row.find('div', class_='definition').text

    print(word + ' - ' + description)

