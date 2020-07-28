import tweepy
from textblob import TextBlob
from scraping.date_tratament import date_tweet_sentiment
from scraping.string_tratament import tratamento_texto

#Tokens de acesso
consumer_key= 'xKz9EpTCHhzP3HVTwFj4dS84W'
consumer_secret= '6HOp6DlBqri9AQQxOHm9H3Yhwk2uZYRPA6n6bOHvvTwgxwb2iF'
acess_token = '1140787860519477249-AkkrhbiBI9ubRz4JJyuvE3RDRcruLL'
access_token_secret='4UXrFAw3PQc4nyW2mnWa7ChJs51ZSvMpHirg8CgaSZzbe'


#Autenticando
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(acess_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)


stock = 'movi3'
data_atual = str(date_tweet_sentiment())
tweets_do_dia = tweepy.Cursor(api.search, q=f"{stock}", since = data_atual,lang="pt").items(100)
quantidade_de_tweets_do_dia = len([tweets_do_dia])
lista_de_tweets = []

for tweet in tweets_do_dia:
    lista_de_tweets.append(tratamento_texto(tweet.text))

print(lista_de_tweets)
