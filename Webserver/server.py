from flask import Flask, render_template, request, redirect, url_for, flash, session
from datetime import timedelta


app = Flask(__name__)
app.secret_key = "my super secret key"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  # removes an annoying warning message
app.permanent_session_lifetime = timedelta(minutes=10)


@app.route("/")
def login():
    return "Login Page"



if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)



