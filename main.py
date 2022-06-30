#!/usr/bin/env python3
# Copyright (c) 2018 Aiven, Helsinki, Finland. https://aiven.io/

import argparse
import os
import sys
from website_checker import WebsiteChecker
from publisher import kafka_puplisher
from consumer_example import consumer_example

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--service-uri', help="Service URI in the form host:port",
                        required=True)
    parser.add_argument('--ca-path', help="Path to project CA certificate",
                        required=True)
    parser.add_argument('--key-path', help="Path to the Kafka Access Key (obtained from Aiven Console)",
                        required=True)
    parser.add_argument('--cert-path', help="Path to the Kafka Certificate Key (obtained from Aiven Console)",
                        required=True)
    parser.add_argument('--website', help="Specify website to be checked.")
    parser.add_argument('--consumer', action='store_true', default=False, help="Run Kafka consumer example")
    args = parser.parse_args()
    validate_args(args)

    kafka_topic = 'website_monitor'

    if args.website:
        # check website availability
        data = WebsiteChecker(args.website)
        data = data.website_data
        # publish data to kafka topic
        kafka_puplisher(args.service_uri, args.ca_path, args.cert_path, args.key_path, kafka_topic, data) 
    elif args.consumer:
        # consuming data from kafka topic
        consumer_example(args.service_uri, args.ca_path, args.cert_path, args.key_path, kafka_topic)

def validate_args(args):
    for path_option in ("ca_path", "key_path", "cert_path"):
        path = getattr(args, path_option)
        if not os.path.isfile(path):
            fail(f"Failed to open --{path_option.replace('_', '-')} at path: {path}.\n"
                 f"You can retrieve these details from Overview tab in the Aiven Console")
    if args.website and args.consumer:
        fail("--website and --consumer are mutually exclusive")
    elif not args.website and not args.consumer:
        fail("--website or --consumer are required")

def fail(message):
    print(message, file=sys.stderr)
    exit(1)

if __name__ == '__main__':
    main()

  
