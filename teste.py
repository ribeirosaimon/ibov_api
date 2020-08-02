from scraping.soup import soup_url, ultimo_topo_da_acao, ultimo_fundo_da_acao, calculo_media_movel
from scraping.date_tratament import date_treatment
from scraping.scraping_stock import tratamento_acao
import datetime
import json
import requests
import time


acao = tratamento_acao('movi3')
print(acao)
