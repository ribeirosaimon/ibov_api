from flask import Flask, jsonify
from flask_restful import Api, Resource
from scraping.scraping_stock import tratamento_acao


app = Flask(__name__)
api = Api(app)


class home(Resource):
    def get(self):
        return {'message':'Digite o ticket da ação após o endereço do site: www.site.com.br/petr4'}
api.add_resource(home,'/')

class get_stock(Resource):
    def get(self, stock):
        self.stock = stock
        return jsonify(tratamento_acao(stock))
api.add_resource(get_stock,'/<string:stock>')

if __name__ == "__main__":
    app.run()
