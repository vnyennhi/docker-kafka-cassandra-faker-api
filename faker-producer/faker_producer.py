"""Produce openweathermap content to 'weather' kafka topic."""
import asyncio
import configparser
import os
import time
from collections import namedtuple
from dataprep.connector import connect
from kafka import KafkaProducer
import json
from faker import Faker

fake = Faker()

def get_registered_user():
    return {
        "name": fake.name(),
        "address": fake.address(),
        "year": fake.year()
    }

KAFKA_BROKER_URL = os.environ.get("KAFKA_BROKER_URL")
TOPIC_NAME = os.environ.get("TOPIC_NAME")


def run():
    kafkaurl = KAFKA_BROKER_URL
    iterator = 0
    print("Setting up Faker producer at {}".format(kafkaurl))
    producer = KafkaProducer(
        bootstrap_servers=kafkaurl,
        # Encode all values as JSON
        value_serializer=lambda x: json.dumps(x).encode('utf8'),
    )

    while True:
        registered_user = get_registered_user()
        # adding prints for debugging in logs
        print("Sending new faker data iteration - {}".format(iterator))
        producer.send(TOPIC_NAME, value=registered_user)
        print("New data sent")
        time.sleep(5)
        print("Waking up!")
        iterator += 1


if __name__ == "__main__":
    run()
