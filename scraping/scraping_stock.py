from scraping.soup import *
from scraping.date_tratament import dataIso
import requests

def tratamento_acao(stock, brasileira=True):
    acao = soup_url(stock, brasileira=brasileira)
    ultima_cotacao = acao[0]

    if len(acao[0]) != len(acao[1]):
        ultima_cotacao = acao[1]
        acao = acao[1:]

    hilo = indicador_hightlow(acao)
    media_hilo = hilo[1]
    call_hilo = hilo[0]
    data = dataIso(acao[0][0])
    ifr = calculo_do_ifr(acao)
    media_movel = calculo_media_movel(acao)
    referencia, referencia_preco = ultimo_topo_e_fundo_da_acao(acao)


    abertura = float(ultima_cotacao[1])
    maxima = float(ultima_cotacao[2])
    minima = float(ultima_cotacao[3])
    fechamento = float(ultima_cotacao[4])
    preco_atual = float(ultima_cotacao[5])
    volume = float(ultima_cotacao[6].replace(',',''))
    volume_medio = avg_vol(stock, brasileira=brasileira)
    procentagem_da_referencia = round(abs((referencia_preco / preco_atual) - 1) * 100, 2)

    json_retorno = {
       f"{stock}":{
          "technical_analysis":{
             "rsi":float(ifr),
             "mov_avg":float(media_movel),
             'reference': referencia,
             'price_reference': referencia_preco,
             '%_last_reference':procentagem_da_referencia,
             'call_hilo': call_hilo,
             'price_hilo':media_hilo,

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
          }
       }
    }
    return json_retorno
