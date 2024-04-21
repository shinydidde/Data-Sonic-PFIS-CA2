import pyrebase
from flask import Flask, redirect, render_template, request, session, url_for
from datetime import datetime
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import mysql.connector
from flask_cors import CORS
import json
from databaseTransactions import roomBookingView, roomDetails, roomListDetails, roomDescribe, roomInsert, roomDelete, roomUpdate,bookingRoom, bookingView, bookingDescribe
import random
import time

mysql = mysql.connector.connect(user='web', password='webPass',
  host='127.0.0.1',
  database='horse_valley_resort')

from logging.config import dictConfig

#Things to do for Sure later post completion:
# To remove all the DB from here and move to the new py file or atleast function
# To create the test suite for Admin atleast

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


# Function to generate a random token ID for a booking
def generate_random_token_id():
    # Generate a random number between 10000 and 99999
    random_part = random.randint(10000, 99999)
    # Get the current timestamp (in milliseconds)
    timestamp = int(time.time() * 1000)
    # Combine the timestamp and random number
    return str(timestamp) + str(random_part)

# Route for the login page
@app.route("/admin/login")
def login():
    # Check if user is logged in
    if session.get("is_logged_in", False):
        return redirect(url_for('welcome'))
    else:
        # If user is not logged in, redirect to login page
        return render_template('login.html')

# Route for the dashboard page
@app.route("/admin/dashboard", methods=["GET", "POST"])
def welcome():
    # Check if user is logged in
    if session.get("is_logged_in", False):

        cur = mysql.cursor() #create a connection to the SQL instance
        print("Coming Inside welcome")
        if request.method == 'POST':
            print("Coming Inside post")
            # Get inputs from the form
            start_date = request.form['check_in']
            end_date = request.form['check_out']
            room_type = request.form['room_type']

            # Execute SQL query to fetch data based on date range and room type
            query = "SELECT COUNT(*) FROM booking WHERE startTime >= ? AND endTime <= ? AND roomType = ?"
            cur.execute(query, (start_date, end_date, room_type))
            total_bookings = cur.fetchone()[0]

            query = "SELECT SUM(roomPrice) FROM room WHERE roomType = ?"
            cur.execute(query, (room_type,))
            total_revenue = cur.fetchone()[0]

            # Calculate occupancy rate
            query = "SELECT SUM(occupancy) FROM room WHERE roomType = ?"
            cur.execute(query, (room_type,))
            total_rooms = cur.fetchone()[0]
            occupancy_rate = (total_bookings / total_rooms) * 100 if total_rooms else 0
        else:
            # Fetch occupancy rate
            cur.execute("SELECT COUNT(*) FROM booking")
            total_bookings = cur.fetchone()[0]

            cur.execute("SELECT SUM(occupancy) FROM room")
            total_rooms = cur.fetchone()[0]

            occupancy_rate = min((total_bookings / total_rooms) * 100, 100)

            # Fetch revenue
            cur.execute("SELECT SUM(roomPrice) FROM room")
            total_revenue = cur.fetchone()[0]
            report_data = {
                'occupancy_rate': occupancy_rate,
                'revenue': total_revenue,
                'guest_feedback': {'positive': 80, 'neutral': 15, 'negative': 5}
            }
            # Generate graph
            labels = list(report_data['guest_feedback'].keys())
            values = list(report_data['guest_feedback'].values())
            plt.figure(figsize=(8, 6))
            plt.bar(labels, values, color='green')
            plt.xlabel('Feedback')
            plt.ylabel('Percentage')
            plt.title('Guest Feedback Analysis')
            plt.ylim(0, 100)  # Set y-axis limit
            plt.yticks(range(0, 101, 5))  # Set y-axis ticks to increment by 5
            plt.grid(True)

            # Convert graph to image
            img_data = BytesIO()
            plt.savefig(img_data, format='png')
            img_data.seek(0)
            graph = base64.b64encode(img_data.getvalue()).decode()
        return render_template("welcome.html", email=session["email"], name=session["name"], report_data=report_data, has_report_data=True, graph=graph, availability={"Suite Room": -1, "Family Room": 0, "Deluxe Room": 1, "Classic Room": 1, "Superior Room": 1, "Luxury Room": 1, "Suite Rooms": 1})
    else:
        # If user is not logged in, redirect to login page
        return redirect(url_for('login'))

