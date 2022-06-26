from kafka import KafkaProducer
import json

def json_serializer(data):
    return json.dumps(data).encode("utf-8")

def kafka_puplisher(service_uri, ca_path, cert_path, key_path, kafka_topic, data):
    producer = KafkaProducer(
        bootstrap_servers=service_uri,
        security_protocol="SSL",
        ssl_cafile=ca_path,
        ssl_certfile=cert_path,
        ssl_keyfile=key_path,
        value_serializer=json_serializer,
    )
    print(f'Publishing the following data to Kafka {kafka_topic} topic:\n{data}')
    producer.send(kafka_topic, data)
    producer.flush()