from bs4 import BeautifulSoup
import requests

url = 'http://www.jalyuzi.uz/vertikalniy-tkan?page=1'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')

cards = soup.find_all('div', class_='product-thumb')


catalogs = [
    {
        "id": 1,
        "name": "STANDART"
    },
    {
        "id": 2,
        "name": "BASIC"
    },
    {
        "id": 3,
        "name": "ELEGANT"
    },
    {
        "id": 4,
        "name": "EURO"
    },
    {
        "id": 5,
        "name": "DIAMOND"
    },
    {
        "id": 6,
        "name": "EXCLUSIVE"
    },
    {
        "id": 7,
        "name": "коллекция № 0"
    },
    {
        "id": 8,
        "name": "коллекция №1"
    },
    {
        "id": 9,
        "name": "коллекция № 2"
    },
    {
        "id": 10,
        "name": "коллекция № 3"
    },
    {
        "id": 11,
        "name": "коллекция № 4"
    },
    {
        "id": 12,
        "name": "коллекция № 5"
    }
]




data = []

for index, card in enumerate(cards):
    obj = card.find(class_='img-responsive')
    title = card.find('h3')
    table_td = card.find_all('td')
    price = card.find(class_='price')
    index = index - 3

    print(catalogs[index])

    data.append({
        'image': obj.get('src'),
        'name': title.text.strip(),
        'model': title.text.strip(),
        'type_id': False,
        'category': table_td[1].text.strip(),
        'catalog': table_td[3].text.strip(),
        'price': price.text.strip(),
        'count': '10',
        'status': True
    })




urls = [card.find('a').get('href') for card in cards]



for i in range(len(urls)):
    detail_page = requests.get(urls[i])

    soup = BeautifulSoup(detail_page.text, 'lxml')
    product = soup.find(class_='product-col')
    table = product.find_all('table', class_='table-striped')[0]

    object_infos = table.find_all('td')

    data[i]['colors'] = object_infos[1].text
    data[i]['property'] = object_infos[2].text
    data[i]['blackout'] = object_infos[3].text
    data[i]['fabrictype'] = object_infos[4].text
    data[i]['weight'] = object_infos[5].text

