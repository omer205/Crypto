#### Project authors:
Omer Cohen, Marina Goldman, Nissiel Thomas

# BTC trend trading strategy
**This** is a final project of the Israel Tech Challenge (TC) Data Science Oct 2021 cohort program.
We aim to provide Bitcoin (BTC) trading strategy using ML models.


## Model
Our model is an XGBoost Ensemble trained on historical BTC price data and provides a 'hold'/'stay-out' prediction based on last 18 days lags. 

Check our 3-parts post in Medium [Part 1](https://medium.com/@omer205/ml-approach-for-bitcoin-swing-trading-part-1-time-series-forecast-f3204a92f549), [Part 2](https://medium.com/@omer205/ml-approach-for-bitcoin-swing-trading-part-2-classification-with-naive-labelling-c18a022aa84e), [Part 3](https://medium.com/@omer205/ml-approach-for-bitcoin-swing-trading-part-3-classification-with-trend-labelling-32190cf5d619).

## Signal Service
After enrolling an email address, a signal based on the model prediction will be sent every 12 hours in email.
In order to get enrolled please approach one of the contributors.

## How to use:
1. `run_crypto.sh`  allows running both the webpage for enrolment and the mailing service. 
2. When adding CL argument `-t` for the main file, the mailing will be in testing mode, meaning prediction will be sent to the email in user list every 30 seconds.
3. API: Currently we are using port 8080 (configurable), accessing the enrolment service is via `/hello`.

## .py files of this project

 - main.py - schedule mailing of predictions

 - model.py - pulling data (from yfinance) and providing prediction

 - website.py - created enrolment page

 - config.py - constants used for the program.

   

## .ipynb files of this project

   - Part I - Time Series Forecasting.ipynb - related to Part I publication in Medium

   - Part II - Classification with Naive Labelling.ipynb - related to Part II publication in Medium

   

   