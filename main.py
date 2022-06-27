from website_checker import WebsiteChecker
from publisher import kafka_puplisher
import os

if __name__ == '__main__':

    # define variables
    url = 'https://api.github.com'
    service_uri = "kafka-testing-andreistefanciprian-f7f4.aivencloud.com:13036"
    ca_path = os.path.join(os.getcwd(), "ca.pem")
    cert_path = os.path.join(os.getcwd(), "service.cert")
    key_path = os.path.join(os.getcwd(), "service.key")

    # check website availability
    check = WebsiteChecker(url)

    # publish data to kafka topic
    kafka_topic = "python_example_topic"
    kafka_puplisher(service_uri, ca_path, cert_path, key_path, kafka_topic, check.website_data)   


