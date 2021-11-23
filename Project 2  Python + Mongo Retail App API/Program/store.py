from pymongo import MongoClient
from flask import Flask, jsonify, request
from bson.json_util import dumps

def getProducts():
    client = MongoClient('mongodb://localhost:27017/', 27017)
    db = client['Retail']
    collection = db['store']
    products = collection.find()
    return dumps(products)

def allsoap():
    client = MongoClient('mongodb://localhost:27017/', 27017)
    db = client['Retail']
    collection = db['soap']
    products = collection.find()
    return dumps(products)

def allshampoo():
    client = MongoClient('mongodb://localhost:27017/', 27017)
    db = client['Retail']
    collection = db['shampoo']
    products = collection.find()
    return dumps(products)
