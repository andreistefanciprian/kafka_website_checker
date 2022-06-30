"""
This is a script that checks websites for connectivity and collects the following data:
- Total response time
- HTTP status code, if the request completes successfully
- Whether the response body matches an optional regex check that can be passed as config to the program
"""

import requests
from http.client import HTTPConnection
from urllib.parse import urlparse
from requests.exceptions import HTTPError
import re

class WebsiteChecker:
    """
    Check website connectivity, collects HTTP status code, response time in milliseconds and response body.
    """

    def __init__(self, url=None, timeout=None):
        self.url = url
        self.timeout = 2 if timeout is None else timeout
        self._site_is_online = self._site_is_online()
        self.http_status_code = self._get_status_code()
        self.http_response_time = self._get_response_time()
        self.http_body = self._get_response_body()
        self.website_data = {
        "URL": self.url,
        "HTTP_Status_Code": self.http_status_code,
        "HTTP_Response_Time": self.http_response_time,
        "Config": self.http_body,
        }

    def _site_is_online(self):
        """
        Returns True if the target URL is online.
        """
        try:
            self._response = requests.get(self.url, timeout=self.timeout)
            # If the response was successful, no Exception will be raised
            self._response.raise_for_status()
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        except Exception as err:
            print(f'Other error occurred: {err}')
        else:
            return True

    def _get_status_code(self):
        """
        Returns HTTP Status Code.
        """
        result = None
        if self._site_is_online:

            return self._response.status_code
        else:
            return None

    def _get_response_time(self):
        """
        Returns HTTP Response Time.
        """
        result = None
        if self._site_is_online:
            latency = self._response.elapsed
            result =  f'{round(latency.total_seconds() * 1000)} ms'
            return result
        else:
            return result

    def _get_response_body(self):
        """
        Returns HTTP Response Body if:
         - site is online
         - status code is 2xx or 3xxx
         - http body matches regex
        """
        result = None

        if self._site_is_online and re.search("^[2,3]\d{2}$", str(self.http_status_code)):
            http_body = str(self._response.text)
            check_regex = re.findall("emojis_url", http_body)
            if check_regex:
                result = self._response.text
            return result

        else:
            return result