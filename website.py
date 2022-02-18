from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "manbearpig_MUDMAN888"
LOCAL_RUN = False
AWS_PORT = 8080
EMAILS_LIST = "user_list.txt"
HOST = "0.0.0.0"

with open(EMAILS_LIST, 'r') as filehandle:
    email = filehandle.read()
    email = email.splitlines()
print(email)


@app.route("/hello")
def index():
    """
    html page for input an email address
    """
    flash("Put your mail address and get BTC signal every 12 hours")
    return render_template("index.html")


@app.route("/greet", methods=['POST', 'GET'])
def greeter():
    """
    Adding email address to distribution list.
    """
    flash("Welcome " + str(request.form['name_input']) + ", you are now ready to get billionaire.")
    # if first time this email was given we add it to our list
    if request.form['name_input'] not in email:
        email.append(str(request.form['name_input']))
    # write the new list in user_list.txt
    with open(EMAILS_LIST, 'w') as filehandle:
        for list_item in email:
            filehandle.write('%s\n' % list_item)
    return render_template("index.html")


if __name__ == '__main__':
    if LOCAL_RUN:
        app.run()
    else:
        app.run(host=HOST, port=AWS_PORT)
