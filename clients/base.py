import logging

import requests


class BaseClient:

    def __init__(self):
        self.base_url = None
        self.http = requests.session()
        self.charset = 'utf-8'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'
        }
        self.logger = logging.getLogger(self.__class__.__name__)

    def run(self, **kwargs):
        raise RuntimeError

    def fetch(self, url, data=None, method='GET', params=None, **kwargs):
        kwargs.setdefault('timeout', 20)
        kwargs.setdefault('headers', self.headers)

        if data:
            method = 'POST'

        response = self.http.request(method, url, data=data, params=params, **kwargs)
        if response.ok:
            response.encoding = self.charset
            return response
        raise Exception(response.status_code, url, response.text)
