#!/bin/bash

# test the hadoop cluster by running wordcount

python3.5 getCoords.py Binghamton NY

# create input directory on HDFS
hadoop fs -mkdir -p coords

# put input files to HDFS
hdfs dfs -put ./coords/* coords

# run wordcount 
#hadoop jar $HADOOP_HOME/share/hadoop/mapreduce/sources/hadoop-mapreduce-examples-2.7.2-sources.jar org.apache.hadoop.examples.WordCount input output
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar \
-file mapper.py -mapper "/usr/bin/python3.5 mapper.py" \
-file reducer.py -reducer "/usr/bin/python3.5 reducer.py" \
-input coords/* -output output

# print the output of wordcount
echo -e "\nwordcount output:"
hdfs dfs -cat output/part-00000

