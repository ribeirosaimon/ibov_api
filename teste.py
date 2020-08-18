from scraping.soup import soup_url, calculo_media_movel, ultimo_topo_e_fundo_da_acao, indicador_hightlow
from scraping.date_tratament import date_treatment, dataIso
from scraping.scraping_stock import tratamento_acao
from scraping.acoes_ibov import LISTA
from pylightxl import open_workbook

book = open_workbook('crono_2020.xlsx',on_demand=True)

for name in book.sheet_names():
    print(name)
