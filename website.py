from flask import Flask, render_template, request, flash
import xgboost
print(xgboost.__version__)

from main import schedule_every_day
app = Flask(__name__)
app.secret_key = "manbearpig_MUDMAN888"
LOCAL_RUN = False
AWS_PORT = 8080

with open('user_list.txt', 'r') as filehandle:
    email = filehandle.read()
    email = email.splitlines()
print(email)

@app.route("/hello")
def index():
    flash("Put your mail address and get BTC signal every 12 hours")
    return render_template("index.html")


@app.route("/greet", methods=['POST', 'GET'])
def greeter():

    flash("Welcome " + str(request.form['name_input']) + ", you are now ready to get billionaire.")
    #if first time this email was given we add it to our list
    if request.form['name_input'] not in email:
        email.append(str(request.form['name_input']))
    #write the new list in user_list.txt
    with open('user_list.txt', 'w') as filehandle:
        for list_item in email:
            filehandle.write('%s\n' % list_item)
    return render_template("index.html")



if __name__ == '__main__':
    if LOCAL_RUN:
        app.run()
    else:
        app.run(host='0.0.0.0', port=AWS_PORT)
