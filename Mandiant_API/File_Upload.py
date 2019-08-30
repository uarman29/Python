# -*- coding: utf-8 -*-
import hashlib
import hmac
import email
import time
import json
import requests

class APIRequestHandler(object):

    def __init__(self):
        self.URL = 'https://api.isightpartners.com'
        self.public_key = 'bd91d6dfd1956f4041c346524039fda70a024d4bbae694eb97c73b124b61ad1f'
        self.private_key = 'd2759dd0ac5f9cb039f341a90b73895643e36fa8bb2809a1215e3352e14d5368'
        self.accept_version = '2.6'

    def run(self):
        time_stamp = email.utils.formatdate(localtime=True)
        ENDPOINT = '/report/16-00038875'
        accept_header = 'application/json'
        new_data = ENDPOINT + self.accept_version + accept_header + time_stamp
        print(new_data)

        key = bytearray()
        key.extend(map(ord, self.private_key))
        hashed = hmac.new(key, new_data.encode('utf-8'), hashlib.sha256)

        headers = {
            'Accept': accept_header,
            'Accept-Version': self.accept_version,
            'X-Auth': self.public_key,
            'X-Auth-Hash': hashed.hexdigest(),
            'Date': time_stamp,
            }

        r = requests.get(self.URL + ENDPOINT, headers=headers)
        status_code = r.status_code
        print('status_code = ' + str(status_code))

        if status_code == 200:
            print(r.text)
            f = open('response.txt', 'w')
            f.write(r.text)
            f.close()

        else:
            print(r.content)


if __name__ == '__main__':
    request_handler = APIRequestHandler()
    request_handler.run()