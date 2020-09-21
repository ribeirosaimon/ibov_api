from scraping.date_tratament import *
from requests import get
from bs4 import BeautifulSoup
import time

def find_line_by_date(soup, date, tag):
    for index in range(1, len(soup)+1, 1):
        new = soup[index].find(tag).text
        if new == date:
            return soup[index]



def new_soup(stock, tempo=600, brasileira=True):
    #tempo calculado em dias com 60 dias padronizado
    contador,contador_de_erro = 0, 0
    resultado_dos_dias = []
    start_date, end_date = date_timestamp_for_date_utc()
    if brasileira == True:
        start_url = f"https://finance.yahoo.com/quote/{stock.upper()}.SA/history?period1={end_date}&period2={start_date}&interval=1d&filter=history&frequency=1d"
    else:
        start_url = f'https://finance.yahoo.com/quote/{stock}/history?p={stock}'
    browser = BeautifulSoup(get(start_url).content, "html.parser")
    base = browser.findAll('tr')
    print(start_url)
    #pegando as informações dos dias que foi passado no soup
    while tempo != len(resultado_dos_dias):
        try:
            span_in_line = find_line_by_date(base, date_treatment(contador), 'td').find_all('span')
            data = [element.text for element in span_in_line]
            resultado_dos_dias.append(data)

        except Exception as e:
            contador_de_erro += 1
            if contador_de_erro > tempo:
                break
            pass
        contador +=1

    return 'resultado_dos_dias'

retorno = new_soup('movi3', tempo=200)
#date_timestamp_for_date_utc()
print(retorno)
