#!/usr/bin/env python
# -*- coding:utf-8 -*-


class Bundle(object):

    def __init__(self, sec_code, exchange):
        self.sec_code = sec_code
        self.exchange = exchange
        self.linkparam = self.exchange + self.sec_code
