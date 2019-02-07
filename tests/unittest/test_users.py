import unittest
from unittest import mock
from marqeta.users import UsersCollection
from marqeta import Client


class UsersCollectionTest(unittest.TestCase):

    def setUp(self):
        self.client = Client('','','')
        self.users_collection = UsersCollection(self.client)

    ''' method for mocking the marqeta.client.get method'''

    def mocked_requests_get(*args):
        class MockResponse:
            def __init__(self, json_data, status_code):
                self.json_data = json_data
                self.status_code = status_code

        class MockError:
            def __init__(self, error_message, error_code):
                self.error = error_message
                self.code = error_code

        if args[0] == 'test_endpoint':
            mock_response = MockResponse({'test_name': 'name'}, 200)
            return MockResponse({"test_name": "name"}, 200)

        return MockError("General Conflict", 400003)

    class MockUserResource(object):

        data = {'first_name': 'test_name'}

        def __init__(self):
            self.response = self.data




    ''' This test method id mocking the client.get method testing it '''

    @mock.patch('marqeta.Client.get', side_effect=mocked_requests_get)
    def test_page(self, mock_page):
        # self.client = Client()
        # self.users_collection = UsersCollection(self.client)

        self.assertTrue(self.client.get('test_endpoint123').error, {'General Conflict'})
        self.assertTrue(self.client.get('test_endpoint').json_data, {'test_name': 'name'})

    # page_response =self.users_collection.__page('test_count', 'test_index')

    # #@mock.patch('UserResource', return_value = object)
    # #@mock.patch('__page',return_value = {'count':5})
    # def test_list(self,mock_list):
    #     response = self.users_collection.list()
    #     response.__page('test_count', 'test_index')
    #     self.assertTrue(response is not None)



    @mock.patch('self.users_collection.create', side_effect= MockUserResource())
    def test_create(self, mock_data):
        data = {'first_name': 'test_name'}
        created_user = self.users_collection.create(data)
        print(created_user)



if __name__ == '__main__':
    unittest.main()
