
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

# run script
python main.py

# deactivate python env after running the publisher/subscriber scripts
deactivate
```