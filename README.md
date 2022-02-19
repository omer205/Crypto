#### Project authors:
Omer Cohen, Marina Goldman, Nissiel Thomas

# BTC trend trading strategy
This is a final project of ITC Data Science Oct 2021 cohort program.
We aim to provide BTC trading strategy using ML models.


## Model
Our model is an XGBoost Ensemble trained on historical BTC price data and provides a 'hold'/'stay-out' prediction 
based on last 18 days lags. 

To be added: [Link to medium article]

## Signal Service
After enrolling email address, signal based on model prediction will be sent every 12 hours in email.
In order to get enrolled please approach one of the contributors.

## How to use:
1. `run_crypto.sh` allows to run both the webpage for enrollment and the mailing service. 
2. When adding CL argument `-t` for the main file, the mailing will be in testing mode, meaning prediction will be sent to email in user list every 30 seconds.
3. API: Currently we are using port 8080 (configurable), accessing the enrollment service is via `/hello`.

## .py files of this project

 - main.py - schedule mailing of predictions
 - model.py - pulling data (from yfinance) and providing prediction
 - website.py - created enrollment page
 - config.py - constants used for the program.