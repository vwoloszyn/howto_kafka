import sys,os
from kafka import KafkaProducer
from kafka.errors import KafkaError
import time
import json

producer = KafkaProducer(bootstrap_servers="localhost:9092")
topic = "test"

def read_file(fileName):
    with open(fileName) as json_file:
        contents = json.load(json_file)


        for content in contents:
            json_dump=json.dumps(content).encode('utf-8')
            print (json_dump)
            future = producer.send(topic,json_dump)
            try:
                future.get(timeout=10)
            except KafkaError as e:
                print(e)
                break
            print('.',end='',flush=True)
            time.sleep(0.2)

    print('done')       


if __name__== '__main__':
    read_file('mock_data.json')