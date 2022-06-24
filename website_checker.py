"""
This is a script that checks websites for connectivity and collects the following things:
- Total response time
- HTTP status code, if the request completes successfully
- Whether the response body matches an optional regex check that can be passed as config to the program
"""

import requests
from http.client import HTTPConnection
from urllib.parse import urlparse

class WebsiteChecker:

    """
    Check website connectivity, collects HTTP status code and response time in milliseconds.
    """

    def __init__(self, url=None, timeout=None):
        self.url = url
        self.timeout = 2 if timeout is None else timeout
        self.response_time = None
        self.status_code = None
        self.connection = self._site_is_online()

    def _site_is_online(self):
        """
        Returns True if the target URL is online.
        """
        
        result = False
        parser = urlparse(self.url)
        host = parser.netloc or parser.path.split("/")[0]

        for port in (80, 443):
            connection = HTTPConnection(host=host, port=port, timeout=self.timeout)
            try:
                connection.request("HEAD", "/")
            except Exception as e:
                print(f'Unable to connect to url {self.url}\n{e}')
            else:
                result = True
            finally:
                connection.close()
                
        return result

    def website_checker(self):
        """
        Returns HTTP Response Code and Time if the target URL is online.
        """

        if self.connection:
            try:
                response = requests.head(self.url, timeout=self.timeout)
            except Exception as e:
                print(f'Unable to connect to url {self.url}\n{e}')
            else:
                self.status_code = response.status_code
                latency = response.elapsed
                self.response_time = f'{round(latency.total_seconds() * 1000)} ms'