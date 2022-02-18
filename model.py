import yfinance as yf
from datetime import date, datetime, timedelta
import numpy as np
import pandas as pd
import pickle

today = date.today()
INTERVAL = 6
STATUS = 'Close'
MODEL_FILENAME = 'model'


def pull_data():
    data = yf.download(tickers="btc-usd", start=(today - timedelta(days=INTERVAL)), interval="1h")
    lags = data[STATUS].iloc[(data.index.hour == 0) | (data.index.hour == 12)]
    lags = (lags - np.min(lags)) / (np.max(lags) - np.min(lags))
    lags = lags[-12:]
    lags = pd.DataFrame(lags).T
    lags.columns = [f'lag_{i}' for i in reversed(range(lags.shape[1]))]
    return lags

def get_signal(model):
    lags = pull_data()
    signal = model.predict(lags)
    return signal


