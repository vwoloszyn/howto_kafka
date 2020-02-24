import sys,os
from kafka import KafkaProducer
from kafka.errors import KafkaError
import time
import json


if __name__== '__main__':
     broker, topic, fileName = sys.argv[1:]
     producer = KafkaProducer(bootstrap_servers=str(broker))

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
