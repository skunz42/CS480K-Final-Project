"""mapper.py"""

import sys
import googlemaps
import json
import urllib
import csv
import pymongo
import os
from os import listdir
from os.path import isfile, join

def findPlace(lat, lng, radius, kw, key):
    #making the url
    AUTH_KEY = key #authentication key
    LOCATION = str(lat) + "," + str(lng) #location for url
    RADIUS = radius
    KEYWORD = kw #search word
    MyUrl = ('https://maps.googleapis.com/maps/api/place/nearbysearch/json'
           '?location=%s'
           '&radius=%s'
           '&keyword=%s'
           '&sensor=false&key=%s') % (LOCATION, RADIUS, KEYWORD, AUTH_KEY) #url for search term
    #grabbing the JSON result
    response = urllib.request.urlopen(MyUrl)
    jsonRaw = response.read()
    jsonData = json.loads(jsonRaw.decode('utf-8'))
    return jsonData

def abrvMapping(state):
    low = state.lower()
    retVal = ""
    if low == "alabama":
        retVal = "AL"
    elif low == "alaska":
        retVal = "AK"
    elif low == "arizona":
        retVal = "AZ"
    elif low == "arkansas":
        retVal = "AR"
    elif low == "california":
        retVal = "CA"
    elif low == "delaware":
        retVal = "DE"
    elif low == "florida":
        retVal = "FL"
    elif low == "georgia":
        retVal = "GA"
    elif low == "hawaii":
        retVal = "HI"
    elif low == "idaho":
        retVal = "ID"
    elif low == "illinois":
        retVal = "IL"
    elif low == "indiana":
        retVal = "IN"
    elif low == "iowa":
        retVal == "IA"
    elif low == "kansas":
        retVal = "KS"
    elif low == "kentucky":
        retVal = "KY"
    elif low == "louisiana":
        retVal == "LA"
    elif low == "maine":
        retVal = "ME"
    elif low == "maryland":
        retVal = "MD"
    elif low == "massachusetts":
        retVal = "MA"
    elif low == "michigan":
        retVal = "MI"
    elif low == "minnesota":
        retVal = "MN"
    elif low == "mississippi":
        retVal = "MS"
    elif low == "missouri":
        retVal = "MO"
    elif low == "montana":
        retVal = "MT"
    elif low == "nebraska":
        retVal == "NE"
    elif low == "nevada":
        retVal = "NV"
    elif low == "new hampshire":
        retVal = "NH"
    elif low == "new jersey":
        retVal = "NJ"
    elif low == "new mexico":
        retVal = "NM"
    elif low == "new york":
        retVal = "NY"
    elif low == "north carolina":
        retVal = "NC"
    elif low == "north dakota":
        retVal = "ND"
    elif low == "ohio":
        retVal = "OH"
    elif low == "oklahoma":
        retVal = "OK"
    elif low == "oregon":
        retVal = "OR"
    elif low == "pennsylvania":
        retVal = "PA"
    elif low == "rhode island":
        retVal = "RI"
    elif low == "south carolina":
        retVal = "SC"
    elif low == "south dakota":
        retVal = "SD"
    elif low == "tennessee":
        retVal = "TN"
    elif low == "texas":
        retVal = "TX"
    elif low == "utah":
        retVal = "UT"
    elif low == "vermont":
        retVal = "VT"
    elif low == "virginia":
        retVal = "VA"
    elif low == "washington":
        retVal = "WA"
    elif low == "west virginia":
        retVal = "WV"
    elif low == "wisconsin":
        retVal = "WI"
    elif low == "wyoming":
        retVal = "WY"
    return retVal

def iterJson(place):
    temp = place['plus_code']['compound_code'].split(',')
    state = ""
    if len(temp[-1].lstrip()) > 2:
        state = abrvMapping(temp[-1].lstrip())
    else:
        state = temp[-1].lstrip()

    x = {
        "Name": place['name'],
        "ID": place['reference'],
        "Latitude": place['geometry']['location']['lat'],
        "Longitude": place['geometry']['location']['lng'],
        "Address": place['vicinity'],
        "Rating": place['rating'],
        "Num Ratings": place['user_ratings_total'],
        "State": state,
        "City": place["vicinity"].split(',')[-1].lstrip()
    }
    return x

def scrapeData():
    #credsfile = open("creds/creds.txt", "r")
    #keyval = credsfile.read()
    #keyval = os.environ.get("GOOGLE_KEY")
    keyval = sys.argv[1]
    gplaces = []
    for line in sys.stdin:
        coords = eval(line)
        gsearch = findPlace(coords[0], coords[1], 1000, 'grocery', keyval)
        if gsearch['status'] == 'OK':
            for place in gsearch['results']:
                storeInfo = iterJson(place)
                gplaces.append(storeInfo)
    return gplaces

def main():
    stores = scrapeData()
    for s in stores:
        print(json.dumps(s))

if __name__ == "__main__":
    main()

