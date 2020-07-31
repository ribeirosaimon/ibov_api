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
    lista_acao_fechamento_alta = []
    lista_acao_fechamento_baixa = []
    soma_da_media_alta, soma_da_media_baixa = 0, 0
    start_url = f"https://finance.yahoo.com/quote/{stock}.SA/history?p={stock}.SA"
    browser = BeautifulSoup(get(start_url).content, "html.parser")
    time.sleep(0.5)
    base = browser.findAll('tr')
    span_in_line = find_line_by_date(base, date_treatment(), 'td').find_all('span')
    data = [element.text for element in span_in_line]
    for x in range(1,21):
        try:
            span_in_line = find_line_by_date(base, date_treatment(x), 'td').find_all('span')
            ifr = [element.text for element in span_in_line]
            abertura = float(ifr[1])
            fechamento = float(ifr[5])
            if fechamento >= abertura:
                calculo = fechamento - abertura
                lista_acao_fechamento_alta.append(round(calculo,2))
                #lista_acao_fechamento_alta.append(fechamento)

            if abertura > fechamento:
                calculo = abertura - fechamento
                lista_acao_fechamento_baixa.append(round(calculo,2))
                #lista_acao_fechamento_baixa.append(abertura)

        except Exception as e:
            pass
    soma_da_media_baixa = (sum(lista_acao_fechamento_baixa) - sum(lista_acao_fechamento_alta))/14

    try:
        retorno_ifr = 100-(100/(1+(soma_da_media_baixa)))
    except:
        retorno_ifr = 0
    print(retorno_ifr)
    return [data,float(retorno_ifr)]

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
