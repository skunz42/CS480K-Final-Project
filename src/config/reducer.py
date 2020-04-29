"""reducer.py"""

from operator import itemgetter
import sys
import json
import pymongo
import os

def main():
    key = sys.argv[1]
    client = pymongo.MongoClient(key, w=1)
    db = client.CS480KFP
    collection = db.stores

    MIN_RATINGS = 30

    for line in sys.stdin:
        place = json.loads(line)
        if int(place['Num Ratings']) > MIN_RATINGS and "Dollar" not in place['Name']:
            db.stores.update({'ID':place['ID']}, place, upsert=True)
            print("Added: " + place['Name'])

if __name__ == "__main__":
    main()

