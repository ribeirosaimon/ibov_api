import json
from scraping.soup import soup_url, avg_vol
from scraping.date_tratament import dataIso

def tratamento_acao(stock):
    acao = soup_url(stock)
    data = dataIso()
    abertura = float(acao[1])
    maxima = float(acao[2])
    minima = float(acao[3])
    fechamento = float(acao[4])
    preco_atual = float(acao[5])
    volume = float(acao[6].replace(',',''))
    volume_medio = avg_vol(stock)
    json_retorno = {f'{stock}':
    {
        'currecy':'R$',
        'date':data,
        'open':abertura,
        'high':maxima,
        'low':minima,
        'close':fechamento,
        'adj_close':preco_atual,
        'vol':volume,
        'avg_vol':volume_medio
        }
    }
    return json(json_retorno)
