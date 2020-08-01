from scraping.soup import soup_url, avg_vol, calculo_do_ifr, calculo_media_movel
from scraping.date_tratament import dataIso

def tratamento_acao(stock, tempo=14):
    acao = soup_url(stock, tempo)
    ifr = calculo_do_ifr(acao)
    media_movel = calculo_media_movel(acao)
    ultima_cotacao = acao[0]
    data = dataIso()

    try:
        abertura = float(ultima_cotacao[1])
    except:
        abertura = 0.0

    try:
        maxima = float(ultima_cotacao[2])
    except:
        maxima = 0.0

    try:
        minima = float(ultima_cotacao[3])
    except:
        minima = 0.0

    try:
        fechamento = float(ultima_cotacao[4])
    except:
        fechamento = 0.0

    try:
        preco_atual = float(ultima_cotacao[5])
    except:
        preco_atual = 0.0


    try:
        volume = float(ultima_cotacao[6].replace(',',''))
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
        'rsi':float(ifr),
        'mov_avg':float(media_movel)
        }
    }
    return json_retorno
