import sys
import warnings

import pandas as pd
from pandas.tseries.offsets import BDay

from datetime import datetime, timedelta

from app import AppClass
from utils import get_uri, market_state, get_data

from api import blueprint
from models import db, TickerClass, LiveTickerClass

from flask import Flask, render_template, request

# Pandas warnings suppressed
warnings.simplefilter(action='ignore', category=FutureWarning)

wait_time = 30000  # 30 seconds
debug = True  # Debug for Flask
port_num = 4444  # Port for Flask

# If market is open use current data else use last open days data
market_status = market_state()
if market_status:
    dt = datetime.today().date()
else:
    # TODO: are BDays == MarketStatus
    dt = datetime.today() - BDay(1)
    dt = dt.date()

uri = get_uri()  # DB login URI - See config/db_login.yaml for login details

app = AppClass(blueprint, uri, db)  # Create an App Class - Wrapped as more than just Flask is used

tickers = ['AAPL', 'MSFT', 'TEAM', 'TSLA']


@app.app.route('/data', methods=['GET', 'POST'])
def data_update():
    """
    Called from javascript file to initiate a Database update - Runs while stock market is open every 'wait_time' ms
    Runs while Flask app is running
    :return: Success call
    """
    app.executor_submit(get_data, uri, tickers, datetime.today().date())
    return 'Updated data', 200


@app.app.route('/')
def index():
    """
    Data is fetched before index returned otherwise there will be no up-to-date graph data
    :return: Data for frontend
    """
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
