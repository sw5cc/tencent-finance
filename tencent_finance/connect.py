#!/usr/bin/env python
# -*- coding:utf-8 -*-


import requests


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0"
}


def connect(url, payload):
    req = requests.get(url, params=payload, headers=headers)
    return req.text
