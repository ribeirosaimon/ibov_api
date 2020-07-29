import tweepy
from scraping.date_tratament import date_tweet_sentiment
from scraping.string_tratament import tratamento_texto
from analise_twitter import keys

#Tokens de acesso
consumer_key= CONSUMER_KEY
consumer_secret= CONSUMER_SECRET
acess_token = ACESS_TOKEN
access_token_secret= ACESS_TOKEN_SECRET


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

todas_palavras = ' '.join(lista_de_tweets)



print(todas_palavras)
