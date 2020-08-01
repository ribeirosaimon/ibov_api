from scraping.soup import soup_url
from scraping.date_tratament import date_treatment
from scraping.scraping_stock import tratamento_acao
import datetime
import json
import requests
import time

acoes = ['movi3','oibr3','wege3','ptbl3','jslg3','ECOR3','egie3','rent3','cyre3','suzb3','ccro3', 'mrfg3','elet6','cmig4','petr4','enev3','pomo4']


def get_api(stock):
    stock = stock
    api = 'https://secure-wildwood-34847.herokuapp.com'
    resposta = requests.request('GET', api + f'/{stock}')
    time.sleep(1)
    acao = resposta.json()
    dados_acao = acao[stock]
    nome_acao = stock
    adj_close = acao[stock]['adj_close']
    avg_vol = acao[stock]['avg_vol']
    vol = acao[stock]['vol']
    high = acao[stock]['high']
    low = acao[stock]['low']
    mov_avg = acao[stock]['mov_avg']
    rsi = acao[stock]['rsi']
    return [nome_acao, adj_close, high, low, avg_vol, vol, mov_avg, rsi]

for x in acoes:
    try:
        retorno = get_api(x)
        if retorno[6]>retorno[1]:
            print(f'A Ação {x} esta com a media movel abaixo do fechamento do pregao')
        if 30 < retorno[7] > 70:
            print(f'A Ação {x} esta com O Inidice de força relativa de {retorno[7]}')
    except:
        print(f'Ocorreu algum erro com a ação {x}')
