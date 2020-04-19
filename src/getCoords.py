import googlemaps
import json
import urllib
import sys

'''***********************************************
                    calcCoords
    purpose:
        calculates the coordinates to use when
        searching. Updates an array of tuples
        storing coordinates
    params:
        key - API authentication key
        coords - array of coordinates
        city - city being searched
    return:
        None
***********************************************'''
def calcCoords(key, coords, city):
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

'''***********************************************
                    Main
***********************************************'''
def main():
    city = str(sys.argv[1])
    state = str(sys.argv[2])
    citystate = city + ", " + state

    credsfile = open("../../Geo-Credentials/creds.txt", "r")
    keyval = credsfile.read()
    coords = []
    calcCoords(keyval, coords, citystate)
    print(coords)
main()
