from scraping.soup import *
from scraping.date_tratament import dataIso, data_atual

def tratamento_acao(stock, brasileira=True):
    acao = soup_url(stock, brasileira=brasileira)
    ultima_cotacao = acao[0]
    hilo = indicador_hightlow(acao)
    media_hilo = hilo[1]
    call_hilo = hilo[0]
    data = data_atual()
    ifr = calculo_do_ifr(acao)
    media_movel = calculo_media_movel(acao)
    referencia, referencia_preco = ultimo_topo_e_fundo_da_acao(acao)
    bollinger_band = bandas_de_bollinger(acao)
    abertura = float(ultima_cotacao[3])
    maxima = float(ultima_cotacao[1])
    minima = float(ultima_cotacao[2])
    fechamento = float(ultima_cotacao[0])
    preco_atual = float(ultima_cotacao[0])
    volume = float(ultima_cotacao[4])
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
          }
       }
    }
    return json_retorno
