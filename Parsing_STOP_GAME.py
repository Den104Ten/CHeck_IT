import requests
from bs4 import BeautifulSoup


# css-qfzx1y
# 3.25

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
            'title': item.find('h6', class_='css-1pvd0aj-Text eu5v0x0').get_text(strip=True)
        })

        for comp in comps:
            print(comp['title'])

parse()
