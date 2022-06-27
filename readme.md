
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

# define website to test inside main.py
url = 'https://api.github.com'

# define kafka url in main.py
service_uri = "kafka-testing.aivencloud.com:13036"

# make service.key, service.cert and ca.pem available in current folder

# run script
python main.py

# deactivate python env after running the publisher/subscriber scripts
deactivate
```