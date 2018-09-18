## Download Kafka from confluent

`cd` to `confluent-5.0.0`

# Edit properties

- `./etc/kafka/server.properties` :  modify `advertised.listeners` 
> `advertised.listeners=PLAINTEXT://localhost:9092`

## start zookeeper
`./bin/zookeeper-server-start ./etc/kafka/zookeeper.properties`

## start kafka
`./bin/kafka-server-start ./etc/kafka/server.properties
`

## create a topic with two partitions
`bin/kafka-topics  --zookeeper localhost:2181 --create --topic demo --partitions 2 --replication-factor 1`


## Running consumers & producer
- Open two terminals and run `python3 consumer.py` in each terminal
- Open another terminal and run `python3 producer.py`
## Result
The messages are processed on different consumers (partitions) based on the partitioning logic in `producer.py`  (odd and even lines). 
>  Even lines partition 0
> Odd lines - partition 1

## Shutting down

 - `Ctlr C` the kafka-server
 - `Ctlr C` the kafka-zookeeper



