from requests import get
from bs4 import BeautifulSoup
from scraping.date_tratament import date_treatment, date_timestamp_for_date_utc
import time
import requests


def soup_url(stock, brasileira=True, tempo=60):
    lista_montada = []
    if brasileira == True:
        stock = f'{stock}.sa'
    start_date, end_date = date_timestamp_for_date_utc()
    endpoint = f'https://query2.finance.yahoo.com/v8/finance/chart/{stock}?symbol={stock}&period1={end_date}&period2={start_date}&interval=1d&includePrePost=true&events=div%2Csplit'
    resposta = requests.request('GET', endpoint)
    tamanho_do_json = resposta.json()['chart']['result'][0]['timestamp']
    for x in range(len(tamanho_do_json)):
        try:
            fechamento = resposta.json()['chart']['result'][0]['indicators']['quote'][0]['close'][x]
            abertura = resposta.json()['chart']['result'][0]['indicators']['quote'][0]['open'][x]
            volume = resposta.json()['chart']['result'][0]['indicators']['quote'][0]['volume'][x]
            baixa = resposta.json()['chart']['result'][0]['indicators']['quote'][0]['low'][x]
            alta = resposta.json()['chart']['result'][0]['indicators']['quote'][0]['high'][x]
            fechamento = round(fechamento,2)
            abertura = round(abertura,2)
            baixa = round(baixa,2)
            alta = round(alta,2)
            lista_montada.append([fechamento, alta, baixa, abertura, volume])
        except:
            pass

    if len(lista_montada) < tempo:
        tempo = 0
    lista_montada = lista_montada[::-1][:tempo]
    return lista_montada


def avg_vol(stock, brasileira=True):
    if brasileira == True:
        stock = f'{stock}.sa'
    endpoint = f'https://query1.finance.yahoo.com/v10/finance/quoteSummary/{stock}?modules=summaryDetail%2CearningsHistory'
    resposta = requests.request('GET', endpoint)
    resposta = float(resposta.json()['quoteSummary']['result'][0]['summaryDetail']['averageVolume']['raw'])
    return resposta


#[['abc3',123,123,123,123],['asdc',123,123,123,1]]
def calculo_do_ifr(lista, tempo=14):
    #tempo Padrao de 14 Dias
    lista_acao_fechamento_alta,lista_acao_fechamento_baixa = [], []
    soma_da_media_alta, soma_da_media_baixa, retorno_ifr  = 0, 0, 0
    lista = lista[:tempo]
    for dados in lista:
        try:
            abertura = float(dados[3])
            fechamento = float(dados[0])
            if fechamento >= abertura:
                calculo = fechamento - abertura
                lista_acao_fechamento_alta.append(round(calculo,2))
            if fechamento < abertura:
                calculo = abertura - fechamento
                lista_acao_fechamento_baixa.append(round(calculo,2))
        except Exception as e:
            pass
    media_calculo_ifr = ((sum(lista_acao_fechamento_alta)/14) / (sum(lista_acao_fechamento_baixa)/14))
    try:
        retorno_ifr = 100-(100/(1+media_calculo_ifr))
    except Exception as e:
        retorno_ifr = 0
        print(e)
    return round(retorno_ifr,2)

def find_line_by_date(soup, date, tag):
    for index in range(1, len(soup)+1, 1):
        new = soup[index].find(tag).text
        if new == date:
            return soup[index]


def calculo_media_movel(lista, tempo=14):
    media_movel = []
    soma_media_movel = 0
    for x in range(tempo):
        try:
            fechamento = float(lista[x][0])
            media_movel.append(fechamento)
            soma_media_movel = round((sum(media_movel) / len(media_movel)),2)
        except Exception as e:
            pass
    return soma_media_movel

#[fechamento, alta, baixa, abertura, volume]

def ultimo_topo_e_fundo_da_acao(lista, candles=2):
    #O candle vai haver uma minima e uma maxima
    lista = lista[::-1]
    contador = 0
    topo = float(lista[0][1])
    fundo = float(lista[0][2])
    candle_referencia = [fundo, topo]
    retorno = ['',0]
    for dados in lista:
        maxima = float(dados[1])
        minima = float(dados[2])
        #se a maxima é maior que o ultimo candle de referencia é o novo topo
        if maxima > float(candle_referencia[1]):
            contador += 1
            if contador >= candles:
                topo = maxima
                candle_referencia = [minima, maxima]
                retorno = ['top',maxima]
        #caso ele perca a maxima, precisa perder em 2 candles
        if minima < float(candle_referencia[0]):
            contador += 1
            if contador >= candles:
                fundo = minima
                candle_referencia = [minima, maxima]
                retorno = ['bottom',minima]
    return retorno


def indicador_hightlow(lista, candles=3):
    lista_media_movel_maxima, lista_media_movel_minima = [], []
    for candle_dias in lista[0:candles]:
        lista_media_movel_maxima.append(candle_dias[1])
        lista_media_movel_minima.append(candle_dias[2])
    maxima_hilo = round(sum(lista_media_movel_maxima) / len(lista[0:candles]), 2)
    minima_hilo = round(sum(lista_media_movel_minima) / len(lista[0:candles]), 2)


    if float(lista[0][3]) < minima_hilo:
        return ['sell', maxima_hilo]
    if float(lista[0][3]) > minima_hilo:
        return ['buy', minima_hilo]
    if float(lista[0][3]) < maxima_hilo:
        return ['sell', minima_hilo]
    if float(lista[0][3]) > maxima_hilo:
        return ['buy', minima_hilo]

def bandas_de_bollinger(lista, candles=20, desvio_padrao=2):
    lista = lista[0:candles]
    middle,desvio_padrao = 0,0
    call_bollinger = 'none'
    for close_price in lista:
        middle += float(close_price[0])
    middle_bollinger = round(middle / candles, 2)
    for x in lista:
        squared = (float(x[0]) - middle_bollinger)
        desvio_padrao += abs(squared ** 2)
    desvio_padrao_bollinger = round(desvio_padrao / candles, 2)
    print(desvio_padrao_bollinger)
    up_bollinger = middle_bollinger + (2 * desvio_padrao_bollinger)
    lower_bollinger = middle_bollinger - (2 * desvio_padrao_bollinger)
    for valor in lista:
        fechamento = valor[0]
        if fechamento > up_bollinger:
            call_bollinger = 'sell'
        if fechamento < lower_bollinger:
            call_bollinger = 'buy'
    return lower_bollinger, middle_bollinger, up_bollinger, call_bollinger

        