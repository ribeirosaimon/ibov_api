from requests import get
from bs4 import BeautifulSoup
from scraping.date_tratament import date_treatment
import time

def find_line_by_date(soup, date, tag):
    for index in range(1, len(soup)+1, 1):
        new = soup[index].find(tag).text
        if new == date:
            return soup[index]

def soup_url(stock):
    lista_acao = []
    start_url = f"https://finance.yahoo.com/quote/{stock}.SA/history?p={stock}.SA"
    browser = BeautifulSoup(get(start_url).content, "html.parser")
    time.sleep(0.5)
    base = browser.findAll('tr')
    span_in_line = find_line_by_date(base, date_treatment(), 'td').find_all('span')
    data = [element.text for element in span_in_line]
    for x in range(1,10):
        try:
            span_in_line = find_line_by_date(base, date_treatment(x), 'td').find_all('span')
            obv = [element.text for element in span_in_line]
            lista_acao.append(obv)
        except:
            pass
    return [data, lista_acao]

def avg_vol(stock):
    r = f'https://finance.yahoo.com/quote/{stock}.SA'
    time.sleep(0.5)
    browser = BeautifulSoup(get(r).content, 'lxml')
    soup = browser.find('td', {'data-test': 'AVERAGE_VOLUME_3MONTH-value'})
    try:
        avg_vol = float(soup.text.replace(',', ''))
    except:
        avg_vol = 0.0
    return float(avg_vol)
