In this project we currently have 6 files.
the readme that you are reading right now.
the user.txt which will allow us to store all the email addresses, and to read them again each time we send an email.
the check.py which is the implementation of flask.
main.py is where we find the function to send the mails and the function that will allow us to automate the sending at a certain time.
in the template folder we have the html file that allows us to build the web page
and finally in the static folder we have main.css which allows us to make our html page beautiful by changing the settings of the page.

IMPORTANT POINT:

1)in main.py add a value prediction which call your model and get his output (put it line 37).
2)i added a function message() to write the text of our mail , change it as you feel it is good and call it,
line 40 message = message().
3)in schedule_every_day() , i already scheduled to send mail twice a day at 12:05 and 00:05,
lets change with the time we want . main.py line 72

run both file together , and copy paste the link to your browser , put your email adress as asked ,, and let syour code work.
