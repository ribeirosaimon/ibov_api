from requests import get
from bs4 import BeautifulSoup
from scraping.date_tratament import date_treatment
import time

def find_line_by_date(soup, date, tag):
    for index in range(1, len(soup)+1, 1):
        new = soup[index].find(tag).text
        if new == date:
            return soup[index]

class Acao:
    def __init__(self,)

    


    def soup_url(stock, tempo=1):
        #tempo calculado em dias
        contador = 0
        resultado_dos_dias = []
        start_url = f"https://finance.yahoo.com/quote/{stock}.SA/history?p={stock}.SA"
        browser = BeautifulSoup(get(start_url).content, "html.parser")
        base = browser.findAll('tr')
        #pegando as informações dos dias que foi passado no soup
        while tempo != len(resultado_dos_dias):
            try:
                span_in_line = find_line_by_date(base, date_treatment(contador), 'td').find_all('span')
                data = [element.text for element in span_in_line]
                resultado_dos_dias.append(data)
            except Exception as e:
                pass
            contador +=1
        return resultado_dos_dias


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

    #[['abc3',123,123,123,123],['asdc',123,123,123,1]]
    def calculo_do_ifr(lista):
        #tempo Padrao de 14 Dias
        lista_acao_fechamento_alta,lista_acao_fechamento_baixa = [], []
        soma_da_media_alta, soma_da_media_baixa,  = 0, 0
        for dados in lista:
            try:
                abertura = float(dados[1])
                fechamento = float(dados[4])
                if fechamento >= abertura:
                    calculo = fechamento - abertura
                    lista_acao_fechamento_alta.append(round(calculo,2))
                if fechamento < abertura:
                    calculo = abertura - fechamento
                    lista_acao_fechamento_baixa.append(round(calculo,2))
            except Exception as e:
                print(e)
            media_calculo_ifr = ((sum(lista_acao_fechamento_alta)/14) / (sum(lista_acao_fechamento_baixa)/14))
            try:
                retorno_ifr = 100-(100/(1+media_calculo_ifr))
            except Exception as e:
                retorno_ifr = 0
                print(e)
        return round(retorno_ifr,2)



    def calculo_media_movel(lista):
        media_movel = []
        soma_media_movel = 0
        for dados in lista:
            try:
                abertura = float(dados[1])
                fechamento = float(dados[4])
                if fechamento >= abertura:
                    media_movel.append(round(fechamento,2))
                if fechamento < abertura:
                    media_movel.append(round(fechamento,2))
            except Exception as e:
                print(e)
            soma_media_movel = round((sum(media_movel) / len(media_movel)),2)

        return soma_media_movel
