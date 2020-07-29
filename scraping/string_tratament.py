from nltk import tokenize
import matplotlib.pyplot as plt
from scraping.palavras_irrelevantes import PALAVRAS_IRRELEVANTES

def tratamento_texto(texto):
    lista_de_tweets = []
    token_espaco = tokenize.WhitespaceTokenizer()
    token_frase = token_espaco.tokenize(texto)
    for palavra in token_frase:
        if palavra not in PALAVRAS_IRRELEVANTES:
            lista_de_tweets.append(palavra.lower())
    for novas_palavras in lista_de_tweets:
        if 'htt' in novas_palavras:
            lista_de_tweets.remove(novas_palavras)
        if 2 >= len(novas_palavras) <= 20:
            lista_de_tweets.remove(novas_palavras)
    return ' '.join(lista_de_tweets)
