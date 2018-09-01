from confluent_kafka import Producer
from time import sleep

KAFKA_TOPIC = 'demo1'
SERVER = 'localhost:9092'

conf = {
    "debug": "topic,msg,broker"
}

p = Producer({'bootstrap.servers': 'localhost:9092'})


def delivery_report(err, msg):
    """ Called once for each message produced to indicate delivery result.
        Triggered by poll() or flush(). """
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))
        
counter = 1
with open('data.txt') as f:
    for line in f:
        key = counter%2      
        p.produce(KAFKA_TOPIC, value=line.rstrip(), key=str(key), partition=key, callback=delivery_report)
        #print(line)
        counter += 1
        p.poll(0.5)

p.flush(5)
print('done')
