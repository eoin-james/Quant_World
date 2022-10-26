import sys

from datetime import datetime, timedelta

from app import AppClass
from utils import get_uri, market_state, get_data

from api import blueprint
from models import db, TickerClass, LiveTickerClass

from flask import Flask, render_template, request

wait_time = 2000
debug = True
port_num = 4444
market_status = market_state()
# market_status = True
uri = get_uri()

app = AppClass(blueprint, uri, db)

tickers = None


@app.app.route('/', methods=['GET', 'POST'])
def index():

    if market_status:
        # If market is open load current days ticker data then run function to maintain DB while app is running
        dt = datetime.today()
        app.executor_submit(get_data, uri, tickers, dt)
    else:
        # If market is closed, load the DB with the previous days ticker data then render_template after
        dt = datetime.today().date() - timedelta(days=1)
        get_data(uri, tickers, dt)

    if request.method == 'GET':
        return render_template(
            'index.html',
            market_status=market_status,
            wait_time=wait_time
        )


if __name__ == '__main__':
    app.run(debug, port_num)
