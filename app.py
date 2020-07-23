from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from scraping.scrap_stocks import Stock

app = Flask(__name__)
api = Api(app)

class get_stock(Resource):
    def get(self, stock):
        return Stock(stock)

api.add_resource(get_stock,'/<string:stock>')

if __name__ == "__main__":
    app.run()
