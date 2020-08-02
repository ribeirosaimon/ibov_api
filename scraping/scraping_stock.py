from scraping.soup import *
from scraping.date_tratament import dataIso

def tratamento_acao(stock):
    acao = soup_url(stock)
    ultima_cotacao = acao[0]

    if len(acao[0]) != len(acao[1]):
        ultima_cotacao = acao[1]
        acao = acao[1:]

    data = dataIso(acao[0][0])
    ifr = calculo_do_ifr(acao)
    media_movel = calculo_media_movel(acao)
    topo_e_fundo = ultimo_topo_e_fundo_da_acao(acao)

    topo = float(topo_e_fundo[0][2])
    fundo = float(topo_e_fundo[1][1])

    abertura = float(ultima_cotacao[1])
    maxima = float(ultima_cotacao[2])
    minima = float(ultima_cotacao[3])
    fechamento = float(ultima_cotacao[4])
    preco_atual = float(ultima_cotacao[5])
    volume = float(ultima_cotacao[6].replace(',',''))
    volume_medio = avg_vol(stock)
    porcentagem_do_topo = round(abs((topo / preco_atual) - 1) * 100, 2)
    porcentagem_do_fundo = round(abs((preco_atual / fundo) - 1) * 100, 2)

    json_retorno = {
       f"{stock}":{
          "technical_analysis":{
             "rsi":float(ifr),
             "mov_avg":float(media_movel),
             'last_top':topo,
             '%_last_top':porcentagem_do_topo,
             'last_bottom':fundo,
             '%_last_bottom':porcentagem_do_fundo
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
