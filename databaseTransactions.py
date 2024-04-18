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


#Room Booking DB
def roomBookingView(startDate, endDate):
    s = '''SET @start_time = '{}'; SET @end_time = '{}'; SELECT r.roomType, r.available - COALESCE(b.total_bookings, 0) AS available_rooms FROM room r LEFT JOIN ( SELECT roomType, COUNT(*) AS total_bookings FROM booking WHERE (startTime <= @end_time AND endTime >= @start_time) GROUP BY roomType) b ON r.roomType = b.roomType;'''.format(startDate, endDate)
    cur.execute(s)
    data = cur.fetchall()
    print("Room Booking Select data range", data)
    return data