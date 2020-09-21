from scraping.date_tratament import *
from requests import get
from bs4 import BeautifulSoup
import time
import requests


def new_soup(stock, brasileira=True):
    lista_montar = []
    start_date, end_date = date_timestamp_for_date_utc()
    if brasileira == True:
        stock = f'{stock}.sa'
    endpoint = f'https://query2.finance.yahoo.com/v8/finance/chart/{stock}?symbol=movi3.sa&period1={end_date}&period2={start_date}&interval=1d&includePrePost=true&events=div%2Csplit'
    resposta = requests.request('GET', endpoint)
    tamanho_do_json = resposta.json()['chart']['result'][0]['timestamp']
    for x in range(len(tamanho_do_json)):
        somar_volume, avg_vol = 0, 0
        fechamento = resposta.json()['chart']['result'][0]['indicators']['quote'][0]['close'][x]
        abertura = resposta.json()['chart']['result'][0]['indicators']['quote'][0]['open'][x]
        volume = resposta.json()['chart']['result'][0]['indicators']['quote'][0]['volume'][x]
        baixa = resposta.json()['chart']['result'][0]['indicators']['quote'][0]['low'][x]
        alta = resposta.json()['chart']['result'][0]['indicators']['quote'][0]['high'][x]
        for y in range(89):
            try:
                somar_volume = resposta.json()['chart']['result'][0]['indicators']['quote'][0]['volume'][x+y]
                avg_vol += somar_volume
            except:
                pass
        lista_montar.append([fechamento, abertura, volume, baixa, alta, avg_vol])
        #print(f'fechamento:{fechamento} abertura: {abertura} volume: {volume} baixa: {baixa} alta: {alta}')



def find_line_by_date(soup, date, tag):
    for index in range(1, len(soup)+1, 1):
        new = soup[index].find(tag).text
        if new == date:
            return soup[index]
            
def soup_url(stock, tempo=60, brasileira=True):
    #tempo calculado em dias com 60 dias padronizado
    contador,contador_de_erro = 0, 0
    resultado_dos_dias = []
    if brasileira == True:
        start_url = f"https://finance.yahoo.com/quote/{stock}.SA/history?p={stock}.SA"
    else:
        start_url = f'https://finance.yahoo.com/quote/{stock}/history?p={stock}'
    browser = BeautifulSoup(get(start_url).content, "html.parser")
    base = browser.findAll('tr')
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
    return resultado_dos_dias

resultado = soup_url('movi3')
print(resultado)
