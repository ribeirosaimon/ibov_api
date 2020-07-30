from flask import Flask, jsonify
from flask_restful import Api, Resource
from scraping.scraping_stock import tratamento_acao
from scraping.analise_twitter import quantidades_de_tweets

app = Flask(__name__)
api = Api(app)

class get_stock(Resource):
    def get(self, stock):
        self.stock = stock
        return jsonify(tratamento_acao(stock))
api.add_resource(get_stock,'/<string:stock>')
'''
class get_stock_information(Resource):
    def get(self,stock):
        self.stock = stock
        return jsonify(quantidades_de_tweets(stock))
api.add_resource(get_stock_information,'/infotweet/<string:stock>')
'''
if __name__ == "__main__":
    app.run()
