from requests import get
from bs4 import BeautifulSoup
from scraping.date_tratament import *
import time
import requests



class Stock:
    def __init__(self, stock, brasileira=True):
        self.stock = stock
        self.brasileira = brasileira


    def inicializando(self):
        if self.brasileira == True:
            stock = f'{self.stock}.sa'
        else:
            stock = self.stock
        
        lista_montada = []
        tempo = 60            
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


    def avg_vol(self):
        if self.brasileira == True:
            stock = f'{self.stock}.sa'
        else:
            stock = self.stock
        endpoint = f'https://query1.finance.yahoo.com/v10/finance/quoteSummary/{stock}?modules=summaryDetail%2CearningsHistory'
        resposta = requests.request('GET', endpoint)
        resposta = float(resposta.json()['quoteSummary']['result'][0]['summaryDetail']['averageVolume']['raw'])
        return resposta

    def calculo_do_ifr(self, lista, tempo=14):
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

    def calculo_media_movel(self, lista, tempo=14):
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
        

    def ultimo_topo_e_fundo_da_acao(self, lista, candles=2):
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

    def indicador_hightlow(self, lista, candles=3):
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

    def bandas_de_bollinger(self, lista, candles=20, desvio_padrao=2):
        lista = lista[0:candles]
        middle,desvio_padrao = 0,0
        call_bollinger = 'none'
        for close_price in lista:
            middle += float(close_price[0])
        middle_bollinger = round(middle / candles, 2)
        for x in lista:
            squared = (float(x[0]) - middle_bollinger)
            desvio_padrao += squared ** 2
        desvio_padrao_bollinger = (desvio_padrao / candles) ** 0.5
        up_bollinger = round(middle_bollinger + (2 * desvio_padrao_bollinger),2)
        lower_bollinger = round(middle_bollinger - (2 * desvio_padrao_bollinger),2)
        for valor in lista:
            fechamento = valor[0]
            if fechamento > up_bollinger:
                call_bollinger = 'sell'
            if fechamento < lower_bollinger:
                call_bollinger = 'buy'
        return lower_bollinger, middle_bollinger, up_bollinger, call_bollinger

    def tratamento_final(self):
        acao = self.inicializando()
        cotacao_ultimo_dia = acao[1]
        ultima_cotacao = acao[0]
        hilo = self.indicador_hightlow(acao)
        media_hilo = hilo[1]
        call_hilo = hilo[0]
        data = data_atual()
        ifr = self.calculo_do_ifr(acao)
        media_movel = self.calculo_media_movel(acao)
        referencia, referencia_preco = self.ultimo_topo_e_fundo_da_acao(acao)
        bollinger_band = self.bandas_de_bollinger(acao)
        abertura = float(ultima_cotacao[3])
        maxima = float(ultima_cotacao[1])
        minima = float(ultima_cotacao[2])
        fechamento = float(ultima_cotacao[0])
        preco_atual = float(ultima_cotacao[0])
        volume = float(ultima_cotacao[4])
        volume_medio = self.avg_vol()
        procentagem_da_referencia = round(abs((referencia_preco / preco_atual) - 1) * 100, 2)
        json_retorno = {
        f"{self.stock}":{
            "technical_analysis":{
                "rsi":float(ifr),
                "mov_avg":float(media_movel),
                'reference': referencia,
                'price_reference': referencia_preco,
                '%_last_reference':procentagem_da_referencia,
                'call_hilo': call_hilo,
                'price_hilo':media_hilo,
                'lower_bollinger_band':bollinger_band[0],
                'middle_bollinger_band':bollinger_band[1],
                'upper_bollinger_band':bollinger_band[2],
                'bollinger_indicator':bollinger_band[3],

            },
            "fundamentalist_analysis":{
                "date":data,
                "open":abertura,
                "high":maxima,
                "low":minima,
                "close":fechamento,
                "adj_close":preco_atual,
                "vol":volume,
                "avg_vol":volume_medio,
                "last_day_price":float(cotacao_ultimo_dia[0])
            }
        }
        }
        return json_retorno