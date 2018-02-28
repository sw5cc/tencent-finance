#!/usr/bin/env python
# -*- coding:utf-8 -*-


def to_utf8_string(unicodestr):
    utf8str = ''
    start = 0
    end = 0
    pos = unicodestr.find('\\u')
    while pos != -1:
        end = pos
        if start != end:
            utf8str += unicodestr[start:end]
        start = pos + 6
        ch = unicodestr[pos + 2:start]
        utf8str += chr(int(ch, 16))
        pos = unicodestr.find('\\u', start)
    if start != len(unicodestr):
        utf8str += unicodestr[start:]
    return utf8str
