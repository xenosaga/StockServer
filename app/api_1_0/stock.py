import datetime
from .. import db
from ..models import Stock_Dividen, Stock_Status

def parse_query(action, stock, data):
    print('parse query')
    res = {}
    if(action == 'per'):
        res = query_profit(stock, data)
    elif(action == 'perr'):
        res = query_profit_range(stock, data)
    return res

def query_profit_range(stock, data):
    res = {}
    rs = Stock_Status.query.filter(per >= data['per']).all()
    for row in rs:
        r_row = {}
        r_row['stock_num'] = row.stock_num
        r_row['per'] = row.per
        res.append(r_row)
    print(res)
    return res

def query_profit(stock, data):
    res = {}
    rs = Stock_Status.query.filter_by(stock_num=stock).first()
    if(rs is None):
        res['per'] = 'TBD'
        res['date'] = 'None'
    else:
        res['per'] = rs.per
        res['date'] = rs.last_update

    return res

def parse_insert(action, stock, data):
    res = {}
    if(action == 'div'):
        res = insert_div(stock, data['data'])
    elif(action == 'status'):
        res = insert_status(stock, data)
    elif(action == 'test'):
        res = test(stock, data)
    return res

    
def insert_div(stock, data):
    # clear old data
    Stock_Dividen.delete_by_stock_num(stock)

    # insert data
    for item in data:
        print(item)
        sd = Stock_Dividen()
        sd.stock_num = item['stock_num']
        sd.div_date = item['div_date']
        sd.div_price = item['div_price']
        sd.div_amount = item['div_amount']
        sd.div_precent = item['div_precent']
        db.session.add(sd)
        db.session.commit()

    return 'OK'

def insert_status(stock, data):
    sd = Stock_Status.query.filter_by(stock_num=stock).first()
    if(sd is None):
        sd = Stock_Status()
        sd.stock_num = stock
    sd.last_date = data['last_date']
    sd.per = data['per']
    sd.last_update = datetime.datetime.utcnow()
    print(data)
    db.session.add(sd)
    db.session.commit()
    return 'OK'

def delect_all(stock):
    sd = Stock_Dividen.delete().where(stock_num=stock)
    db.session.delete(sd)
    db.session.commit()

def test(dtock, data):
    sd = Stock_Dividen()
    sd.stock_num = 2330
    sd.div_price = 230
    sd.div_amount = 2.5
    sd.div_date = datetime.datetime(2009, 5, 20)
    sd.div_precent = 2.5/230

    db.session.add(sd)
    db.session.commit()