# Route for the bookings
@app.route("/admin/dashboard/rooms", methods=["GET", "POST"])
def bookings():

    # If user is not logged in, redirect to login page
    if not session.get("is_logged_in", False):
        return redirect(url_for('login'))

    data = roomDetails()

    #Retriving the Column Names
    column_info = roomDescribe()
    column_names = [col[0] for col in column_info]

    # Remove the first column name from the list
    column_names = column_names[1:]

    #Converting List into JSON
    dict_list = []
    for item in data:
        dict_item = {column_names[i]: item[i+1] for i in range(len(column_names))}
        dict_list.append(dict_item)
    json.dumps(dict_list)

    # To retrive the room_types to show to users
    room_types = [item[1] for item in data]
    # print("Room Types: ", room_types)

    if request.method == 'POST':
        type = request.form['type']
        # print("Type:", type)
        if type == "add":
            # print("Coming Inside Add")
            # roomType = request.form['roomType']
            # occupancy = request.form['occupancy']
            # roomPrice = request.form['roomPrice']
            # available = request.form['available']
            # roomImage = request.form['roomImage']
            # roomTitle = request.form['roomTitle']
            # roomDesc = request.form['roomDesc']
            # print("Values from Submit Button", roomType, occupancy,roomPrice,available,roomImage,roomTitle,roomDesc)
            insertingTheValues = roomInsert(request)
            print("Post Add Admin", insertingTheValues)

            #To update the Room table details to view in Frontend
            data = roomDetails()
            dict_list = []
            for item in data:
                dict_item = {column_names[i]: item[i+1] for i in range(len(column_names))}
                dict_list.append(dict_item)
            json.dumps(dict_list)

            # To retrive the room_types to show to users
            room_types = [item[1] for item in data]

            return render_template("admin-rooms.html", email=session.get("email"), name=session["name"], rooms=dict_list, len=len(data), roomTypes=room_types)

        if type == "remove":
            # print("Inside Remove Type:", type)
            # roomType = request.form['roomType']
            # # print("Values from Submit Button ", roomType)
            # s='''DELETE from room where roomType = '{}';'''.format(roomType)
            # cur.execute(s)
            # mysql.commit()
            deletingTheValues = roomDelete(request)
            print("Post Remove Admin", deletingTheValues)

            #To update the Room table details to view in Frontend
            data = roomDetails()
            dict_list = []
            for item in data:
                dict_item = {column_names[i]: item[i+1] for i in range(len(column_names))}
                dict_list.append(dict_item)
            json.dumps(dict_list)

            # To retrive the room_types to show to users
            room_types = [item[1] for item in data]

            #roomTypes=['Suite Room', 'Family Room', 'Deluxe Room', 'Classic Room', 'Superior Room', 'Luxury Room']
            return render_template("admin-rooms.html", email=session.get("email"), name=session["name"], rooms=dict_list, len=len(data), roomTypes=room_types)

        if type == "update":
            # print("Inside Update Type: ", type)
            # roomType = request.form['roomType']
            # occupancy = request.form['occupancy']
            # roomPrice = request.form['roomPrice']
            # available = request.form['available']
            # roomImage = request.form['roomImage']
            # roomTitle = request.form['roomTitle']
            # roomDesc = request.form['roomDesc']
            # print("Values from Submit Button", roomType, occupancy,roomPrice,available,roomImage,roomTitle,roomDesc)

            # s='''UPDATE room SET occupancy = '{}', roomPrice = '{}', available = '{}', roomImage = '{}', roomTitle = '{}', roomDesc = '{}' where roomType = '{}';'''.format(occupancy,roomPrice,available,roomImage,roomTitle,roomDesc,roomType)
            # cur.execute(s)
            # mysql.commit()
            updatingTheValues = roomUpdate(request)
            print("Post Update Admin", updatingTheValues)


            #To update the Room table details to view in Frontend
            data = roomDetails()
            dict_list = []
            for item in data:
                dict_item = {column_names[i]: item[i+1] for i in range(len(column_names))}
                dict_list.append(dict_item)
            json.dumps(dict_list)

            # To retrive the room_types to show to users
            room_types = [item[1] for item in data]

            return render_template("admin-rooms.html", email=session.get("email"), name=session["name"], rooms=dict_list, len=len(data), roomTypes=room_types)

    else:
        return render_template("admin-rooms.html", email=session.get("email"), name=session.get("name"), rooms=dict_list, len=len(data), roomTypes=room_types)


# Route for the user rooms availability
@app.route("/user/rooms/availability", methods=["GET", "POST"])
def availability():
    if request.method == "POST":
        result = request.form
        startDate = result["startDate"]
        endDate = result["endDate"]
        print(startDate,endDate)
        data = roomBookingView(startDate, endDate)
        print("Printing from Here: ", data)

        # Convert the list of tuples to a dictionary
        result_dict = {}
        for room_type, available_rooms in data:
            result_dict[room_type] = available_rooms

        # Convert the dictionary to a JSON string
        availRoomsNo = json.dumps(result_dict)
        print(availRoomsNo)
        return render_template("index.html", email=session.get("email"), name=session["name"], availRoomsNo=availRoomsNo, roomDetails = roomDetails)
        #return render_template(url_for('index'))


