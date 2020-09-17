from flask import Flask, jsonify
from flask_restful import Api, Resource
from scraping.scraping_stock import tratamento_acao


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
        return jsonify(tratamento_acao(stock, brasileira=True))
api.add_resource(get_stock,'/br/<string:stock>')

class get_usa_stock(Resource):
    def get(self, stock):
        self.stock = stock
        return jsonify(tratamento_acao(stock, brasileira=False))
api.add_resource(get_usa_stock,'/usa/<string:stock>')


if __name__ == "__main__":
    app.run()
