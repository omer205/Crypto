import smtplib, ssl, schedule, time, pickle
from smtplib import SMTP
import sys
import argparse
from model import get_signal
from config import *

parser = argparse.ArgumentParser(
    description="-t (optional) for testing frequency")
parser.add_argument("-t", action='store_true', help="type [-t] to have testing frequency of prediction")
args = parser.parse_args()

SCHEDULE_1 = "12:05"
SCHEDULE_2 = "00:05"

def get_message():
    """"
    Gets prediction signal from imported get_signal function and
    returns: string - message according to the signal
    """
    prediction = get_signal(model)[0]
    if prediction == HOLD_BTC:
        message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT_HOLD)
    else:
        message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT_OUT)
    return message


def read_from_txt():
    """
    open file and read the content in a list
    return: list of strings
    """
    a_file = open(EMAILS_LIST, "r")
    receiver_email = [(line.strip()).split() for line in a_file]
    a_file.close()
    return receiver_email


def send_mail():
    """
    The function sends email from python using library smtplib
    """
    global server  # initialize a variable server

    # Google SMTP server is a free service that will enable you to send emails from your website, web app or domain.
    # SMTP means Simple Mail Transfer Protocol and it allows you to send emails between servers.
    # Most emails are sent from this server – in fact, if you use Gmail or any Google app, you are using this server.

    smtp_server = SERVER_SMTP
    port = PORT
    sender_email = EMAIL_SENDER  # Email from which prediction message is sent
    password = EMAIL_PASSWORD
    receiver_email = read_from_txt()

    message = get_message()
    context = ssl.create_default_context()  # Create a secure SSL context

    # Try to log in to server and send email
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()  # Can be omitted
        server.starttls(context=context)  # Secure the connection
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)  # login to the send account
        server.sendmail(sender_email, receiver_email, message)  # send message to everyone from the list
    except Exception as e:
        # Print any error messages to stdout
        print(e)
    finally:
        server.quit()


def schedule_every_day():
    """
    Sends prediction message email according to defined schedule.
    There is regular schedule and schedule for testing purposes.
    """
    schedule.every().day.at(SCHEDULE_1).do(send_mail)
    schedule.every().day.at(SCHEDULE_2).do(send_mail)
    if args.t:
        schedule.every(TEST_FREQUENCY).seconds.do(send_mail)
    while True:
        # Checks whether a scheduled task
        # is pending to run or not
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    model = pickle.load(open(MODEL_FILENAME, 'rb'))
    schedule_every_day()