@app.route('/booking', methods=["POST", "GET"])
def book():
    # Retrieve the values of startDate and endDate from the URL parameters
    start_date = request.args.get('startDate')
    end_date = request.args.get('endDate')
    print("Coming into Method of Booking", start_date , end_date)
    roomData = roomBookingView(start_date, end_date)
    # Convert the list of tuples to a dictionary
    result_dict = {}
    for room_type, available_rooms in roomData:
        result_dict[room_type] = available_rooms

    # Convert the dictionary to a JSON string
    availRoomsNo = json.dumps(result_dict)
    availRoomsNoDict = json.loads(availRoomsNo)
    print(availRoomsNo, availRoomsNoDict)

    if request.method == 'POST':
        # Get form data
        name = request.form['name']
        email = request.form['email']
        check_in = request.form['check_in']
        check_out = request.form['check_out']
        room_type = request.form['room_type']
        room_number = request.form['room_number']
        random_token_id = generate_random_token_id()
        print("ToeknID, request", random_token_id, request)
        bookingCreate = bookingRoom(request, random_token_id)
        print("Success here in the Booking Addition")

        bookedDetails = bookingView(random_token_id)

        # column_info_booking = bookingDescribe()
        # column_names = [col[0] for col in column_info_booking]

        # # Remove the first column name from the list
        # column_names = column_names[1:]

        # booking_dict = []
        # for item in bookedDetails:
        #     dict_item = {column_names[i]: item[i+1] for i in range(len(column_names))}
        #     booking_dict.append(dict_item)
        # json.dumps(booking_dict)

        # Convert the dictionary to a JSON string
        # availRoomsNo = json.dumps(result_dict)
        # availRoomsNoDict = json.loads(availRoomsNo)
        # print(availRoomsNo, availRoomsNoDict)

        return render_template('booking-confirmation.html', name = name, email = email, check_in = check_in, check_out = check_out, room_type= room_type, room_number = room_number, bookedDetails = random_token_id)

    # return render_template('booking.html', availability={"Suite Room": -1, "Family Room": 0, "Deluxe Room": 1, "Classic Room": 1, "Superior Room": 1, "Luxury Room": 1, "Suite Rooms": 1})
    # # availRoomsNo = {"Suite Room": -3, "Family Room": 0, "Deluxe Room": 1}
    return render_template('booking.html', availability=availRoomsNoDict)

@app.route('/booking-confirmation')
def confirmation():
        # Redirect to a thank you page or confirmation page
    randomId = request.args.get('random_token_id')
    print("Here", randomId)
    # Need to get the data from DB

    return render_template('booking-confirmation.html',name = "test", email = "Testing",check_in= "2024-01-01",check_out= "2024-01-01",room_type= "Suite Room")


@app.route('/manage-booking/<token>', methods=['GET','POST'])
def booking_confirmation(token):
    username = request.form.get('username')
    # Example validation: Check if the username is not empty
    if request.method == 'POST':
        if username:
            # Perform additional validation if needed
            print("token", token)
            bookedDetails = bookingView(token)
            print("Booked Details", bookedDetails)
            return render_template('manage-booking.html', token=token)
        else:
            return render_template('index.html')
    # Render the booking confirmation template with the token


# Route for the Booking Confirmation: /user/booking/confirm
# Details required: name, emailid(unique), phone number, dates, room type, number of rooms, random uniqueID -> saved in DB
# Functionalities will be to make the DB call to write for that date range.
# Example: dnsname/user/booking/uniqueID

#user Route to delete his booking:
# dnsname/user/booking/uniqueID -> Option to delete the booking

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
@app.route('/' , methods=["GET", "POST"])
def index():

    if request.method == "GET":
        data = roomDetails()
        return render_template('index.html', room=data)

    if request.method == "POST":

        result = request.form
        startDate = result["startDate"]
        endDate = result["endDate"]
        #print(startDate,endDate)
        data = roomBookingView(startDate, endDate)
        # print("Printing from Here: ", data)

        # Convert the list of tuples to a dictionary
        result_dict = {}
        for room_type, available_rooms in data:
            result_dict[room_type] = available_rooms

        # Convert the dictionary to a JSON string
        availRoomsNo = json.dumps(result_dict)
        print(availRoomsNo)

        tempArray = []
        for item in data:
            if item[1] >= 1:
                tempArray.append(item[0])
        roomSpecificData = roomListDetails(tempArray)
        print("Data of Specific Rooms", roomSpecificData)
        return render_template("index.html", email=session.get("email"), name=session["name"], availRoomsNo=availRoomsNo, room=roomSpecificData)

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

