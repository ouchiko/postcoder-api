from app import app
from flask import render_template
from flask import request
from flask import url_for
from postcode_search import PostcodeSearch
from flask import jsonify

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/postcode/<string:partial_postcode>')
def pricemax(partial_postcode):
    pc = PostcodeSearch("app/datasrc/opennames.db");
    status = pc.setPostcode(partial_postcode)
    if status == True:
        response = pc.search()
        return jsonify(response)
    else:
        return jsonify(status)

with app.test_request_context():
    print url_for('static', filename='app.css')
    print url_for('static', filename='app.js')
