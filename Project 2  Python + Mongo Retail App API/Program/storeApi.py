from werkzeug.wrappers import request, Response
from flask import Flask, jsonify, request
from store import getProducts, allsoap, allshampoo


app = Flask(__name__)
@app.route('/store', methods = ['GET', 'POST'])
def home():
    if(request.method == 'GET'):
        return getProducts()

@app.route('/soap', methods = ['GET', 'POST'])
def soap():
    if(request.method == 'GET'):
        return allsoap()

@app.route('/shampoo', methods = ['GET', 'POST'])
def shampoo():
    if(request.method == 'GET'):
        return allshampoo()

if __name__ == '__main__':
  from werkzeug.serving import run_simple
  run_simple('localhost', 9000, app)