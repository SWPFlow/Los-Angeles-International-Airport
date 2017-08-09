# Los-Angeles-International-Airport
A script for processing traffic data of Los Angeles International Airport


Consider the Los Angeles International Airport (LAX) traffic data “lax.json”(provided to you in the same folder as this handout). This JSON data file lists the number of passengers who departed from or arrived at LAX terminals at the first day of each month, starting from January, 2006 to November, 2016. For example, the 5th record says there were 401,535 people arriving at Terminal 1 on 1/1/2006 through domestic flights.


a Python 2.7 script “lax.py” that takes “lax.json” and a list of keywords (that specify the search condition) as the input, and outputs (prints to screen rather than writes to a file) the following statistics for the records that satisfy the search condition: min, max, median, average, and standard deviation (comprises only numbers exactly in this order and separated by commas). For example, min is the minimum number of passengers among all qualified records.


The keywords in the list are separated by white spaces and may only contain keywords of 3 categories: terminal, year, and traffic type (departure/arrival).


 Accepted keywords for terminals are: T1 (for terminal 1), T2, ..., T6, and TBI (for Tom Bradley international terminal). Keywords are case-insensitive. “t1” should be recognized the same as “T1”, for example.
 Year is a four-digit number, e.g., 2006.
 Traffic type is either departure or arrival.
