from datetime import datetime, date
from marqeta.response_models.application import Application
import json

class AccessTokenResponse(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def token(self):
        if 'token' in self.json_response:
            return self.json_response['token']

    @property
    def expires(self):
        if 'expires' in self.json_response:
                return datetime.strptime(self.json_response['expires'], '%Y-%m-%dT%H:%M:%SZ')

    @property
    def application(self):
        if 'application' in self.json_response:
            return Application(self.json_response['application'])

    @property
    def tokenTypeMarqetaMaster(self):
        if 'tokenTypeMarqetaMaster' in self.json_response:
            return self.json_response['tokenTypeMarqetaMaster']

    @property
    def user_token(self):
        if 'user_token' in self.json_response:
            return self.json_response['user_token']

    @property
    def master_roles(self):
        if 'master_roles' in self.json_response:
            return self.json_response['master_roles']

    @property
    def token_type(self):
        if 'token_type' in self.json_response:
            return self.json_response['token_type']

    @property
    def one_time(self):
        if 'one_time' in self.json_response:
            return self.json_response['one_time']

    def __repr__(self):
         return '<Marqeta.response_models.access_token_response.AccessTokenResponse>'