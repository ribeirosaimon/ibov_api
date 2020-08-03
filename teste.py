from scraping.soup import soup_url, calculo_media_movel, ultimo_topo_e_fundo_da_acao
from scraping.date_tratament import date_treatment, dataIso
from scraping.scraping_stock import tratamento_acao


stock = 'vvar3'
acao = soup_url(stock)
ultima_deteccao = ultimo_topo_e_fundo_da_acao(acao)
print(ultima_deteccao)
