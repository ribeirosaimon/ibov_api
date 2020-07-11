from flask import Flask, request, jsonify
from scraping.date_tratament import date_treatment
from scraping.scrap_stocks import scrap_stocks

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/stock/<stock>", methods=['GET'])
def stocks(stock):
    try:
        return scrap_stocks(stock)
    except:
        return f'{error} not found'

if __name__ == "__main__":
    app.run()
