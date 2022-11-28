import boto3
import pandas as pd
import plotly.graph_objs as go
import pandas as pd
import numpy as np
from plotly.subplots import make_subplots
from utils import fetch_ticker_data, df_to_s3

pd.options.plotting.backend = "plotly"

"""
Path
/Users/eoinmca/PycharmProjects/Quant_World/SockTickerAppAWS
"""

tickers = ['AAPL', 'MSFT', 'TEAM', 'TSLA']
bucket_name = 'sta-bucket'
s3 = boto3.resource("s3")


def plot(df):
    data = df.drop(['Date', 'Time'], axis=1)
    rows = 2
    cols = 2
    fig = make_subplots(rows, cols)
    x = 0
    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            fig.add_trace(
                go.Scatter(
                    x=df['Time'],
                    y=data[data.columns[x]].values,
                    mode='lines',
                    name=data.columns[x]),
                row=i,
                col=j)
            x = x + 1

    fig.show()


"""
title='',
template='simple_white',
labels=dict(index="Time", value="Value", variable="Ticker")
"""


def main():
    # Get Data
    data = fetch_ticker_data(tickers)

    # Upload Data
    # df_to_s3(data, bucket_name)

    # Plot Data
    plot(data)


if __name__ == '__main__':
    main()
