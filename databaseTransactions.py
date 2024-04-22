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


#Creation of Cursor fot the DB
cur = mysql.cursor()

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

#Room Details of all
def roomDetails():
    try:
        cur.execute('''SELECT * FROM room''') # execute an SQL statment
        data = cur.fetchall()
        return data
    except Exception as e:
        print("Error:", e)
        return None

#Booking Details of all
def bookingDetails():
    try:
        cur.execute('''SELECT * FROM booking''') # execute an SQL statment
        data = cur.fetchall()
        return data
    except Exception as e:
        print("Error:", e)
        return None

#Room Price for the given room type
def roomPrice(roomType):
    try:
        query = '''SELECT roomPrice FROM room WHERE roomType = '{}';'''.format(roomType)
        cur.execute(query)
        data = cur.fetchall()
        print("Data from RoomPrice DB Call ", data)
        return data
    except Exception as e:
        print("Error:", e)
        return None

#Describing the Column Names of the Room Table
def roomDescribe():
    try:
        cur.execute('''DESCRIBE room''')
        column_info = cur.fetchall()
        return column_info
    except Exception as e:
            print("Error:", e)
            return None

#Describing the Column Names of the Booking Table
def bookingDescribe():
    try:
        cur.execute('''DESCRIBE booking''')
        column_info = cur.fetchall()
        return column_info
    except Exception as e:
            print("Error:", e)
            return None


#Inserting into room Details:
def roomInsert(request):
    try:
        roomType = request.form['roomType']
        occupancy = request.form['occupancy']
        roomPrice = request.form['roomPrice']
        available = request.form['available']
        roomImage = request.form['roomImage']
        roomTitle = request.form['roomTitle']
        roomDesc = request.form['roomDesc']
        s='''INSERT INTO room(roomType,occupancy,roomPrice,available,roomImage,roomTitle,roomDesc) VALUES('{}','{}','{}','{}','{}','{}','{}');'''.format(roomType,occupancy,roomPrice,available,roomImage,roomTitle,roomDesc)
        cur.execute(s)
        mysql.commit()
        print("INsert successful")
        return "success add"
    except Exception as e:
        print("Error:", e)
        return None

#Deleting the Room
def roomDelete(request):
    try:
        roomType = request.form['roomType']
        print(roomType)
        s='''DELETE from room where roomType = '{}';'''.format(roomType)
        g = cur.execute(s)
        print("Here", g)
        mysql.commit()
        print("Delete successful")
        return "success Delete"
    except Exception as e:
        print("Error:", e)
        return None

#Updating the Room
def roomUpdate(request):
    try:
        roomType = request.form['roomType']
        occupancy = request.form['occupancy']
        roomPrice = request.form['roomPrice']
        available = request.form['available']
        roomImage = request.form['roomImage']
        roomTitle = request.form['roomTitle']
        roomDesc = request.form['roomDesc']
        s='''UPDATE room SET occupancy = '{}', roomPrice = '{}', available = '{}', roomImage = '{}', roomTitle = '{}', roomDesc = '{}' where roomType = '{}';'''.format(occupancy,roomPrice,available,roomImage,roomTitle,roomDesc,roomType)
        cur.execute(s)
        mysql.commit()
        print("Update successful")
        return "success Update"

    except Exception as e:
        print("Error:", e)
        return None

#Room Details for the selected array of rooms
def roomListDetails(roomList):
    try:
        # Create the SQL query dynamically with the specified room types
        query = "SELECT * FROM room WHERE roomType IN ("
        query += ', '.join(['%s'] * len(roomList))  # Add placeholders for each room type
        query += ");"
        cur.execute(query, roomList)
        data = cur.fetchall()
        # print("Selected Room Data", data)
        return data

    except Exception as e:
        print("Error:", e)
        return None

#Room Check based upon Date Range
def roomBookingView(startDate, endDate):
    try:
        print("Room Booking Select data range", startDate, endDate)

        # Set the start and end times
        start_query = "SET @start_time = %s;"
        end_query = "SET @end_time = %s;"
        cur.execute(start_query, (startDate,))
        cur.execute(end_query, (endDate,))

        # Execute the main query
        query = '''
        SELECT r.roomType,
                r.available - COALESCE(b.total_bookings, 0) AS available_rooms
        FROM room r
        LEFT JOIN (
            SELECT roomType, COUNT(*) AS total_bookings
            FROM booking
            WHERE startTime <= @end_time AND endTime >= @start_time
            GROUP BY roomType
        ) b ON r.roomType = b.roomType;
        '''
        cur.execute(query)
        data = cur.fetchall()
        print("Data from the DB: ", data)
        return data
    except Exception as e:
        print("Error:", e)
        return None

