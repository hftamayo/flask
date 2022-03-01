from flask import Flask, render_template, abort, jsonify

from model import data

app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template("welcome.html", cards=data)

@app.route("/cards/<int:index>")
def card_view(index):
    try:
        card = data[index]
        return render_template("cards.html", card=card, index=index, max_index=len(data)-1)
    except IndexError:
        abort(404)

@app.route("/api/card")
def api_card_list():
    return jsonify(data)

@app.route("/api/card/<int:index>")
def api_card_detail(index):
    try:
        return data[index]
    except IndexError:
        abort(404)