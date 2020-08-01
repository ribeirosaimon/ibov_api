from requests import get
from bs4 import BeautifulSoup
from scraping.date_tratament import date_treatment
import time

def find_line_by_date(soup, date, tag):
    for index in range(1, len(soup)+1, 1):
        new = soup[index].find(tag).text
        if new == date:
            return soup[index]

def soup_url(stock):
    start_url = f"https://finance.yahoo.com/quote/{stock}.SA/history?p={stock}.SA"
    browser = BeautifulSoup(get(start_url).content, "html.parser")
    time.sleep(0.5)
    base = browser.findAll('tr')
    span_in_line = find_line_by_date(base, date_treatment(), 'td').find_all('span')
    data = [element.text for element in span_in_line]
    calculo_de_analises(base)
    return [data, round(retorno_ifr,2), soma_media_movel]


def avg_vol(stock):
    r = f'https://finance.yahoo.com/quote/{stock}.SA'
    time.sleep(0.5)
    browser = BeautifulSoup(get(r).content, 'lxml')
    soup = browser.find('td', {'data-test': 'AVERAGE_VOLUME_3MONTH-value'})
    try:
        avg_vol = float(soup.text.replace(',', ''))
    except:
        avg_vol = 0.0
    return float(avg_vol)


def calculo_de_analises(base, tempo=20):
    #tempo Padrao de 14 Dias
    lista_acao_fechamento_alta,lista_acao_fechamento_baixa, media_movel = [], [], []
    soma_da_media_alta, soma_da_media_baixa, soma_media_movel = 0, 0, 0
    for x in range(tempo):
        try:
            span_in_line = find_line_by_date(base, date_treatment(x), 'td').find_all('span')
            ifr = [element.text for element in span_in_line]
            abertura = float(ifr[1])
            fechamento = float(ifr[4])
            if fechamento >= abertura:
                calculo = fechamento - abertura
                lista_acao_fechamento_alta.append(round(calculo,2))
                media_movel.append(round(fechamento,2))
            if fechamento < abertura:
                calculo = abertura - fechamento
                lista_acao_fechamento_baixa.append(round(calculo,2))
                media_movel.append(round(fechamento,2))
        except Exception as e:
            pass
        media_calculo_ifr = ((sum(lista_acao_fechamento_alta)/14) / (sum(lista_acao_fechamento_baixa)/14))
        soma_media_movel = round((sum(media_movel) / len(media_movel)),2)
        try:
            retorno_ifr = 100-(100/(1+media_calculo_ifr))
        except Exception as e:
            retorno_ifr = 0
            print(e)
    return [retorno_ifr, soma_media_movel]
