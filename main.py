import smtplib, ssl, schedule, time, pickle
from model import get_signal

#use this function when you implemented variable prediction in the function send mail
#message = message() line 40
SUBJECT = 'BTC Signal - ITC Project'
TEXT_HOLD = 'Hello,\n Today is a good day. We recommend you to stay in.'
TEXT_OUT = 'Hello,\n Today is a bad day. We recommend you to be out.'
MODEL_FILENAME = 'model'
TEST = 1

def get_message():
    prediction = get_signal(model)[0]
    if prediction == 1 :
        message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT_HOLD)

    else:
        message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT_OUT)
    return message

def send_mail():

    """
    the function send email from python using library smtplib
    """

    global server #initialize a variable server

    #Google SMTP server is a free service that will enable you to send emails from your website, web app or domain.
    #SMTP means Simple Mail Transfer Protocol and it allows you to send emails between servers.
    # Most emails are sent from this server – in fact, if you use Gmail or any Google app, you are using this server.

    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls it is the default mail submission port.
    sender_email = "projectitcbtc@gmail.com" # our group email
    password = "helloworld123" #email password
    receiver_email = read_from_txt() #catch all mail adress from the file user_list.txt and return as a list

    #add predict value here

    # message = """\
    # Subject: cryptocurrency project
    #
    # hello , This message is sent from Python."""
    message = get_message()
    context = ssl.create_default_context() # Create a secure SSL context

    # Try to log in to server and send email
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()  # Can be omitted
        server.starttls(context=context)  # Secure the connection
        server.ehlo()  # Can be omitted
        server.login(sender_email, password) #lgin to the send account
        server.sendmail(sender_email, receiver_email, message) #send message to everyone from the mist
    except Exception as e:
        # Print any error messages to stdout
        print(e)
    finally:
        server.quit()


def read_from_txt():
    # open file and read the content in a list
    a_file = open("user_list.txt", "r")

    receiver_email = [(line.strip()).split() for line in a_file]

    a_file.close()

    return receiver_email


def schedule_every_day():

    schedule.every().day.at("12:05").do(send_mail) #every day at 12:05 this func call send mail func
    schedule.every().day.at("00:05").do(send_mail)
    if TEST:
        schedule.every(30).seconds.do(send_mail)
    while True:
        # Checks whether a scheduled task
        # is pending to run or not
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    model = pickle.load(open(MODEL_FILENAME, 'rb'))
    schedule_every_day()
