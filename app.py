from flask import Flask, jsonify
from flask_restful import Api, Resource
from scraping.scraping_stock import tratamento_acao

app = Flask(__name__)
api = Api(app)


class get_stock(Resource):
    def get(self, stock):
        self.stock = stock
        return jsonify(tratamento_acao(stock))
api.add_resource(get_stock,'/<string:stock>')


if __name__ == "__main__":
    app.run()
