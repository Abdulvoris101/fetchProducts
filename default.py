from bs4 import BeautifulSoup
import requests
import json

url = 'http://www.jalyuzi.uz/vertikalniy-tkan?page=3'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')

cards = soup.find_all('div', class_='product-thumb')


colors = [
    "Черный",
    "Желтый",
    "Серый",
    "Белый",
    "Бежевый",
    "Молочный",
    "Зеленый",
    "Коричневый",
    "Узорный",
    "Красный",
    "Синий",
    "Однотонный",
    "Бордовый",
    "Золота",
    "Фиолетовый",
    "Оранжевый",
    "Голубой",
    "Розовый",
    "Темно-синий"
]


catalogs = [
    'STANDART',
    'BASIC',
    'ELEGANT',
    'EURO',
    'DIAMOND',
    'EXCLUSIVE',
    'коллекция №0',
    'коллекция №1',
    'коллекция №2',
    'коллекция №3',
    'коллекция №4',
    'коллекция №5'
]


categories = [
    "Рулонные шторы КOMBO",
    "Вертикальные тканевые",
    "Горизонтальные алюминиевые",
    "Мультифактурные жалюзи",
    "Горизонтальные деревянные",
    "Рулонные бамбуковые",
    "Рулонные кассетные",
    "Рулонные кассетные КOMBO",
    "Жалюзи Вертикальные пластиковые",
    "Рулонные шторы РОЛЛО",
    "Рулонные шторы шангриЛА"
    "Фото жалюзи"
]

fabrictypes = [
    "Полиэстер",
    "Алюминиевый"
]



properties = [
   "Гладкие",
    "С фактурой"
]



data = []

for i in range(13):
    obj = cards[i].find(class_='img-responsive')
    title = cards[i].find('h3')
    table_td = cards[i].find_all('td')
    price = cards[i].find(class_='price')


    category_id = categories.index(table_td[1].text.strip())
    price = str(price.text.strip()[:-3])


    usd = 11325.00


    data.append({
        'image_url': obj.get('src'),
        'name': title.text.strip(),
        'model': title.text.strip(),
        'type_id': False,
        'category': category_id + 1,
        'price': str(int(price) / usd)[:6],
        'count': 10,
        'status': True
    })




urls = [card.find('a').get('href') for card in cards]

info = {
    'name': [],
    'value': [],
}

names = []
values = []

for i in range(13):
    detail_page = requests.get(urls[i])

    soup = BeautifulSoup(detail_page.text, 'lxml')
    product = soup.find(class_='product-col')
    table = product.find_all('table', class_='table-striped')[0]
    value_list = table.find_all('td')
    name_list = table.find_all('th')[1:]



    if name_list[1].text == 'Цвет':
        color_id = colors.index(value_list[1].text.capitalize())
        data[i]['color'] = [color_id + 1]


    if name_list[2].text == 'Свойство':
        property_id = properties.index(value_list[2].text.capitalize())
        data[i]['property'] = property_id + 1
            
    
    if name_list[3].text == 'Затемнение:':
        blackout = value_list[3].text.capitalize()
        data[i]['blackout'] = blackout

        


    if name_list[4].text == 'Тип ткани':
        fabrictype_id = fabrictypes.index(value_list[4].text.capitalize())
        data[i]['fabrictype'] = fabrictype_id + 1

            
    if name_list[5].text == 'Ширина ленты':
        weight = value_list[5].text.capitalize()

        if str(weight)[2:] == ' мм':
            weight = value_list[5].text.strip()[:2] + ' mm'

            data[i]['weight'] = weight  


    if name_list[6].text == 'Каталог':
        catalog_id = catalogs.index(value_list[6].text.upper())
        data[i]['catalog'] = catalog_id + 1  
    

data = json.dumps(data)

f = open("db3.json", "a")
f.write(data)
f.close()