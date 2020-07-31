from scraping.soup import soup_url, avg_vol
from scraping.date_tratament import dataIso

def tratamento_acao(stock):
    acao = soup_url(stock)
    ifr = acao[1]
    acao = acao[0]
    data = dataIso()
    print(ifr)

    try:
        abertura = float(acao[1])
    except:
        abertura = 0.0

    try:
        maxima = float(acao[2])
    except:
        maxima = 0.0

    try:
        minima = float(acao[3])
    except:
        minima = 0.0

    try:
        fechamento = float(acao[4])
    except:
        fechamento = 0.0

    try:
        preco_atual = float(acao[5])
    except:
        preco_atual = 0.0


    try:
        volume = float(acao[6].replace(',',''))
    except :
        volume = 0.0


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
        'avg_vol':volume_medio,
        'rsi':float(ifr)
        }
    }
    return json_retorno
