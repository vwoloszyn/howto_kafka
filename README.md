A simple Producer and Consumer for Kafka

# 1. Preparing the Environment

## 1.1 downloading Apache Kafka 
Check https://kafka.apache.org/quickstart for
references.
```
wget https://downloads.apache.org/kafka/2.4.0/kafka_2.12-2.4.0.tgz
tar -xzf kafka_2.12-2.4.0.tgz
cd kafka_2.12-2.4.0
```

## 1.2 Starting the servers
Kafka uses ZooKeeper so you need to first start a ZooKeeper server if you don't already have one. You can use the convenience script packaged with kafka to get a quick-and-dirty single-node ZooKeeper instance.

```
bin/zookeeper-server-start.sh config/zookeeper.properties
bin/kafka-server-start.sh config/server.properties
```

## 1.3 creating the topic
```
#Let's create a topic named "test" used in this example with a single partition and only one replica:
bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic test
```

# 2. Executing the code

## 2.0 installing requirements 
```
Run pip install -r requirements.txt
```


## 2.1 Executing the producer 
It will take input from a file and send it out as messages to the Kafka cluster. By default, each line will be sent as a separate message.

Run the producer and then type a few messages into the console to send to the server. 
```
python producer.py localhost:9092 test mock_data.json
```

## 2.2 Executing the consumer 
Getting Started with Spark Streaming with Python and Kafka

Spark Streaming provides a way of processing "unbounded" data - commonly referred to as "streaming" data. It does this by breaking it up into microbatches, and supporting windowing capabilities for processing across multiple batches.


```
python spark_stream_consumer.py localhost:2181 test
```


this example use operations of map/reduce/transform over a dstram object for calculating:
1)users in this batch
2)most commom country
3)least commom country
4)mmost commom domain
```
parsed.map(lambda x: x['id']).countByValue().count().map(lambda x:'users in this batch: %s' % x).pprint()
parsed.map(lambda x: x['country']).countByValue().transform(lambda rdd:rdd.sortBy(lambda x:-x[1])).map(lambda x:'most commom country in this batch: %s' % x[0]).pprint(1)
parsed.map(lambda x: x['country']).countByValue().transform(lambda rdd:rdd.sortBy(lambda x:x[1])).map(lambda x:'least commom country in this batch: %s' % x[0]).pprint(1)
parsed.map(lambda x: x['email'].split("@")[1]).countByValue().transform(lambda rdd:rdd.sortBy(lambda x:-x[1])).map(lambda x:'most commom domain: %s' % x[0]).pprint(1)
```
