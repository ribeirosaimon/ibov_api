import unittest
from scraping.scrap_stocks import Stock


class MyTest(unittest.TestCase):

    def testando_o_preco_de_volume(self, name_stock='movi3'):
        acao = Stock(name_stock)
        acao = acao[name_stock]
        assert isinstance(acao['vol'], float)
    def testando_o_preco_de_avg_vol(self, name_stock='movi3'):
        acao = Stock(name_stock)
        acao = acao[name_stock]
        assert isinstance(acao['avg_vol'], float)
    def testando_o_preco_de_abertura(self, name_stock='movi3'):
        acao = Stock(name_stock)
        acao = acao[name_stock]
        assert isinstance(acao['open'], float)
    def testando_o_preco_de_fechamento(self, name_stock='movi3'):
        acao = Stock(name_stock)
        acao = acao[name_stock]
        assert isinstance(acao['close'], float)
    def testando_o_preco_de_minima(self, name_stock='movi3'):
        acao = Stock(name_stock)
        acao = acao[name_stock]
        assert isinstance(acao['low'], float)
    def testando_o_preco_de_maxima(self, name_stock='movi3'):
        acao = Stock(name_stock)
        acao = acao[name_stock]
        assert isinstance(acao['high'], float)
    def testando_o_preco_de_adj_close(self, name_stock='movi3'):
        acao = Stock(name_stock)
        acao = acao[name_stock]
        assert isinstance(acao['adj_close'], float)
    def testando_o_preco_de_adj_close(self, name_stock='movi3'):
        acao = Stock(name_stock)
        acao = acao[name_stock]
        assert isinstance(acao['currecy'], str)

if __name__ == '__main__':
    unittest.main()
'''


            'date':dataIso(),
  
            'high':float(td_stock[2]),
 


'''