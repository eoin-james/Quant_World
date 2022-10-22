import requests

import yfinance as yf
from pandas import DataFrame


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
