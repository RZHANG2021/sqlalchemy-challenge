import numpy as np
import datetime as dt
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

# Database setup
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base=automap_base()
# reflect the tables
Base.prepare(engine,reflect=True)

# Save references to each table
Measurement=Base.classes.measurement
Station=Base.classes.station

# Create our session (link) from Python to the DB


# Flask setup
app=Flask(__name__)

# Flask Routes

@app.route("/")
def welcome():
    return (
        f"Welcome to the Hawaii Climate Analysis API!<br/r>"
        f"Avaiable routes:<br/r>"
        f"/api/v1.0/precipitation<br/r>"
        f"/api/v1.0/stations<br/r>"
        f"/api/v1.0/tobs<br/r>"
        f"/api/v1.0/<start_date>/<end_date><br/r>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    session=Session(engine)
    """return the precipitation data for the last year"""
    # calculate the date 1 year ago from last date in database
    year_ago = dt.date(2017,8,23)-dt.timedelta(days=365)

    # Perform a query to retrieve the data and precipitation scores, and filter out the None value
    date_precipitation=session.query(Measurement.date,Measurement.prcp).\
        filter(Measurement.date>=year_ago).\
        filter(Measurement.prcp!=None).all()
    session.close()
    # Convert the query results to a dictionary using date as the key and prcp as the value
    precipitation_j={date:prcp for date,prcp in date_precipitation}
    return jsonify(precipitation_j)

@app.route("/api/v1.0/stations")
def stations():
    session=Session(engine)
    """return the sations list"""
    stations=session.query(Station.station).all()
    session.close()
    # convert station names into a normal list
    stations_list=list(np.ravel(stations))
    return jsonify(stations_list)



@app.route("/api/v1.0/tobs")
def tobs():
    session=Session(engine)
    "return the tobs data for the last year most active station"
    # Query the dates and temperature observations of the most active station for the last year of data.
    active_station_preyear=dt.date(2017,8,18)-dt.timedelta(days=365)
    active_station=session.query(Measurement.date,Measurement.tobs).\
        filter(Measurement.station=='USC00519281').\
        filter(Measurement.date>=active_station_preyear).\
        filter(Measurement.tobs!=None).all()
    session.close()
    # Convert the query results to a dictionary using date as the key and tobs as the value
    station_tobs={date:tobs for date,tobs in active_station}
    return jsonify(station_tobs)

@app.route("/api/v1.0/<start_date>")
@app.route("/api/v1.0/<start_date>/<end_date>")
def stats(start_date=None, end_date=None):
    session=Session(engine)
    """given the start date only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date."""								
    # set the required calculation   
    analysis= [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]								
    if end_date == None:
        temp_analysis =session.query(*analysis).\
            filter(Measurement.date>=start_date).all()
        # convert the result into a list and return in json form
        calculated_temp=list(np.ravel(temp_analysis))
        return jsonify(calculated_temp)
    else:
        temp_analysis =session.query(*analysis).\
            filter(Measurement.date>=start_date).\
            filter(Measurement.date>=end_date).all()
        # convert the result into a list and return in json form
        calculated_temp=list(np.ravel(temp_analysis))
        return jsonify(calculated_temp)     
    session.close()

if __name__=="__main__":
    app.run(debug=True)