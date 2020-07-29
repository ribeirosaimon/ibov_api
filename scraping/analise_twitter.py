import tweepy
from scraping.date_tratament import date_tweet_sentiment_mes_anterior
from scraping.string_tratament import tratamento_texto
from analise_twitter.keys import *

#Tokens de acesso
consumer_key= CONSUMER_KEY
consumer_secret= CONSUMER_SECRET
acess_token = ACESS_TOKEN
access_token_secret= ACESS_TOKEN_SECRET


#Autenticando
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(acess_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)


def analisando_acao_twitter(stock):
    lista_de_tweets = []
    data_atual = str(date_tweet_sentiment_mes_anterior())
    tweets_do_dia = tweepy.Cursor(api.search, q=f"{stock}", since = data_atual,lang="pt").items()
    for tweet in tweets_do_dia:
        lista_de_tweets.append(tratamento_texto(tweet.text))
        print(len(lista_de_tweets))
    return ' '.join(lista_de_tweets)

def quantidades_de_tweets(stock):
    lista_de_tweets = []
    data_atual = str(date_tweet_sentiment_mes_anterior())
    tweets_do_mes = tweepy.Cursor(api.search, q=f"{stock}", since = data_atual,lang="pt").items()
    for tweet in tweets_do_mes:
        lista_de_tweets.append(tratamento_texto(tweet.text))
    return {f'{stock}':len(lista_de_tweets)}
