import bs4
import requests
from bs4 import BeautifulSoup
import json
import time
import urllib.parse
from scraping.date_tratament import date_treatment


def scrap_stocks(stock):
    td_stock = []
    data = date_treatment()
    # make a scraping for averange volume in YAHOO FINANCE
    r = requests.get(f'https://finance.yahoo.com/quote/{stock}.SA')
    soup = bs4.BeautifulSoup(r.text, 'lxml')
    soup = soup.find('td',{'data-test':'AVERAGE_VOLUME_3MONTH-value'})
    vol_medio = float(soup.text.replace(',',''))
    # make a scraping for stock price in YAHOO FINANCE/stock
    time.sleep(0.5)
    r = requests.get(f'https://finance.yahoo.com/quote/{stock}.SA/history?p={stock}.SA')
    soup = bs4.BeautifulSoup(r.text, 'lxml')
    tbody_soup = soup.find('tbody')
    #The TR is has to be for today
    for tr_soup in tbody_soup:
        td_soup = tr_soup.find('span')
        if td_soup.text == data:
            tr_soup_today = tr_soup
            for td in tr_soup_today:
                td_stock.append(td.text)

    if td_stock[6] == '-':
        td_stock[6] = 0
    else:
        td_stock[6] = td_stock[6].replace(',','')
        td_stock[6] = float(td_stock[6])
    dict_stock = {'stock':stock,
        'date':td_stock[0],
        'open':float(td_stock[1]),
        'high':float(td_stock[2]),
        'low':float(td_stock[3]),
        'close':float(td_stock[4]),
        'volume':td_stock[6],
        'volume medio':vol_medio
    }
    return dict_stock
