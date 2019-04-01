#!/usr/bin/env python3

from marqeta.resources.collection import Collection
from marqeta.response_models.campaign_response_model import CampaignResponseModel
from marqeta.response_models.store_model import StoreModel


class CampaignsCollection(object):
    '''
    Marqeta API 'campaigns' endpoint list, create, find and update operations
    '''
    _endpoint = 'campaigns'

    def __init__(self, client):
        '''
        Creates a client collection object
        :param client: client object
        '''
        self.client = client
        self.collections = Collection(self.client, CampaignResponseModel)

    def __call__(self, token):
        '''
        Special case call made with token
        :param token: campaigns token
        :return: CampaignsContext object
        '''
        return CampaignsContext(token, self.client)

    def page(self, count=5, start_index=0):
        '''
        Provides the requested page for campaigns
        :param count: data to be displayed per page
        :param start_index: start_index
        :return: requested page with CampaignResponseModel object for the requested
        page 'data'field
        '''
        return self.collections.page(endpoint=self._endpoint, count=count, start_index=start_index)

    def stream(self, params=None):
        '''
        Stream through the list of requested endpoint data field
        :param params: query parameters
        :return: CampaignResponseModel object
        '''
        return self.collections.stream(endpoint=self._endpoint, query_params=params)

    def list(self, params=None, limit=None):
        '''
        List all the campaigns
        :param params: query parameters
        :param limit: parameter to limit the list count
        :return: List of CampaignResponseModel object:
        '''
        return self.collections.list(endpoint=self._endpoint, query_params=params, limit=limit)

    def create(self, data, params=None):
        '''
        Creates an campaigns object
        :param data: data required for creation
        :param params: query parameters
        :return: CampaignResponseModel object
        '''
        return self.collections.create(endpoint=self._endpoint, query_params=params, data=data)

    def find(self, token, params=None):
        '''
        Finds a specific campaigns object
        :param token: campaigns token
        :param params: query parameters
        :return: CampaignResponseModel object
        '''
        return self.collections.find(endpoint=self._endpoint + '/{}'.format(token),
                                     query_params=params)

    def save(self, token, data):
        '''
        Updates an campaigns object
        :param token: campaigns token
        :param data: data to be updated
        :return: CampaignResponseModel object
        '''
        return self.collections.save(data, endpoint=self._endpoint + '/{}'.format(token))

    def __repr__(self):
        return '<Marqeta.resources.campaigns.CampaignsCollection>'


class CampaignsContext(CampaignsCollection):

    def __init__(self, token, client):
        super(CampaignsContext, self).__init__(client)
        self.token = token
        self.stores = self.Stores(self.token, Collection(client, StoreModel))

    class Stores(object):
        '''
        Lists the children for parent campaigns
        Returns StoreModel object
        '''
        _endpoint = 'campaigns/{}/stores'

        def __init__(self, token, collection):
            self.token = token
            self.collection = collection

        def page(self, count=5, start_index=0):
            return self.collection.page(endpoint=self._endpoint.format(self.token),
                                        count=count, start_index=start_index)

        def stream(self, params=None, limit=None):
            return self.collection.stream(endpoint=self._endpoint.format(self.token),
                                          query_params=params, limit=limit)

        def list(self, params=None, limit=None):
            return self.collection.list(endpoint=self._endpoint.format(self.token),
                                        query_params=params, limit=limit)

        def __repr__(self):
            return '<Marqeta.resources.campaigns.CampaignsContext.Stores>'
