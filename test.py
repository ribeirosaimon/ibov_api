import unittest
from scraping_stock import Stock

acao = 'movi3'

class MyTest(unittest.TestCase):
    def testando_o_volume_medio(self):
        assert isinstance(Stock.avg_vol(acao), float)

if __name__ == '__main__':
    unittest.main()
