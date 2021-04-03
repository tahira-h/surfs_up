
# Import the Flask Dependency
from  flask import Flask
# Create a New Flask App
#app = Flask(__name__)
# Create Flask Routes, create a function called hello_world.
# Note: Whenever making a route in Flask, put the code wanted in the specific route below.
#@app.route('/')
#def hello_world():
#    return 'Hello world'

# Import Dependencies
import datetime as dt
import numpy as np
import pandas as pd

# SQLAlchemy dependencies
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# Import dependencies for Flask
from flask import Flask, jsonify

# Set up the database, to access the SQLite database
engine = create_engine("sqlite:///hawaii.sqlite")

# Reflect the database into our classes.
Base = automap_base()
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create a session link from Python to our database
session = Session(engine)

# Set up Flask

# Define the Flask app, called "app"
app = Flask(__name__)


# The __name__ variable is a special type of variable in Python. It's value depends on where and how the code is run.
# Ex, if importing "app.py file" into another Python file named example.py, the variable __name__ would be set to example.
# NOTE: When running the script with python app.py the __name__ variable will be set to __main__. This indicates we are not using any other file to run this code.

# CREATE THE WELCOME ROUTE

# Define welcome route


# Add the routing information for each of the other routes 

#Create a welcome() function and the return statement.
# Add precipitation, stations, tobs, and temp routes that's needed into the return statment 
#def welcome()

@app.route("/")
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')
    

# NOTE: 
# When creating routes, follow the naming convention '/api/v1.0/' followed by the name of the route. This convention signifies that this is a version 1 of the application.This line can be updated to support future versions of the app as well. 


#Precipitation Route

# Steps:
# 1. Create the route ("/api")
# 2. Create precipitation function().   return line in 2nd line 
# 3. Calculate the date one year ago from the most recent date after precipitation function().  prev_year = dt.date...   #return in 3rd line now
# 4. Write a query to get the date and precipitation for the previous year. precipitation = session.query...indented line underneath filter()   # return is now in next line
# 5. Create a dictionary with the date as the key and the precipitation as the value. 
#   To do this, "jsonify" the dictionary. 'Jsonify()' is a function that converts the dictionary to a JSON file. 
#   this will be an addition to the line of code for "return"
 
@app.route("/api/v1.0/precipitation")
def precipitation():
   prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   precipitation = session.query(Measurement.date, Measurement.prcp).\
       filter(Measurement.date >= prev_year).all() 
   return jsonify(precipitation)

# Stations Route

@app.route("/api/v1.0/stations")
def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)

# Monthly Temperature Route

@app.route("/api/v1.0/tobs")
def temp_monthly():
   prev_year = dt.date(2017.8, 23) - dt.timedelta(days=365)
   results = session.query(Measurement.tobs).\
       filter(Measurement.station == 'USC00519281').\
       filter(Measurement.date) >= prev_year.all()
   temps = list(np.ravel(results))
   return jsonify(temps=temps)




