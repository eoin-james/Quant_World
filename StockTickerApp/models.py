from flask_sqlalchemy import SQLAlchemy

# Extension
db = SQLAlchemy()


# Model
class TickerClass(db.Model):
    # id = db.Column(db.Integer, primary_key=True)
    # Date = db.Column(db.String(8), nullable=False, unique=False)
    DateTime = db.Column(db.String(8), nullable=False, unique=True, primary_key=True)
    AAPL = db.Column(db.Float)
    MSFT = db.Column(db.Float)
    TEAM = db.Column(db.Float)
    TSLA = db.Column(db.Float)

    def __repr__(self):
        return f'Ticker {self.DateTime, self.AAPL, self.MSFT, self.TEAM, self.TSLA}'


class LiveTickerClass(db.Model):
    # id = db.Column(db.Integer, primary_key=True)
    # Date = db.Column(db.String(8), nullable=False, unique=False)
    DateTime = db.Column(db.String(8), nullable=False, unique=True, primary_key=True)
    AAPL = db.Column(db.Float)
    MSFT = db.Column(db.Float)
    TEAM = db.Column(db.Float)
    TSLA = db.Column(db.Float)

    def __repr__(self):
        return f'LiveTicker {self.DateTime, self.AAPL, self.MSFT, self.TEAM, self.TSLA}'
