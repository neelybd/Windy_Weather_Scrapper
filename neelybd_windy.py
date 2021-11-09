from urllib.request import urlopen
import json


# print("Function: neelybd_windy")
# print("Release: 1.0.0")
# print("Date: 2021-11-09")
# print("Author: Brian Neely")
# print()
# print()
# print("These functions are used to scrape weather data from Windy.")
# print("The windy_scrapper will get weather data using Lat and Longs of a specific location, and return the 150 hour "
#       "forcast unsing either GFS or ECMWF.")
# print("The output type can be specified for a dictionary of all data; "
#       "dictionary of header information such as Time Zone, etc;"
#       "dictionary of celestial information such as Sunrise;"
#       "dictionary of daily weather data;"
#       "dictionary of trihourly weather data.")
# print()
# print()


def windy_scrapper(lat, long, forcast_in='gfs', output_type='all'):
    # Check forcast type
    if forcast_in.lower()[:2] == 'ec':
        forcast = 'ecmwf'
    elif forcast_in.lower()[:2] == 'gf':
        forcast = 'gfs'
    else:
        print('Forcast type is invalid, defaulting to GFS')
        forcast = 'gfs'

    # URL String
    url_str = 'https://node.windy.com/forecast/v2.1/{forcast_str}/{lat_str}/{long_str}'

    # Format URL
    url_str_format = url_str.format(forcast_str=forcast,
                                    lat_str=str(lat),
                                    long_str=str(long))

    # Read URL data
    data = urlopen(url_str_format).read()

    # Decode and convert JSON to dict
    data_dict = json.loads(data.decode('UTF-8'))

    # Output Data
    if output_type.lower() == 'all':
        print("Returning dictionary of results")
        return data_dict

    # Get Header
    data_header_dict = data_dict['header']

    # Get Celestial
    data_celestial_dict = data_dict['celestial']

    # Get Daily Summary
    data_daily_dict = data_dict['summary']

    # Get Data
    data_trihourly_dict = data_dict['data']

    # Output Data
    if output_type.lower() == 'header':
        print("Returning header")
        return data_header_dict
    elif output_type.lower() == 'celestial':
        print("Returning celestial")
        return data_celestial_dict
    elif output_type.lower() == 'daily':
        print("Returning daily")
        return data_daily_dict
    elif output_type.lower() == 'trihourly':
        print("Returning trihourly")
        return data_trihourly_dict
    else:
        print("Invalid output type... Returning all")
        return data_dict
