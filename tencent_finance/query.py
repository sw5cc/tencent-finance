#!/usr/bin/env python
# -*- coding:utf-8 -*-


from tencent_finance import constant as cons
from tencent_finance import unicode_converter
from .connect import connect


class Item(object):
    def __init__(self, exchange, sec_code, name, pinyin, share_type):
        self.exchange = exchange
        self.sec_code = sec_code
        self.name = unicode_converter.to_utf8_string(name)
        self.pinyin = str(pinyin).upper()
        self.share_type = share_type


def query_all(keyword):
    url = cons.QUERY_URL
    payload = {'q': keyword, 't': 'all'}
    hints = connect(url, payload)[8: -1].split('^')
    result = []
    for hint in hints:
        lh = hint.split('~')
        item = Item(lh[0], lh[1], lh[2], lh[3], lh[4])
        result.append(item)
    return result


def query_exchange(sec_code):
    result = query_all(sec_code)
    if len(result) > 0:
        return result[0].exchange
