import pandas
import yfinance as yf

from typing import Union
from pandas.tseries.offsets import BDay
from datetime import datetime, timedelta


def fetch_ticker_data(tickers: list, date: Union[datetime, None] = None) -> pandas.DataFrame:
    """
    Fetch data from yfinance for given date and tickers.
    :param tickers: List of tickers to download
    :param date: Date to fetch data from - Must be Business day
    :return: DF with columns Date, Time, [Tickers]
    """

    # TODO: Check if passed date is BDay
    if not date:
        date = datetime.today() - BDay()
        date = date.date()

    yf.pdr_override()
    # Download Data
    data = yf.download(tickers, start=date, interval='2m', rounding=2, progress=False)
    # Only use Close data
    df = data['Close'].reset_index(level=0)

    # Split Datetime col into Date and Time cols
    df.insert(loc=0, column='Time', value=[d.time() for d in df['Datetime']])
    df.insert(loc=0, column='Date', value=[d.date() for d in df['Datetime']])
    return df.drop('Datetime', axis=1)


def df_to_s3(data: pandas.DataFrame, bucket_name: str) -> None:
    """
    Passes DF to S3 bucket
    :param data: DF
    :param bucket_name: S3 Bucket
    :return: None
    """
    aws_s3_save_name = f'{data["Date"].iloc[0]}_Data_for_{"_".join(data.columns[2:])}.csv'
    data.to_csv(f's3://{bucket_name}/{aws_s3_save_name}')
