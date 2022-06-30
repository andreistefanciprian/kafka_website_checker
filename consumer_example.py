# Copyright (c) 2018 Aiven, Helsinki, Finland. https://aiven.io/
from kafka import KafkaConsumer

def consumer_example(service_uri, ca_path, cert_path, key_path, kafka_topic):
    consumer = KafkaConsumer(
        bootstrap_servers=service_uri,
        auto_offset_reset='earliest',
        security_protocol="SSL",
        ssl_cafile=ca_path,
        ssl_certfile=cert_path,
        ssl_keyfile=key_path,
        consumer_timeout_ms=1000,
    )
    consumer.subscribe([kafka_topic])
    for message in consumer:
        msg = message.value.decode('utf-8')
        print(f'Message {message.offset}')
        print(msg)
    consumer.close()