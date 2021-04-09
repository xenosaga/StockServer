from flask import jsonify, request
from . import api
from .. import db
from .stock import parse_insert, parse_query

@api.route('/', methods=['GET', 'POST'])
def main():
    res = {}
    res['status'] = 'OK'
    return jsonify(res)

@api.route('/insert/<action>/<stock_num>', methods=['GET', 'POST'])
def insert_div(action, stock_num):
    data = request.json
    print(data)
    res = parse_insert(action, stock_num, data)

    print(res)
    return res

@api.route('/query/<action>/<stock_num>', methods=['GET', 'POST'])
def query(action, stock_num):
    res = {}
    data = request.json
    print(data)

    res['action'] = action
    res['stock_num'] = stock_num
    res = parse_query(action, stock_num, {})
    print(res)

    return res