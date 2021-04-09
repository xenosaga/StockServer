from . import db
from datetime import datetime

class Stock_Dividen(db.Model):
    __tablename__ = 'stock_dividen'
    index = db.Column(db.Integer, primary_key=True)
    stock_num = db.Column(db.Integer)
    div_date = db.Column(db.DateTime)
    div_price = db.Column(db.Float)
    div_amount = db.Column(db.Float)
    div_precent = db.Column(db.Float)

    @classmethod
    def delete_by_stock_num(cls, stock):
        cls.query.filter(cls.stock_num == stock).delete()
        db.session.commit()

    def __repr__(self):
        return '<Stock dividen %r>' % str(self.stock_num)

class Stock_Status(db.Model):
    __tablename__ = 'stock_status'
    stock_num = db.Column(db.Integer, primary_key=True)
    per = db.Column(db.Float)
    last_date = db.Column(db.Date)
    last_update = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return '<Stock status %r>' % str(self.stock_num)