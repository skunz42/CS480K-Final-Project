import googlemaps
import json
import urllib
import sys

def calcCoords(key, coords, city):
    """
    Parameters
    ----------
    key : str?
        API authentication key
    coords : list of float tuples
        coordinates to be searched on
    city : str
        city and state name
    """

    gmaps = googlemaps.Client(key=key) #authentication
    geocode_result = gmaps.geocode(city) #gets results for city
    nelat = geocode_result[0]['geometry']['bounds']['northeast']['lat'] #northeast latitude
    nelng = geocode_result[0]['geometry']['bounds']['northeast']['lng'] #northeast longitude
    swlat = geocode_result[0]['geometry']['bounds']['southwest']['lat'] #southwest latitude
    swlng = geocode_result[0]['geometry']['bounds']['southwest']['lng'] #southwest longitude
    km = 0.015

    templat = swlat #latitude and longitude used for calculation purposes
    templng = swlng

    while (templat <= nelat): #north/south calc
        while (templng <= nelng): #east/west calc
            coords.append((templat, templng))
            templng += km # ~ 1 km
        templng = swlng
        templat += km # ~ 1 km

def writeToFile(coords, city, state):
    """
    Parameters
    ----------
    coords : list of float tuples
        coordinates to be searched on
    city : str
        city name
    state : str
        state name
    """

    fileCount = 0
    inFileCount = 0
    currentFn = "coords/" + city + state + str(fileCount)
    f = open(currentFn, "w")
    for c in coords:
        f.write(''.join(str(c)))
        f.write("\n")
        inFileCount += 1
        if inFileCount > 14:
            inFileCount = 0
            fileCount += 1
            f.close()
            f = open("coords/" + city + state + str(fileCount), "w")

def main():
    if len(sys.argv) != 3:
        print("Enter in format python <city> <state>")
        sys.exit(1)
        
    city = str(sys.argv[1])
    state = str(sys.argv[2])
    citystate = city + ", " + state

    credsfile = open("creds.txt", "r")
    keyval = credsfile.read()
    coords = []
    calcCoords(keyval, coords, citystate)
    writeToFile(coords, city, state)
main()
