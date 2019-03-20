from datetime import datetime, date
from marqeta.response_models.android_push_token_request_address import AndroidPushTokenRequestAddress
import json

class PushTokenizeRequestData(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def display_name(self):
        if 'display_name' in self.json_response:
            return self.json_response['display_name']

    @property
    def last_digits(self):
        if 'last_digits' in self.json_response:
            return self.json_response['last_digits']

    @property
    def network(self):
        if 'network' in self.json_response:
            return self.json_response['network']

    @property
    def token_service_provider(self):
        if 'token_service_provider' in self.json_response:
            return self.json_response['token_service_provider']

    @property
    def opaque_payment_card(self):
        if 'opaque_payment_card' in self.json_response:
            return self.json_response['opaque_payment_card']

    @property
    def user_address(self):
        if 'user_address' in self.json_response:
            return AndroidPushTokenRequestAddress(self.json_response['user_address'])

    def __repr__(self):
         return '<Marqeta.response_models.push_tokenize_request_data.PushTokenizeRequestData>'