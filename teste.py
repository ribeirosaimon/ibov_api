from scraping.date_tratament import *
from scraping.soup import *
from scraping.scraping_stock import *
from requests import get
from bs4 import BeautifulSoup
import time
import requests


def teste_endpoint(br, acao):
    endpoint_teste = f'http://127.0.0.1:5000/{br}/{acao}'
    retorno = requests.get(endpoint_teste).json()
    print(retorno)


retorno = bandas_de_bollinger(soup_url('mu',brasileira=False))
print(retorno)