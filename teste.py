from scraping.soup import soup_url, calculo_media_movel
from scraping.date_tratament import date_treatment, dataIso
from scraping.scraping_stock import tratamento_acao

stock = 'oibr3'
acao = tratamento_acao(stock)
print(acao)
