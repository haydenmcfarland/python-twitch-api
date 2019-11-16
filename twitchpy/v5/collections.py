from twitchpy.other.constants import *
from twitchpy.other.decorators import oauth_required
from twitchpy.other.helper import dict_gen
from twitchpy.v5.base import TwitchBase


class Collections(TwitchBase):
    def get_collection_metadata(self, collection_id):
        request = 'collections/{}'.format(collection_id)
        return self._get(request)

    def get_collection(self, collection_id, include_all_items=False):
        request = 'collections/{}/items'.format(collection_id)
        params = dict_gen(include_all_items=include_all_items)
        return self._get(request, params=params)

    def get_collection_by_channel(
            self,
            channel_id,
            limit=10,
            cursor=None,
            containing_item=None):
        request = 'channels/{}/collections'.format(channel_id)
        params = dict_gen(
            limit=limit,
            cursor=cursor,
            containing_item=containing_item)
        return self._get(request, params=params)

    @oauth_required
    def create_collection(self, channel_id, title):
        request = 'channels/{}/collections'.format(channel_id)
        json = dict_gen(title=title)
        return self._post(request, json=json)

    @oauth_required
    def create_collection(self, collections_id, title):
        request = 'collections/{}'.format(collections_id)
        json = dict_gen(title=title)
        return self._put(request, json=json)

    @oauth_required
    def create_collection_thumbnail(self, collection_id, item_id):
        request = 'collections/{}/thumbnail'.format(collection_id)
        json = dict_gen(item_id=item_id)
        return self._put(request, json=json)

    @oauth_required
    def delete_collection(self, collection_id):
        request = 'collections/{}'.format(collection_id)
        return self._delete(request)

    @oauth_required
    def add_item_to_collection(
            self,
            collection_id,
            item_id,
            item_type='video'):
        request = 'collections/{}/items'.format(collection_id)
        json = dict_gen(id=item_id, type=item_type)
        return self._post(request, json=json)

    @oauth_required
    def delete_item_from_collection(self, collection_id, item_id):
        request = 'collections/{}/items/{}'.format(collection_id, item_id)
        return self._delete(request)

    @oauth_required
    def move_collection_item(self, collection_id, item_id, position):
        request = 'collections/{}/items/{}'.format(collection_id, item_id)
        json = dict_gen(position=position)
        return self._put(request, json=json)
