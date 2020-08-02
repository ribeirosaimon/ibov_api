from scraping.soup import soup_url, avg_vol, calculo_do_ifr, calculo_media_movel
from scraping.date_tratament import dataIso

def tratamento_acao(stock):
    acao = soup_url(stock)
    data = dataIso()

    ultima_cotacao = acao[0]
    if len(acao[0]) != len(acao[1]):
        ultima_cotacao = acao[1]
        acao = acao[1:]


    ifr = calculo_do_ifr(acao)
    media_movel = calculo_media_movel(acao)


    abertura = float(ultima_cotacao[1])
    maxima = float(ultima_cotacao[2])
    minima = float(ultima_cotacao[3])
    fechamento = float(ultima_cotacao[4])
    preco_atual = float(ultima_cotacao[5])
    volume = float(ultima_cotacao[6].replace(',',''))
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
        'mov_avg':float(media_movel),
        }
    }
    return json_retorno
