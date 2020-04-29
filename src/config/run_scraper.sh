#!/bin/bash

if [ "$#" -ne 2 ]
then
    echo "Usage: $0 CityName StateAbbrev"
    exit 1
fi

source ./set_vars.sh

python3.5 getCoords.py $1 $2

# create input directory on HDFS
hadoop fs -mkdir -p coords
hadoop fs -mkdir -p creds

# put input and credential files to HDFS
hdfs dfs -put ./coords/* coords

hdfs dfs -put ./creds/* creds

echo "Starting hadoop scraping..."

# run scraper
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar \
-file mapper.py -mapper "/usr/bin/python3.5 mapper.py $GOOGLE_KEY" \
-file reducer.py -reducer "/usr/bin/python3.5 reducer.py $DB_KEY" \
-input coords/* -output output

# print the output of wordcount
echo -e "\ninformation gathered:"
hdfs dfs -cat output/part-00000

