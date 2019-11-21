from flask import Flask
from flask import render_template, request, url_for, redirect, jsonify, json
#from flask.ext.scss import Scss
import sqlite3

app = Flask(__name__)
#Scss(app)

# Main Page
@app.route('/')
def index():
    return render_template("main.html")

# Registration Page
# Click 'New User'
@app.route('/Register')
def register():
    render_template("register.html")
    return 'ok'

@app.route('/User', methods=['POST'])
def saveUser():
    return render_template("NewUser.html")

@app.route('/adduser',methods = ['POST', 'GET'])
def adduser():
   print("test")
   if request.method == 'POST':
      try:
         nm = request.form['nm']
         phone = request.form['phone']
         card = request.form['card']
         
         with sqlite3.connect("Siip.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO users(name,phone) VALUES ('" + nm + "','" + phone + "');")
            
            con.commit()
      except:
         con.rollback()
         msg = "error in insert operation"
         return "failed"
      finally:
         con.close()
         return "success 2"

# Scanner call - jQuery Ajax call 
@app.route('/Scan')
def scan():
      # Do scanner stuff here
      # Get userId - SQLLite
      # redirect_to user/<userId> -- In front end
      return jsonify(results = {"dataKey": "value"})

# User Page
# For getting an existing user
'''
@app.route('/User/<userId>')
def user(userId):
      return render_template("user.html", user=userId)
'''
    