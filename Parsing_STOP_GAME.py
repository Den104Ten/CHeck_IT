import requests
from bs4 import BeautifulSoup

# Программа по парсингу!

def save():
    with open('parse_info.txt', 'a') as file:  #Создает новый файл, куда буду записываться данные
        file.write(f'{comp["title"]} -> Price: {comp["price"]}\n')  # Выводит название и цену товара

def parse():
    URL = 'https://www.olx.kz/d/elektronika/noutbuki-i-aksesuary/?utm_source=olx&utm_medium=vc'
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 OPR/92.0.0.0'
    }

    response = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(response.content, 'html.parser')
    items = soup.find_all('div', class_='css-qfzx1y')
    comps = []

    for item in items:
        comps.append({
            'title': item.find('h6', class_='css-1pvd0aj-Text eu5v0x0').get_text(strip=True),
            'price': item.find('p', class_='css-1q7gvpp-Text eu5v0x0').get_text(strip=True),
        })

        global comp
        for comp in comps:
            print(f'{comp["title"]} -> Price: {comp["price"]}')
            save()

parse()
