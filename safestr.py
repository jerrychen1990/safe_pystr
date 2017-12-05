#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 11/28/17 4:41 PM
# @Author  : jerry

import platform

CODE = u'utf8'

version_str = platform.python_version()


def convert2unicode(element):
    if version_str.startswith(u'3'):
        return convert2unicode_v3(element)
    if version_str.startswith(u'2'):
        return convert2unicode_v2(element)


def convert2unicode_v3(element):
    if isinstance(element, str):
        return element
    if isinstance(element, bytes):
        return element.decode(CODE)
    return str(element)


def convert2unicode_v2(element):
    if isinstance(element, str):
        return element.decode(CODE)
    if isinstance(element, unicode):
        return element
    return unicode(element)


def is_general_str(element):
    if version_str.startswith(u"3"):
        return isinstance(element, str) or isinstance(element, bytes)
    if version_str.startswith(u"2"):
        return isinstance(element, unicode) or isinstance(element, str)
    return False


def safe_format(pattern, **kwargs):
    safe_pattern = safe_nest_unicode(pattern)
    safe_kwargs = dict([(k, safe_repr_unicode(v)) for k, v in kwargs.items()])
    return safe_pattern.format(**safe_kwargs)


def safe_repr_unicode(element):
    def surround(body, head, tail=None):
        if not tail:
            tail = head
        return head + body + tail

    __quote = u"'"
    __double_quote = u'"'

    if isinstance(element, list):
        return surround(u", ".join([safe_repr_unicode(e) for e in element]), u"[", u"]")
    if isinstance(element, tuple):
        return surround(u", ".join([safe_repr_unicode(e) for e in element]), u"(", u")")
    if isinstance(element, set):
        return surround(u", ".join(sorted([safe_repr_unicode(e) for e in element])), u"{", u"}")
    if isinstance(element, dict):
        sorted_kv = sorted([(safe_repr_unicode(k), safe_repr_unicode(v)) for k, v in element.items()])
        return surround(u", ".join([k + u": " + v for k, v in sorted_kv]), u"{", u"}")

    rs = convert2unicode(element)
    if is_general_str(element):
        if __quote in rs:
            rs = surround(rs, __double_quote)
        else:
            rs = surround(rs, __quote)
    return rs


def safe_nest_unicode(element):
    rs = safe_repr_unicode(element)
    if is_general_str(element):
        rs = rs[1:-1]
    return rs


def safe_print(element):
    if version_str.startswith(u"2"):
        print(safe_nest_unicode(element).encode(CODE))
    if version_str.startswith(u"3"):
        print(safe_nest_unicode(element))


