from datetime import date, timedelta
import numpy as np
import pandas as pd
import yfinance as yf
from config import *


def pull_data():
    """
    Function downloads crypto currency according to defined frequency and for defined period.
    Value at the time of interest is pulled (e.g. at 0 and 12 o'clock).
    :return: 1-row dataframe with most recent values in the defiend period as columns
    """
    today = date.today()
    data = yf.download(tickers=CRYPTO, start=(today - timedelta(days=PERIOD)), interval=FREQUENCY)
    lags = data[STATUS].iloc[(data.index.hour == HR1) | (data.index.hour == HR2)]
    lags = (lags - np.min(lags)) / (np.max(lags) - np.min(lags))
    lags = lags[-NUM_LAGS:]
    lags = pd.DataFrame(lags).T
    lags.columns = [f'lag_{i}' for i in reversed(range(lags.shape[1]))]
    return lags


def get_signal(ml_model):
    """
    :param ml_model: prediction model for trading strategy
    The function activates function of pulling trading data and creating 1-row dataframe
    which is used in pretrained model for prediction.
    :return: prediction result of the model (0 or 1)
    """
    lags = pull_data()
    signal = ml_model.predict(lags)
    return signal
