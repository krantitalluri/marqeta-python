from datetime import datetime, date
import json

class KycAnswer(object):

    def __init__(self, json_response):
        self.json_response = json_response

    def __str__(self):
        return json.dumps(self.json_response, default=self.json_serial)

    @staticmethod
    def json_serial(o):
        if isinstance(o, datetime) or isinstance(o, date):
            return o.__str__()

    @property
    def answer(self):
        if 'answer' in self.json_response:
            return self.json_response['answer']

    @property
    def key(self):
        if 'key' in self.json_response:
            return self.json_response['key']

    def __repr__(self):
         return '<Marqeta.response_models.kyc_answer.KycAnswer>'