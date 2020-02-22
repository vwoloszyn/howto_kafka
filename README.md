# howto_kafka
A simple Producer and Consumer for Kafka

# install Apache Kafka locally 
Check https://kafka.apache.org/quickstart for
references.
## downloading
```
wget https://downloads.apache.org/kafka/2.4.0/kafka_2.12-2.4.0.tgz
tar -xzf kafka_2.12-2.4.0.tgz
cd kafka_2.12-2.4.0
```

## Start the server
```
# Kafka uses ZooKeeper so you need to first start a ZooKeeper server
bin/zookeeper-server-start.sh config/zookeeper.properties
# Now start the Kafka server:
bin/kafka-server-start.sh config/server.properties
```

## creating the topic
```
#Let's create a topic named "test" with a single partition and only one replica:
bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic test
```
