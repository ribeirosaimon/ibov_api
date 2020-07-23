import unittest
from scraping.scrap_stocks import scrap_stocks


class MyTest(unittest.TestCase):
  acao = scrap_stocks('movi3')
  def testando_o_preco_de_volume(self,acao):
      self.isinstance(acao['avg_vol'], int)
  def testando_o_preco_de_fechamento(self,acao):
      self.isinstance(acao['close'], int)
  def testando_o_preco_de_abertura(self,acao):
      self.isinstance(acao['open'], int)
  def testando_o_preco_de_maxima(self,acao):
      self.isinstance(acao['high'], int)
