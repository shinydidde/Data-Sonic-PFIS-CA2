from flask import Flask, render_template, request
from google.auth.transport import requests
from google.cloud import datastore
import google.oauth2.id_token
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

# Dummy data for testing(you can remove this if you are fetching data from a database)
rooms_data = [
    {"id": 1, "room_number": "101", "type": "Single", "capacity": 1, "price": 100.00, "available": True},
    {"id": 2, "room_number": "102", "type": "Double", "capacity": 2, "price": 150.00, "available": False}
]

@app.route('/api/rooms', methods=['GET'])
def get_rooms():
    return jsonify(rooms_data)

# Serve index.html file
firebase_request_adapter = requests.Request()
@app.route('/login')
def index():
    cur = mysql.cursor() #create a connection to the SQL instance
    cur.execute('''SELECT * FROM room''') # execute an SQL statment
    data = cur.fetchall()
    # Verify Firebase auth.
    id_token = request.cookies.get("token")
    error_message = None
    claims = None
    times = None
    if id_token:
        try:
            # Verify the token against the Firebase Auth API. This example
            # verifies the token on each page load. For improved performance,
            # some applications may wish to cache results in an encrypted
            # session store (see for instance
            # http://flask.pocoo.org/docs/1.0/quickstart/#sessions).
            claims = google.oauth2.id_token.verify_firebase_token(
                id_token, firebase_request_adapter
            )
        except ValueError as exc:
            # This will be raised if the token is expired or any other
            # verification checks fail.
            error_message = str(exc)

        # Record and fetch the recent times a logged-in user has accessed
        # the site. This is currently shared amongst all users, but will be
        # individualized in a following step.
        store_time(datetime.datetime.now(tz=datetime.timezone.utc))
        times = fetch_times(10)

    return render_template(
        "index.html", user_data=claims, error_message=error_message, times=times, room=data
    )

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

#   app.run(host='0.0.0.0',port='8080') #Run the flask app at port 8080
  app.run(host='0.0.0.0',port='8080', ssl_context=('cert.pem', 'privkey.pem')) #Run the flask app at port 8080
