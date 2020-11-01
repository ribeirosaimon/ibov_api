from flask import Flask, jsonify
from flask_restful import Api, Resource
from scraping.soup_poo import Stock


app = Flask(__name__)
api = Api(app)


class home(Resource):
    def get(self):
        return {'First type the country':'br or usa',
                'after type the ticket stock':'petr4 or fb',
                'exemple':'br/petr4 or usa/fb'}
api.add_resource(home,'/')

class get_stock(Resource):
    def get(self, stock):
        self.stock = stock
        acao = Stock(stock, brasileira=True)
        acaobr = acao.tratamento_final()
        return jsonify(acaobr)
api.add_resource(get_stock,'/br/<string:stock>')

class get_usa_stock(Resource):
    def get(self, stock):
        self.stock = stock
        acao = Stock(stock, brasileira=False)
        acaousa = acao.tratamento_final()
        return jsonify(acaousa)
api.add_resource(get_usa_stock,'/usa/<string:stock>')


if __name__ == "__main__":
    app.run()
