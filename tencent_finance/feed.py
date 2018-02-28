#!/usr/bin/env python
# -*- coding:utf-8 -*-


from simplejson import loads


from tencent_finance import constant as cons
from .connect import connect


class DataFeed(object):
    '''

    '''
    def __init__(self, bundles):
        '''

        :param bundles: Bundle
        '''
        self.bundles = bundles

    def basic_info(self, pack):
        for item in self.bundles:
            if item.exchange == 'us':
                continue
            to_update = pack.which(item.exchange)
            url = cons.BASIC_INFO_URLS[item.exchange]
            if item.exchange == 'hk':
                payload = {'c': item.sec_code}
                json = loads(connect(url, payload))
                if json['code'] == 0:
                    to_update.update(json['data'])
            elif item.exchange == 'sz' or item.exchange == 'sh':
                payload = {'code': item.linkparam, 'type': 'gsgk_tips'}
                json = loads(connect(url, payload))
                if json['msg'] == 'OK':
                    to_update.update(json['data'])

    def extend_info(self, info):
        pass