from time import sleep
import json
from json import dumps
from kafka import KafkaProducer
import pandas as pd

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda x: dumps(x).encode('iso-8859-15')
)

df = pd.read_csv("netflix_titles.csv")
res = df.to_json(orient="records")
y = json.loads(res)

for i in y:
    print("sent")
    data = i
    producer.send("netflix_movies", value=data)
    sleep(0.2)
