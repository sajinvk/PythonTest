import numpy as np # library to handle data in a vectorized manner
import pandas as pd # library for data analsysis

from geopy.geocoders import Nominatim # module to convert an address into latitude and longitude values
import requests # library to handle requests
from pandas.io.json import json_normalize # tranform json file into a pandas dataframe

import random # library for random number generation

# libraries for displaying images
from IPython.display import Image 
from IPython.core.display import HTML 

import folium # plotting library

print('Libraries imported.')

CLIENT_ID = 'UD4JURZQNJSG3WQRWH2B4GY1RFBIRKSKCRCGN3C4NZQ43YAB' # your Foursquare ID
CLIENT_SECRET = 'WG5M3SM4VDQ5XDMXNWCOUFVNQ443CO5CCCO0OVHXWX2OVV5X' # your Foursquare Secret
VERSION = '20180604'
LIMIT = 30
print('Your credentails:')
print('CLIENT_ID: ' + CLIENT_ID)
print('CLIENT_SECRET:' + CLIENT_SECRET)

address = '102 North End Ave, New York, NY'

geolocator = Nominatim()
location = geolocator.geocode(address)
latitude = location.latitude
longitude = location.longitude
print('The geographical coordinates of the Conrad Hotel are {} and {}.'.format(latitude, longitude))
