# Mail Service Constants
SUBJECT = 'BTC Signal - ITC Project'
TEXT_HOLD = 'Hello,\n Today we believe is a good day.\n We recommend you to HOLD BTC for the next 12 hrs.'
TEXT_OUT = 'Hello,\n Today we think BTC is risky.\n We recommend you to stay out for next 12 hrs.'
MODEL_FILENAME = 'model'
HOLD_BTC = 1
PORT = 587  # For starttls it is the default mail submission port.
EMAIL_SENDER = "projectitcbtc@gmail.com"
# EMAIL_PASSWORD = personal.PASSWORD  # stored in separate file 'personal'
EMAIL_PASSWORD = 'helloworld123'
SERVER_SMTP = "smtp.gmail.com"
EMAILS_LIST = "user_list.txt"
TEST_FREQUENCY = 30

#Prediction and Data Constants
PERIOD = 18
STATUS = 'Open'
MODEL_FILENAME = 'model'
FREQUENCY = "1h"
CRYPTO = "btc-usd"
SCHEDULE_1 = 0
SCHEDULE_2 = 12
NUM_LAGS = 2 * PERIOD
