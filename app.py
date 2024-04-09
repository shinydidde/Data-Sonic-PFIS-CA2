from flask import Flask
from flask import render_template
from flask import request
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
@app.route('/')
def index():
    cur = mysql.cursor() #create a connection to the SQL instance
    cur.execute('''SELECT * FROM Room''') # execute an SQL statment
    data = cur.fetchall()
    return render_template('index.html', Room=data)

@app.route('/room/<id>')
def room(id):
   cur = mysql.cursor() #create a connection to the SQL instance
   cur.execute("SELECT * FROM Room WHERE RoomNo = %s", [id]) # execute an SQL statment
   data = cur.fetchall()
   return render_template('room.html', details=jsonify(data))

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html')

if __name__ == "__main__":

#   app.run(host='0.0.0.0',port='8080') #Run the flask app at port 8080
  app.run(host='0.0.0.0',port='8080', ssl_context=('cert.pem', 'privkey.pem')) #Run the flask app at port 8080
