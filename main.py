from neelybd_windy import *
import pandas as pd


print("Program: Windy Weather Scrapper")
print("Release: 1.0.0")
print("Date: 2021-11-09")
print("Author: Brian Neely")
print()
print()
print("This program is an example of using the neelybd windy scraper.")
print()
print()

# Set long and lat
lat = 47.7643211
long = -122.248001

# Get Data
data_dict = windy_scrapper(lat=lat, long=long, output_type='trihourly')

# Convert data dictionary to DataFrame
data_df = pd.DataFrame.from_dict(data_dict)
