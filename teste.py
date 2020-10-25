from scraping.date_tratament import *
from scraping.soup import *
from scraping.scraping_stock import *
from requests import get
from bs4 import BeautifulSoup
import time
import requests


retorno = bandas_de_bollinger(soup_url('mu',brasileira=False))
print(retorno)

