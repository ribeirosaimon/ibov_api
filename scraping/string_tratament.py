from nltk import tokenize
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from scraping.palavras_irrelevantes import PALAVRAS_IRRELEVANTES

def tratamento_texto(texto):
    lista_de_palavras = []
    token_espaco = tokenize.WhitespaceTokenizer()
    token_frase = token_espaco.tokenize(texto)
    for palavra in token_frase:
        if palavra not in PALAVRAS_IRRELEVANTES:
            lista_de_palavras.append(palavra)
    return lista_de_palavras



'''
nuvem_palavras = WordCloud(width = 800, height = 500, max_font_size = 110,
                          collocations = False).generate(todos_palavras)
plt.figure(figsize= (10, 7))
plt.imshow(nuvem_palavras, interpolation = 'bilinear')
plt.axis('off')
plt.show()
'''
