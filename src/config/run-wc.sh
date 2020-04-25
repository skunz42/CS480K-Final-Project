#!/bin/bash

# test the hadoop cluster by running wordcount

# create input directory on HDFS
hadoop fs -mkdir -p coords

# put input files to HDFS
hdfs dfs -put ./coords/* coords

# run wordcount 
#hadoop jar $HADOOP_HOME/share/hadoop/mapreduce/sources/hadoop-mapreduce-examples-2.7.2-sources.jar org.apache.hadoop.examples.WordCount input output
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar \
-file mapper.py -mapper mapper.py \
-file reducer.py -reducer reducer.py \
-input coords/* -output output

# print the output of wordcount
echo -e "\nwordcount output:"
hdfs dfs -cat output/part-00000

