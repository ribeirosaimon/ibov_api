from scraping.soup import soup_url, calculo_media_movel, ultimo_topo_e_fundo_da_acao
from scraping.date_tratament import date_treatment, dataIso
from scraping.scraping_stock import tratamento_acao
from scraping.acoes_ibov import LISTA








stock = 'movi3'
acao = tratamento_acao(stock)
print(acao)
