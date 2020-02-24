import sys
from pyspark import SparkContext, SparkConf
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
import json
from pyspark.sql import SQLContext
from pyspark.sql.functions import countDistinct
from pyspark.sql.functions import col
import pyspark.sql.functions as fn
from pyspark.sql.functions import desc, asc
from uuid import uuid1
import os

#  Preparing the Environmen
os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages org.apache.spark:spark-streaming-kafka-0-8_2.11:2.4.5 pyspark-shell'
os.environ["PYSPARK_PYTHON"] = "/usr/local/bin/python3"
os.environ["PYSPARK_DRIVER_PYTHON"] = "/usr/local/bin/python3"

if __name__ == "__main__":
    sc = SparkContext(appName="PythonStreamingRecieverKafka") # Create Spark context
    sc.setLogLevel("ERROR")
    ssc = StreamingContext(sc, 20) #  Create Streaming Context with the batch duration of N seconds


    broker, topic = sys.argv[1:] # reading args url and topic from the command line

    kafkaStream = KafkaUtils.createStream(ssc, broker, "raw-event-streaming-consumer",{topic:1}) # Connect to Kafka and getting a dstram

    # Message Processing
    parsed = kafkaStream.map(lambda v: json.loads((v[1]))) # Parse the inbound message as json

    #simple measures on the data on the fly
    parsed.count().map(lambda x:'records in this batch: %s' % x).pprint()
    parsed.map(lambda x: x['id']).countByValue().count().map(lambda x:'users in this batch: %s' % x).pprint()
    parsed.map(lambda x: x['country']).countByValue().transform(lambda rdd:rdd.sortBy(lambda x:-x[1])).map(lambda x:'most commom country in this batch: %s' % x[0]).pprint(1)
    parsed.map(lambda x: x['country']).countByValue().transform(lambda rdd:rdd.sortBy(lambda x:x[1])).map(lambda x:'least commom country in this batch: %s' % x[0]).pprint(1)
    parsed.map(lambda x: x['email'].split("@")[1]).countByValue().transform(lambda rdd:rdd.sortBy(lambda x:-x[1])).map(lambda x:'most commom domain: %s' % x[0]).pprint(1)
    
    #Start the streaming context
    ssc.start()
    ssc.awaitTermination()