from confluent_kafka import Consumer, KafkaException, KafkaError
import sys

def print_assinment(consumer, partitions):
    print("Assignment: ", partitions)


c = Consumer({
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'confluent-client',
    'default.topic.config': {
        'auto.offset.reset': 'smallest'},
    'api.version.request': True
})

c.subscribe(['demo1'], on_assign=print_assinment)

while True:
    msg = c.poll(0.1)
    if not msg:
        # print('NO message')
        continue

    if msg.error():
         # Error or event
        if msg.error().code() == KafkaError._PARTITION_EOF:
            # End of partition event
            sys.stderr.write('%% %s [%d] reached end at offset %d\n' %
                             (msg.topic(), msg.partition(), msg.offset()))
        else:
            # Error
            raise KafkaException(msg.error())    
    else:
        print('On partiion nr. ' + str(msg.partition()))
        print(msg.value())

