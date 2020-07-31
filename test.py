import unittest
from scraping.soup import soup_url, avg_vol
from scraping.date_tratament import date_treatment


stock = str(input('Digite o Nome da Ação que queira Testar: '))

acao = soup_url(stock)
ifr = acao[1]
acao = acao[0]
volume = float(acao[6].replace(',',''))

class MyTest(unittest.TestCase):
    def testando_abertura_da_acao(self):
        self.assertIsInstance(float(acao[1]), float)

    def testando_fechamento_da_acao(self):
        self.assertIsInstance(float(acao[4]), float)

    def testando_maxima_da_acao(self):
        self.assertIsInstance(float(acao[2]), float)

    def testando_minima_da_acao(self):
        self.assertIsInstance(float(acao[3]), float)

    def testando_avg_vol_da_acao(self):
        self.assertIsInstance(avg_vol(stock), float)

    def testando_vol_da_acao(self):
        self.assertIsInstance(volume, float)

    def testando_preco_atual_da_acao(self):
        self.assertIsInstance(float(acao[5]), float)

    def testando_a_data(self):
        self.assertEqual(date_treatment(), acao[0])

    def testando_o_rsi(self):
        self.assertIsInstance(ifr, float)


if __name__ == '__main__':
    unittest.main()
    print(type(ifr))
