import boto3

from io import StringIO
from utils import fetch_ticker_data, df_to_s3

"""
Path
/Users/eoinmca/PycharmProjects/Quant_World/SockTickerAppAWS
"""

tickers = ['AAPL', 'MSFT', 'TEAM', 'TSLA']
bucket_name = 'sta-bucket'


def main():
    s3 = boto3.resource("s3")
    data = fetch_ticker_data(tickers)
    df_to_s3(data, bucket_name)


if __name__ == '__main__':
    main()
