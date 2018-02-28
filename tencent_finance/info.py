#!/usr/bin/env python
# -*- coding:utf-8 -*-


class Info(dict):

    def __init__(self, **kw):
        super(Info, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            return None

    def __setattr__(self, key, value):
        self[key] = value


class InfoPack(Info):

    TYPE_SH = 0
    TYPE_SZ = 1
    TYPE_HK = 2

    def __init__(self, **kw):
        super(InfoPack, self).__init__(**kw)
        self.pack = [Info(), Info(), Info()]

    def which(self, exchange):
        if exchange == 'sh':
            return self.pack[self.TYPE_SH]
        elif exchange == 'sz':
            return self.pack[self.TYPE_SZ]
        elif exchange == 'hk':
            return self.pack[self.TYPE_HK]

    @property
    def sh(self):
        return self.pack[self.TYPE_SH]

    @property
    def sz(self):
        return self.pack[self.TYPE_SZ]

    @property
    def hk(self):
        return self.pack[self.TYPE_HK]
