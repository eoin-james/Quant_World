import sys
import warnings

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
# Checks if stock market is open and decides on a datetime for the APP to use
market_status = market_state()
if market_status:
    dt = datetime.today().date()  # Today's stock data so far
else:
    # TODO: Make sure market was open 'yesterday' as could be a weekend etc
    dt = datetime.today().date() - timedelta(days=1)  # Yesterdays stock data

uri = get_uri()  # DB login URI - See config/db_login.yaml for login details

app = AppClass(blueprint, uri, db)  # Create an App Class - Wrapped as more than just Flask is used

tickers = ['AAPL', 'MSFT', 'TEAM', 'TSLA']  # Set the stock data you want - Max 4 for now not tested on less than 4 yet


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
