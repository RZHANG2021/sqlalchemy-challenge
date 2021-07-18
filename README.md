# sqlalchemy-challenge

Background

To utilize Python and SQLAlchemy to proform analysis and data exploration on the provided climate database. All of the analysis is required to be completed using SQLAlchemy ORM queries, Pandas, and Matplotlib.

The challenge separated into 4 sessions:

First session:

1.1 Climate Analysis and Exploration:

-Explore the provided data set and locate the most recent date

-Based on the most recent date, retrieve the last 12 months of precipitation data, clear the data retrieved and sort the data by dates

-Load the data into a Pandas DataFrame and set the index to the date column, plot the results using DataFrame plot method. 


-And print the summary statistics for the precipitation data.


1.2 Station Analysis

-Design a query to calculate the total number of stations in the dataset.

-Design a query to fid the most active satations (ie which station has the most rows?)

o List the stations and observation counts in descending order
       
o Find out Which station id has the highest number of observations

o Using the most active station id, calculate the lowest, highest, and average temperature

-Design a query to retrieve the last 12 months of temperature observation data (TOBS).
o Filter by the station with the highest number of observations

o Query the last 12 months of temperature observation data for this station

o Plot the results as a histogram with bins=12.


The 2nd Session: Climate App


Design a Flask API based on the queries that you have just developed.
Use Flask to create routes needed.

Routes
o /
Home page.
List all routes that are available.

o /api/v1.0/precipitation
Convert the query results to a dictionary using date as the key and prcp as the value
Return the JSON representation of your dictionary

o /api/v1.0/stations
Return a JSON list of stations from the dataset

/api/v1.0/tobs
Query the dates and temperature observations of the most active station for the last year of data

Return a JSON list of temperature observations (TOBS) for the previous year.

o /api/v1.0/<start> and /api/v1.0/<start>/<end>
Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.

When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.

When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.

       
The 3rd Session:
       
       
3.1 Temperature Analysis I

-Hawaii is reputed to enjoy mild weather all year. Is there a meaningful difference between the temperature in, for example, June and December?

Utilize pandas to perform the analysis:

-Convert the date column format from string to datetime.

-Set the date column as the DataFrame index

-Identify the average temperature in June and December at all stations across all available years in the dataset. 

-Use the t-test to determine whether the difference in the means, if any, is statistically significant. Would a paired t-test, or an unpaired t-test is more suitable? Why?

3.2 Temperature Analysis II

If planning a trip in between August first to August seventh of this year, would the weather be ideal. Using historical data in the dataset find out what the temperature has previously looked like.
-Use the function called calc_temps to use input start date and end date in the format %Y-%m-%d. and return the minimum, average, and maximum temperatures for the trip  range of dates.
-Plot the min, avg, and max temperature from the previous query as a bar chart.
o Use "Trip Avg Temp" as the title.

o Use the average temperature as the bar height (y value)


o Use the peak-to-peak (TMAX-TMIN) value as the y error bar (YERR).
o 

3.3 Daily Rainfall Average
To check and see what the rainfall has been:
-Calculate the rainfall per weather station using the previous year's matching dates.
-Sort this in descending order by precipitation amount and list the station, name, latitude, longitude, and elevation.
3.4 Daily Temperature Normals

Calculate the daily normals for the duration of the trip planed. 

Normals are the averages for the min, avg, and max temperatures. Using the provided function called daily_normals, which calculate the daily normals for a specific date. This date string needs to be in the format %m-%d. Ensure to use all historic TOBS that match that date string.

-Set the start and end date of the trip.

-Use the date to create a range of dates.

-Strip off the year and save a list of strings in the format %m-%d.

-Use the daily_normals function to calculate the normals for each date string and append the results to a list called normals.

-Load the list of daily normals into a Pandas DataFrame and set the index equal to the date.

-Use Pandas to plot an area plot (stacked=False) for the daily normals.

