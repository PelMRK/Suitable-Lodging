import requests
from bs4 import BeautifulSoup
from lxml import etree
import pandas as pd
import csv


def read_infile():
    with open('infile.csv', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
        j = 0
        for elem in data:
            data[j] = elem[0]
            j += 1
    return data


end_page = 23  # Указываем кол-во страниц с сайта
ads = pd.Series()
prices = pd.Series()
links = pd.Series()
for page in range(1, end_page+1):
    req = requests.get("https://www.avito.ru/sankt_peterburg_i_lo/kvartiry/sdam/na_dlitelnyy_srok"
                       "-ASgBAgICAkSSA8gQ8AeQUg?f=ASgBAgECAkSSA8gQ8AeQUgFFxpoMFXsiZnJvbSI6MCwidG8iOjIwMDAwfQ&p=" +
                       str(page))
    if req.status_code != 200:
        quit()
    soup = BeautifulSoup(req.content, 'html.parser')
    dom = etree.HTML(str(soup))

    address = soup.find_all('div', class_='geo-root-zPwRk iva-item-geo-_Owyg')  # для Москвы и Питера
    # address = soup.find_all('span', class_='geo-address-fhHd0 text-text-LurtD text-size-s-BxGpL')  # для Казани
    price = soup.find_all('span', class_='price-text-_YGDY text-text-LurtD text-size-s-BxGpL')
    link = soup.find_all('div', class_='iva-item-titleStep-pdebR')
    if len(address) == len(price) == len(link):
        pass
    else:
        print(len(address))
        print(len(price))
        print(len(link))

    for el in address:
        print(el.text)
        ads.loc[len(ads)] = el.text.replace(" ", " ")
        print(round(len(ads)/len(address)*100, 2), '%')
    ads.to_csv("addresses.csv")
    for el in price:
        print(el.text)
        el = el.text.replace("₽ в месяц", "")
        el = el.replace("от", ""). replace("₽ за сутки", "")
        prices.loc[len(prices)] = el.replace(" ", "")
        print(round(len(prices)/len(price)*100, 2), '%')
    prices.to_csv("prices.csv", sep=';')
    for el in link:
        print(el.find('a').get("href"))
        links.loc[len(links)] = el.find('a').get("href")
        print(round(len(links)/len(link)*100, 2), '%')
    links.to_csv("links.csv")
