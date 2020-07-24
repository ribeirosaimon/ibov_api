import unittest
from scraping.date_tratament import date_treatment
from scraping_stock import tratamento_acao

stock = 'movi3'
acao = tratamento_acao(stock)


class MyTest(unittest.TestCase):
    def testando_abertura_da_acao(self):
        self.assertIsInstance(acao[stock]['open'], float)

    def testando_fechamento_da_acao(self):
        self.assertIsInstance(acao[stock]['close'], float)

    def testando_maxima_da_acao(self):
        self.assertIsInstance(acao[stock]['high'], float)

    def testando_minima_da_acao(self):
        self.assertIsInstance(acao[stock]['low'], float)

    def testando_avgVol_da_acao(self):
        self.assertIsInstance(acao[stock]['avg_vol'], float)

    def testando_vol_da_acao(self):
        self.assertIsInstance(acao[stock]['vol'], float)

    def testando_preco_atual_da_acao(self):
        self.assertIsInstance(acao[stock]['adj_close'], float)

    def testando_a_data(self):
        self.assertEqual(date_treatment(), 'Jul 24, 2020')


if __name__ == '__main__':
    unittest.main()
