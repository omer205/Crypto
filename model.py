from datetime import date, timedelta
import numpy as np
import pandas as pd
import yfinance as yf

TODAY = date.today()
PERIOD = 18
STATUS = 'Open'
MODEL_FILENAME = 'model'
FREQUENCY = "1h"
CRYPTO = "btc-usd"
SCHEDULE_1 = 0
SCHEDULE_2 = 12
NUM_LAGS = 2 * PERIOD


def pull_data():
    """
    Function downloads crypto currency according to defined frequency and for defined period.
    Value at the time of interest is pulled (e.g. at 0 and 12 o'clock).
    :return: 1-row dataframe with most recent values in the defiend period as columns
    """
    data = yf.download(tickers=CRYPTO, start=(TODAY - timedelta(days=PERIOD)), interval=FREQUENCY)
    lags = data[STATUS].iloc[(data.index.hour == SCHEDULE_1) | (data.index.hour == SCHEDULE_2)]
    lags = (lags - np.min(lags)) / (np.max(lags) - np.min(lags))
    lags = lags[-NUM_LAGS:]
    lags = pd.DataFrame(lags).T
    lags.columns = [f'lag_{i}' for i in reversed(range(lags.shape[1]))]
    return lags


def get_signal(model):
    """
    :param model: prediction model for trading strategy
    The function activates function of pulling trading data and creating 1-row dataframe
    which is used in pretrained model for prediction.
    :return: prediction result of the model (0 or 1)
    """
    lags = pull_data()
    signal = model.predict(lags)
    return signal
