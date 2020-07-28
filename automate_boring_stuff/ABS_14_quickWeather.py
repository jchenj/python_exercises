#! /usr/bin/python3
# ABS_14_quickWeather.py -> Prints the weather for a location on the command
# line for 9:00 am on the next three days/ 

import json
import requests
import sys

# Compute the location from command line arguments
if len(sys.argv) < 2:
    print('Usage: ABS_14_quickWeather.py location')
    sys.exit()
location = ' '.join(sys.argv[1:])

APPID = '4ff771b5837cb1e7ca881f584afbda45'

# Download the JSON weather data from OpenWeatherMap.org's API
url = 'http://api.openweathermap.org/data/2.5/forecast?q=' + location + '&APPID=' + APPID
print(url)
response = requests.get(url)
response.raise_for_status()

# Load the JSON data into a Python variable
weatherData = json.loads(response.text)

# Print weather descriptions
w = weatherData['list']
print('Tomorrow\'s weather in %s:' % (location))
print(w[3]['dt_txt'])
print(w[3]['weather'][0]['main'],'-', w[3]['weather'][0]['description'])
print()
print('Day after tomorrow:')
print(w[11]['dt_txt'])
print(w[11]['weather'][0]['main'],'-', w[11]['weather'][0]['description'])
print()
print('Two days after tomorrow:')
print(w[19]['dt_txt'])
print(w[19]['weather'][0]['main'],'-', w[19]['weather'][0]['description'])
print()

