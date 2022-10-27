import requests
import yaml
from datetime import datetime, timedelta

import yfinance as yf
from pandas import DataFrame

import sys


def market_state() -> bool:
    """
    Checks if the market is open
    :return: True if open else False
    """
    response = requests.get('https://api.tradier.com/v1/markets/clock',
                            params={'delayed': 'true'},
                            headers={'Authorization': 'Bearer <TOKEN>', 'Accept': 'application/json'}
                            )
    json_response = response.json()
    return json_response['clock']['state'] == 'open'


def fetch_ticker_data(tickers: list[str]) -> DataFrame:
    return yf.download(tickers, period='ytd', interval='1h')


def get_uri():
    """
    Creates URI for DB setup
    Add login data to StockTickerApp/config/db_login.yaml
    """
    with open('config/db_login.yaml', 'r') as login_f:
        try:
            login_dict = yaml.safe_load(login_f)
            username = login_dict.pop('username')
            password = login_dict.pop('password')
            host = login_dict.pop('host')
            port = login_dict.pop('port')
            db_name = login_dict.pop('db_name')
        except yaml.YAMLError as exc:
            print(exc)

    # Using pure python PyMySQL bindings - URI = 'mysql+pymysql://.....'
    return f'mysql+pymysql://{username}:{password}@{host}:{port}/{db_name}'


def get_data(uri, tickers=None, dt=datetime.today()):
    # TODO add try except
    if tickers is None:
        tickers = ['AAPL', 'MSFT', 'TEAM', 'TSLA']
    yf.pdr_override()
    data = yf.download(tickers, start=dt, interval='2m', rounding=2)
    close_data = data['Close'].reset_index(level=0)
    close_data.iloc[:, 0] = close_data.iloc[:, 0].apply(lambda x: str(x)[11:16])
    close_data = close_data.groupby('Datetime').first().reset_index()
    close_data.to_sql('ticker_class', uri, if_exists='replace', index=False)
    # print(close_data[:, -1], file=sys.stderr)
