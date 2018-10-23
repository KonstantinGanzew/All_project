import csv
from datetime import datetime
import requests
from bs4 import BeautifulSoup



def get_html(Url):
    r = requests.get(Url)                                           # Respanse
    return r.text                                                   # Возвращает HTML код страницы



def get_all_links(html):
    soup = BeautifulSoup(html, 'lxml')
                                                                    # Список объектов соупа
    tds = soup.find('table', id = 'currencies-all').find_all('td', class_ = 'currencies-name')
    links = []                                                      # Списоксо со всеми ссылками со страницы
    for td in tds:
        a = td.find('a', class_ = 'currency-name-container').get('href')
        link = 'https://coinmarketcap.com/all/views/all' + a
        links.append(link)
    return links



def main():
    url = 'https://coinmarketcap.com/all/views/all'
    all_Links = get_all_links(get_html(url))
    print(all_Links)











if __name__ == '__main__':
    main()
