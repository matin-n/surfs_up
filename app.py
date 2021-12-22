import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

# access the SQLite database
engine = create_engine("sqlite:///hawaii.sqlite")

# automap_base: automatically generates mapped classes and relationships from a database schema
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# create a session link
session = Session(engine)

# define Flask application
app = Flask(__name__)


@app.route('/')
def welcome():
    return (
        '''
        Welcome to the Climate Analysis API! \n
        Available Routes: \n
        /api/v1.0/precipitation \n
        /api/v1.0/stations \n
        /api/v1.0/tobs \n
        /api/v1.0/temp/{start}/{end} \n
        ''').replace('\n', '<br>')


@app.route("/api/v1.0/precipitation")
def precipitation():
    # calculates the date one year ago from the most recent date in the database
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    # get the date and precipitation for the previous year
    precipitation = session.query(Measurement.date, Measurement.prcp). \
        filter(Measurement.date >= prev_year).all()
    precip = {date: prcp for date, prcp in precipitation}
    session.close()
    return jsonify(precip)


@app.route("/api/v1.0/stations")
def stations():
    results = session.query(Station.station).all()
    stations_list = list(np.ravel(results))
    session.close()
    return jsonify(stations_list=stations_list)


@app.route("/api/v1.0/tobs")
def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs). \
        filter(Measurement.station == 'USC00519281'). \
        filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    session.close()
    return jsonify(temps=temps)


@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel). \
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        session.close()
        return jsonify(temps)

    results = session.query(*sel). \
        filter(Measurement.date >= start). \
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    session.close()
    return jsonify(temps)
