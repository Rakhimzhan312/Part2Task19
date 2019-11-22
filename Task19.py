# парсинг

import requests
from bs4 import BeautifulSoup
import csv

def get_html(url):
    req=requests.get(url)
    return req.text

def write_cvs(data):
    with open('lalafo_tels.csv', 'a') as f:
        writer = csv.writer(f)

        writer.writerow( (data['title'],
                          data['price']) )  
    f.close()
def get_content(html):
    soup = BeautifulSoup(html, 'lxml')
    content = soup.find('div' , class_='mr-3').find('article', class_='listing-item')
    for cont in content:
        try:           
            title = cont.find('div', class_='listing-item-main').find('div', class_='').find('a', class_='item listing-item-title pro text-truncate').text.strip()
        except:
            title = ''
        try:
            price = cont.find('div', id_='listing-item-main').find('div', class_='').find('a', class_='listing-item-title').text.strip()
        except:
            price = ''
        data = {'title':title,
                'price':price }

        write_cvs(data)


url = 'https://lalafo.kg/kyrgyzstan/mobilnye-telefony-i-aksessuary?currency=KGS'

html = get_html(url)
get_content(html)
print('hi')