from bs4 import BeautifulSoup
import requests
import json
from post import post_objects



pageNum = int(input("Number of page: "))


url = f'http://www.jalyuzi.uz/rulonniy-bambukiviy'

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
    "Темно-синий",
    'Салатовый'
]


catalogs = [
    'STANDART',
    'BASIC',
    'ELEGANT',
    'EURO',
    'DIAMOND',
    'EXCLUSIVE',
    'коллекция № 0',
    'коллекция №1',
    'коллекция № 2',
    'коллекция № 3',
    'коллекция № 4',
    'коллекция № 5'
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
    "Рулонные шторы шангриЛА",
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

for index, card in enumerate(cards):
    obj = card.find(class_='img-responsive')
    title = card.find('h3')
    table_td = card.find_all('td')
    price = card.find(class_='price')


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
        'status': True,
        'color': []
    })




urls = [card.find('a').get('href') for card in cards]

info = {
    'name': [],
    'value': [],
}

names = []
values = []

for i in range(len(urls)):
    detail_page = requests.get(urls[i])

    soup = BeautifulSoup(detail_page.text, 'lxml')
    product = soup.find(class_='product-col')
    table = product.find_all('table', class_='table-striped')[0]
    value_list = table.find_all('td')
    name_list = table.find_all('th')[1:]    
    



   
    
    try:

        if name_list[1].text == 'Цвет':
            color_id = colors.index(value_list[1].text.capitalize())
            data[i]['color'].append(color_id + 1)

    except IndexError:
        print('stupid color')

    
    # try:

    #     if name_list[1].text == 'Свойство':
    #         property_id = properties.index(value_list[1].text.capitalize())
    #         data[i]['property'] = property_id + 1
        
    # except IndexError:
    #     print('stupid property')

    # try:
    #     if name_list[3].text == 'Каталог':
    #         catalog_id = catalogs.index(value_list[3].text)
    #         data[i]['catalog'] = catalog_id + 1  
    #     elif name_list[3].text == 'Свойство':
    #         property_id = properties.index(value_list[3].text.capitalize())
    #         data[i]['property'] = property_id + 1
    # except IndexError:
    #     print('stupid catalog')

    
    

    
    

    
    # try:

    #     if name_list[4].text == 'Ширина':
    #         weight = value_list[4].text.capitalize()

    #         if str(weight)[3:] == ' см':
    #             weight = value_list[4].text.strip()[:3] + ' sm'
    #             data[i]['weight'] = weight 
            
    # except IndexError:
    #     print('stupid weight')

    try:

        if name_list[2].text == 'Затемнение:':
            blackout = value_list[2].text.capitalize()
            data[i]['blackout'] = blackout
    except IndexError:
        print('stupid blackout')

    # try:
    #     if name_list[3].text == 'Тип ткани':
    #         fabrictype_id = fabrictypes.index(value_list[3].text.capitalize())
    #         data[i]['fabrictype'] = fabrictype_id + 1
    # except IndexError:
    #     print('stupid fabrictype')
    
    


data = json.dumps(data)

f = open(f"dbrulloniy{pageNum}.json", "a")
f.write(data)
f.close()

# post_objects(pageNum=pageNum)