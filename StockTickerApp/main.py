import sys
import warnings

from datetime import datetime, timedelta

from app import AppClass
from utils import get_uri, market_state, get_data

from api import blueprint
from models import db, TickerClass, LiveTickerClass

from flask import Flask, render_template, request

warnings.simplefilter(action='ignore', category=FutureWarning)

wait_time = 30000
debug = True
port_num = 4444
market_status = market_state()
if market_status:
    dt = datetime.today().date()
else:
    dt = datetime.today().date() - timedelta(days=1)

uri = get_uri()

app = AppClass(blueprint, uri, db)

tickers = ['AAPL', 'MSFT', 'TEAM', 'TSLA']


@app.app.route('/data', methods=['GET', 'POST'])
def data_update():
    app.executor_submit(get_data, uri, tickers, datetime.today().date())
    return 'Updated data', 200


@app.app.route('/')
def index():
    get_data(uri, tickers, dt)

    return render_template(
        'index.html',
        market_status=market_status,
        wait_time=wait_time,
        date=dt,
        tickers=tickers
    )


if __name__ == '__main__':
    app.run(debug, port_num)
