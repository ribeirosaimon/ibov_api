from flask import Flask, request, jsonify
from scraping.scrap_stocks import scrap_stocks

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/<stock>", methods=['GET'])
def stocks(stock):
    try:
        return scrap_stocks(stock)

    except Exception as e:
        return e


if __name__ == "__main__":
    app.run(debug=True)
