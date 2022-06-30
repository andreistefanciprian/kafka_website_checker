
## Description

This is a program that:
- checks website for connectivity
- collects HTTP Status Code
- collects HTTP Respose Time
- collects config in HTTP Respose Body, if it matches regex
- sends all above data to a Kafka topic

## Run script

```bash
# create python3 virtual env
python3 -m venv venv

# activate python env
source venv/bin/activate

# install pip packages
pip install -r requirements.txt

# to publish to kafka topic, make sure you have a service URI to connect to along with certificates (service.key, service.cert and ca.pem)
# make kafka certificates available in current folder
# create kafka topic, website_monitor ( kafka_topic = 'website_monitor' defined in main.py)
# check website and publish collected data to kafka topic, website_monitor

python main.py --service-uri kafka-testing-andreistefanciprian-f7f4.aivencloud.com:13036 \
--ca-path ca.pem \
--key-path service.key \
--cert-path service.cert  \
--website 'https://api.github.com'

# get data from kafka topic
python main.py --service-uri kafka-testing-andreistefanciprian-f7f4.aivencloud.com:13036 \
--ca-path ca.pem \
--key-path service.key \
--cert-path service.cert \
--consumer

# deactivate python env after running the publisher/subscriber scripts
deactivate
```
