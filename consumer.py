from kafka import KafkaConsumer
from json import loads
from time import sleep
import pymongo
from pymongo import MongoClient

client = MongoClient("localhost", 27017)
db = client.test
collection = db.netflix_movies

consumer = KafkaConsumer(
    'topic_test',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group-id',
    value_deserializer=lambda x: loads(x.decode('utf-8'))
)
for event in consumer:
    event_data = event.value
    # Do whatever you want
    collection.insert_one(event_data)
    print("inserted")
    sleep(1)