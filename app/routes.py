from flask import Flask, render_template, request, url_for, redirect, jsonify, json
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from app import app

# Main Page
@app.route('/')
def index():
    return render_template("main.html")

# Registration Page
# Click 'New User' - Left Side
@app.route('/Register')
def register():
    return render_template("register.html")

# Called from the form in register.html on submit
# Inserts the user into the database
@app.route('/AddUser', methods = ['POST'])
def addUser():
   print("test")
   if request.method == 'POST':
      try:
         nm = request.form['nm']
         phone = request.form['phone']
         card = request.form['card']
         
         with sqlite3.connect("Siip.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO users(name,phone,creditCard) VALUES (?,?,?)", (nm, phone, card))
            
            con.commit()
      except:
         con.rollback()
         msg = "error in insert operation"
         return "failed"
      finally:
         con.close()
         return "success 2"

# Scanner call - jQuery Ajax call 
# Click 'Scan' - Right Side
@app.route('/Scan')
def scan():
      # Do scanner stuff here
      # Get userId - SQLLite
      # return userInfo as JSON
      # redirect_to user/<userId> -- In front end
   reader = SimpleMFRC522()

   try:
      id, text = reader.read()
      return jsonify(results = {"rfid": id})
   finally:
      GPIO.cleanup()

# User Page
# For getting an existing user
@app.route('/User/<userId>')
def user(userId):
      return render_template("user.html", user=userId)
    
