'''Module includes methods for connecting and retrieving data in
   accounting program API and retriving data from there.'''
from datetime import datetime
import json
import hmac
import hashlib
from base64 import b64encode
import requests

class MeritAktiva():

    '''Class for MeritAktiva API methods'''

    def __init__(self, api_id: str, api_key: str):
        '''Defining basic settings for class.
           api_id: str, obtained in MeritAktiva company logged page
           api_key: str, obtained in MeritAktiva company logged page
           '''
        self.api_id = api_id
        self.api_key = api_key
        self.entry_point = 'https://aktiva.meritaktiva.fi/api/v1/'

    def get(self, api_address: str, api_arguments: dict)-> requests.Response:
        """api_address: str, URL-address to api,
        api_arguments: dict, arguments sent to api
        returns: requests.Response object in json format"""

        time_stamp = datetime.now().strftime("%Y%m%d%H%M%S")
        json_request = json.dumps(api_arguments, separators=(',', ':'))

        data_string = self.api_id + time_stamp + json_request
        hashed = hmac.new(
            bytes(self.api_key, 'utf-8'),
            msg=bytes(data_string, 'utf-8'), digestmod=hashlib.sha256).digest()
        signature = b64encode(hashed).decode('utf-8')

        url = self.entry_point + api_address \
            + '?ApiId=' + self.api_id \
            + '&timestamp=' + time_stamp \
            + '&signature=' + signature

        response = requests.get(
            url=url,
            json=True,
            headers={'content-type': 'application/json'},
            data=json_request
            )

        # Returning Python object
        response = json.loads(response.json())

        return response

    def push(self):
        '''Method pushes data via MeritAktiva API'''