#RoomType from the Room Table
def roomType():
    try:
        cur.execute('''SELECT roomType FROM room''') # execute an SQL statment
        data = cur.fetchall()
        return data
    except Exception as e:
        print("Error:", e)
        return None
     
#Booking the Room as per the given details
def bookingRoom(request, randomNumber, price):
    try:
        name = request.form['name']
        email = request.form['email']
        check_in = request.form['check_in']
        check_out = request.form['check_out']
        room_type = request.form['room_type']
        # room_number = request.form['room_number']
        ava_status = "Booked"
        booking_notes = request.form['note']
        s='''INSERT INTO booking(roomType,randomTokenID,startTime,endTime,guestName,guestMailID,avaStatus,bookingNotes, totalPrice) VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}');'''.format(room_type,randomNumber,check_in,check_out,name,email,ava_status,booking_notes, price)
        cur.execute(s)
        mysql.commit()
        print("INsert successful")
        return "success add booking"
    except Exception as e:
        print("Error:", e)
        return None

#Booking details as per the Random ID
def bookingView(random_id):
    try:
        # random_id = request.form['random_id']
        query = '''SELECT * FROM booking WHERE randomTokenID = '{}';'''.format(random_id)
        cur.execute(query)
        data = cur.fetchall()
        print("Selected Booking Data", data)
        return data
    except Exception as e:
        print("Error:", e)
        return None

# Guest Name as per the random ID
def bookingName(random_id):
    try:
        # random_id = request.form['random_id']
        query = '''SELECT guestName FROM booking WHERE randomTokenID = '{}';'''.format(random_id)
        cur.execute(query)
        data = cur.fetchall()
        #print("Selected Booking Data", data)
        return data
    except Exception as e:
        print("Error:", e)
        return None

#Deleting the booking as per the random ID
def bookingDelete(random_id):
    try:
        s='''DELETE from booking where randomTokenID = '{}';'''.format(random_id)
        g = cur.execute(s)
        mysql.commit()
        return "success Delete"
    except Exception as e:
        print("Error:", e)
        return None

#Updating the booking as per random ID
def bookingUpdate(randomId, note):
    try:
        s='''UPDATE booking SET bookingNotes = '{}' where randomTokenID = '{}';'''.format(note,randomId)
        cur.execute(s)
        mysql.commit()
        print("Update successful")
        return "success Update"

    except Exception as e:
        print("Error:", e)
        return None

#Occupancy Rate Report for the Month
def occupancyRateResort():
    try:
        s= ("""
            SELECT
                DATE(b.startTime) AS Date,
                COUNT(b.BookingID) * 100.0 / r.TotalRooms AS OccupancyRate
            FROM
                booking b
            CROSS JOIN (
                SELECT COUNT(*) AS TotalRooms FROM room
            ) r
            WHERE
                b.startTime >= DATE_SUB(CURRENT_DATE(), INTERVAL 1 MONTH)
            GROUP BY
                DATE(b.startTime)
            ORDER BY
                Date;
            """)
        cur.execute(s)
        data = cur.fetchall()
        print("Data from Occupancy Report for the month", data)
        return data
    except Exception as e:
        print("Error:", e)
        return None
    
#Occupancy Rate as per the date range for the selected Room Type
def occupancyRateRangeResort(start_date, end_date, room_type):
    try:
        query = """
            SELECT DATE(startTime), COUNT(*)
            FROM booking
            WHERE roomType = %s
            AND startTime >= %s
            AND endTime <= %s
            GROUP BY DATE(startTime)
        """
        # Execute query with parameters
        cur.execute(query, (room_type, start_date, end_date))
        
        # Fetch the result
        occupancy_data = cur.fetchall()
        print("Data from Occ rate range resort ", occupancy_data)
        return occupancy_data
    except Exception as e:
        print("Error:", e)
        return None
