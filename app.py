import pyrebase
from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
from datetime import datetime
import re
import mysql.connector
from flask_cors import CORS
import json
mysql = mysql.connector.connect(user='web', password='webPass',
  host='127.0.0.1',
  database='horse_valley_resort')

from logging.config import dictConfig

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})
app = Flask(__name__)
CORS(app)

# Set the secret key for the Flask app. This is used for session security.
app.secret_key = "horse_valley_resort"

# Configuration for Firebase
config = {
    "apiKey": "AIzaSyBDEtNyTYKttRSSeSfaEi_Whpd5-L0YqTs",
    "authDomain": "resort-2ffe4.firebaseapp.com",
    "databaseURL": "https://resort-2ffe4-default-rtdb.firebaseio.com/",
    "storageBucket": "resort-2ffe4.appspot.com"
}

# Initialize Firebase
firebase = pyrebase.initialize_app(config)

# Get reference to the auth service and database service
auth = firebase.auth()
db = firebase.database()


# Route for the login page
@app.route("/admin/login")
def login():
    return render_template("login.html")

# Route for the dashboard page
@app.route("/admin/dashboard")
def welcome():
    # Check if user is logged in
    if session.get("is_logged_in", False):
        return render_template("welcome.html", email=session["email"], name=session["name"])
    else:
        # If user is not logged in, redirect to login page
        return redirect(url_for('login'))

# Route for the bookings
@app.route("/admin/dashboard/rooms")
def bookings():
    # Check if user is logged in
    if session.get("is_logged_in", False):
        cur = mysql.cursor() #create a connection to the SQL instance
        cur.execute('''SELECT * FROM room''') # execute an SQL statment
        data = cur.fetchall()
        print("Query Result from DB", data)

        #Retriving the Column Names
        cur.execute('''DESCRIBE room''')
        column_info = cur.fetchall()
        column_names = [col[0] for col in column_info]
        print("Column Names of Room", column_names)

        #Converting List into JSON
        dict_list = []
        for item in data:
            dict_item = {column_names[i]: item[i] for i in range(len(column_names))}
            dict_list.append(dict_item)
        json.dumps(dict_list)
        print("Json Output", dict_list)
        # return render_template("admin-rooms.html", email=session["email"], name=session["name"], rooms=dict_list)
        return render_template("admin-rooms.html", email=session["email"], name=session["name"], rooms=dict_list, len=len(data))
    else:
        # If user is not logged in, redirect to login page
        return redirect(url_for('login'))

@app.route("/admin/dashboard/rooms/addition")
def rooms_add():
    if session.get("is_logged_in", False):
        cur = mysql.cursor() #create a connection to the SQL instance
        if request.method == 'POST':
            roomType = request.form['roomType']
            occupancy = request.form['occupancy']
            roomPrice = request.form['roomPrice']
            available = request.form['available']
            roomImage = request.form['roomImage']
            roomTitle = request.form['roomTitle']
            roomDesc = request.form['roomDesc']
            print("Values from Submit Button", roomType, occupancy,roomPrice,available,roomImage,roomTitle,roomDesc)
            # s='''INSERT INTO room(roomType,occupancy,roomPrice,available,roomImage,roomTitle,roomDesc) VALUES('{}','{}','{}','{}','{}','{}','{}');'''.format(roomType,occupancy,roomPrice,available,roomImage,roomTitle,roomDesc)
            # cur.execute(s)
            # mysql.commit()
        return render_template("admin-rooms.html", email=session["email"], name=session["name"])
    else:
        # If user is not logged in, redirect to login page
        return redirect(url_for('login'))


# Route for the Booking for the user: /user/booking
# Functionalities will be to return the room details with type and availablity for the seletected range.

# Route for the Booking Confirmation: /user/booking/confirm
# Details required: name, emailid(unique), phone number, dates, room type, number of rooms, random uniqueID -> saved in DB
# Functionalities will be to make the DB call to write for that date range.
# Example: dnsname/user/booking/uniqueID

#User Route for Login/ view the booking:
#DB call to random unique ID -> View all teh bookings and he can delete that booking
# dnsname/user/booking/uniqueID -> unique ID I will list the booking.

#user Route to delete his booking:
# dnsname/user/booking/uniqueID -> Option to delete the booking

# Route for the Admin Booking page /admin/dashboard/booking
# Functionalities will be to view all the booking

# Route for the Admin Room page /admin/dashboard/rooms
# Functionalities will be to add a number of rooms for the given room type.

# Route for the Admin Update page /admin/dashboard/booking/update
# Functionalities will be adding the room to the booking

# Route for the Admin Delete page /admin/dashboard/booking/delete
#Functionalitites will be deleting the booking



# Route for login result
@app.route("/admin/result", methods=["POST", "GET"])
def result():
    if request.method == "POST":
        result = request.form
        email = result["email"]
        password = result["pass"]
        try:
            # Authenticate user
            user = auth.sign_in_with_email_and_password(email, password)
            session["is_logged_in"] = True
            session["email"] = user["email"]
            session["uid"] = user["localId"]
            # Fetch user data
            data = db.child("users").get().val()
            # Update session data
            if data and session["uid"] in data:
                session["name"] = data[session["uid"]]["name"]
                # Update last login time
                db.child("users").child(session["uid"]).update({"last_logged_in": datetime.now().strftime("%m/%d/%Y, %H:%M:%S")})
            else:
                session["name"] = "User"
            # Redirect to welcome page
            return redirect(url_for('welcome'))
        except Exception as e:
            print("Error occurred: ", e)
            return redirect(url_for('login'))
    else:
        # If user is logged in, redirect to welcome page
        if session.get("is_logged_in", False):
            return redirect(url_for('welcome'))
        else:
            return redirect(url_for('login'))

# Route for logout
@app.route("/admin/logout")
def logout():
    # Update last logout time
    db.child("users").child(session["uid"]).update({"last_logged_out": datetime.now().strftime("%m/%d/%Y, %H:%M:%S")})
    session["is_logged_in"] = False
    return redirect(url_for('login'))

# Serve index.html file
@app.route('/')
def index():
    cur = mysql.cursor() #create a connection to the SQL instance
    cur.execute('''SELECT * FROM room''') # execute an SQL statment
    data = cur.fetchall()
    return render_template('index.html', room=data)

@app.route('/room/<id>')
def room(id):
   cur = mysql.cursor() #create a connection to the SQL instance
   cur.execute("SELECT * FROM room WHERE roomNo = %s", [id]) # execute an SQL statment
   data = cur.fetchall()
   my_dict = [dict(zip(("id", "roomType", "occupancy", "roomPrice", "available", "roomImage", "roomTitle", "roomDesc"), x)) for x in data]
   return render_template('room.html', details=my_dict)

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html')

if __name__ == "__main__":

# app.run(host='0.0.0.0',port='8080') #Run the flask app at port 8080
  app.run(host='0.0.0.0',port='8080', ssl_context=('cert.pem', 'privkey.pem')) #Run the flask app at port 8080
  # app.run(host='0.0.0.0',port='17234', ssl_context=('cert.pem', 'privkey.pem')) #Run the flask app at port 8080

