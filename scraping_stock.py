import bs4
import requests
from bs4 import BeautifulSoup
import json
import urllib.parse
from scraping.date_tratament import date_treatment, dataIso



class Stock:
    def __init__(self, avg_vol):


    def avg_vol(stock):
        avg_vol = None
        r = requests.get(f'https://finance.yahoo.com/quote/{stock}.SA')
        soup = bs4.BeautifulSoup(r.text, 'lxml')
        soup = soup.find('td',{'data-test':'AVERAGE_VOLUME_3MONTH-value'})
        if avg_vol != None:
            avg_vol = float(soup.text.replace(',',''))
        else:
            avg_vol = 0.0
        return avg_vol


acao  = Stock('movi3')

'''


def Stock(stock):
    information = ''
    scrapingtoday = ''
    td_stock = []
    date_treatment()
    # make a scraping for averange volume in YAHOO FINANCE
    r = requests.get(f'https://finance.yahoo.com/quote/{stock}.SA')
    soup = bs4.BeautifulSoup(r.text, 'lxml')
    soup = soup.find('td',{'data-test':'AVERAGE_VOLUME_3MONTH-value'})
    vol_medio = float(soup.text.replace(',',''))
    # make a scraping for stock price in YAHOO FINANCE/stock
    r = requests.get(f'https://finance.yahoo.com/quote/{stock}.SA/history?p={stock}.SA')
    soup = bs4.BeautifulSoup(r.text, 'lxml')
    tbody_soup = soup.find('tbody')
    #The TR is has to be for today
    for tr_soup in tbody_soup:
        td_soup = tr_soup.find('span')
        if td_soup.text == date_treatment():
            scrapingtoday = tr_soup
    for information in scrapingtoday:
        td_stock.append(information.text)
    #all information for the last weekday
    if td_stock[6] == '-':
        td_stock[6] = '0'
    td_stock[6] = td_stock[6].replace(',','')
    volume = float(td_stock[6])
    #return new Dict
    acao = {
            f'{stock}':{
            'currecy':'R$',
            'date':dataIso(),
            'open':float(td_stock[1]),
            'high':float(td_stock[2]),
            'low':float(td_stock[3]),
            'close':float(td_stock[4]),
            'adj_close':float(td_stock[5]),
            'vol':volume,
            'avg_vol':vol_medio}
            }
    return acao
'''
