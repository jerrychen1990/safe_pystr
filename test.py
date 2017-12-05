#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 11/28/17 4:44 PM
# @Author  : xiaowa

from safestr import CODE, safe_print, safe_repr_unicode, safe_nest_unicode, safe_format

a = u'喆'
b = a.encode(CODE)
c = u'abc'
d = c.encode(CODE)
e = 1
f = 1.1
g = 4 + 3j
h = True
i = set([f, g, h])
j = (a, b, c, d, e)
k = [a, b, c, d, e, f, g, h, i, j]
l = {a: b, c: d, e: i, f: j, h: k}
m = '"喆a'
n = "'喆a"


def test_safe_format():
    expect = u"'喆'|'喆'|['喆', '喆', 'abc', 'abc', 1, 1.1, (4+3j), True, " \
             u"{(4+3j), 1.1, True}, " \
             u"('喆', '喆', 'abc', 'abc', 1)]|('喆', '喆', 'abc', 'abc', 1)|" \
             u"{'abc': 'abc', '喆': '喆', 1: ['喆', '喆', 'abc', 'abc', 1, 1.1," \
             u" (4+3j), True, {(4+3j), 1.1, True}, ('喆', '喆', 'abc', 'abc', 1)]," \
             u" 1.1: ('喆', '喆', 'abc', 'abc', 1)}喆"

    assert expect == safe_format(u'{unicode}|{bytes}|{list}|{tuple}|{dict}喆',
                                 unicode=a, bytes=b, list=k, tuple=j,
                                 dict=l)
    assert expect == safe_format(u'{unicode}|{bytes}|{list}|{tuple}|{dict}喆'.encode(CODE),
                                 unicode=a, bytes=b, list=k, tuple=j,
                                 dict=l)


def test_safe_repr_unicode():
    assert safe_repr_unicode(a) == u"'喆'"
    assert safe_repr_unicode(b) == u"'喆'"
    assert safe_repr_unicode(c) == u"'abc'"
    assert safe_repr_unicode(d) == u"'abc'"
    assert safe_repr_unicode(e) == u"1"
    assert safe_repr_unicode(f) == u"1.1"
    assert safe_repr_unicode(g) == u"(4+3j)"
    assert safe_repr_unicode(h) == u"True"
    assert safe_repr_unicode(i) == u"{(4+3j), 1.1, True}"
    assert safe_repr_unicode(j) == u"('喆', '喆', 'abc', 'abc', 1)"
    assert safe_repr_unicode(k) == u"['喆', '喆', 'abc', 'abc', 1, 1.1, " \
                                   u"(4+3j), True, {(4+3j), 1.1, True}, ('喆', '喆', 'abc', 'abc', 1)]"
    assert safe_repr_unicode(l) == u"{'abc': 'abc', '喆': '喆', " \
                                   u"1: ['喆', '喆', 'abc', 'abc', 1, 1.1, (4+3j), True, {(4+3j), 1.1, True}, " \
                                   u"('喆', '喆', 'abc', 'abc', 1)], 1.1: ('喆', '喆', 'abc', 'abc', 1)}"
    assert safe_repr_unicode(m) == u"'\"喆a'"
    assert safe_repr_unicode(n) == u"\"'喆a\""


def test_safe_nest_unicode():
    assert safe_nest_unicode(a) == u"喆"
    assert safe_nest_unicode(b) == u"喆"
    assert safe_nest_unicode(c) == u"abc"
    assert safe_nest_unicode(d) == u"abc"
    assert safe_nest_unicode(e) == u"1"
    assert safe_nest_unicode(f) == u"1.1"
    assert safe_nest_unicode(g) == u"(4+3j)"
    assert safe_nest_unicode(h) == u"True"
    assert safe_nest_unicode(i) == u"{(4+3j), 1.1, True}"
    assert safe_nest_unicode(j) == u"('喆', '喆', 'abc', 'abc', 1)"
    assert safe_nest_unicode(k) == u"['喆', '喆', 'abc', 'abc', 1, 1.1, " \
                                   u"(4+3j), True, {(4+3j), 1.1, True}, ('喆', '喆', 'abc', 'abc', 1)]"
    assert safe_nest_unicode(l) == u"{'abc': 'abc', '喆': '喆', " \
                                   u"1: ['喆', '喆', 'abc', 'abc', 1, 1.1, (4+3j), True, {(4+3j), 1.1, True}, " \
                                   u"('喆', '喆', 'abc', 'abc', 1)], 1.1: ('喆', '喆', 'abc', 'abc', 1)}"
    assert safe_nest_unicode(m) == u'"喆a'
    assert safe_nest_unicode(n) == u"'喆a"


def test_safe_print():
    safe_print(a)
    safe_print(b)
    safe_print(c)
    safe_print(d)
    safe_print(e)
    safe_print(f)
    safe_print(g)
    safe_print(h)
    safe_print(i)
    safe_print(j)
    safe_print(k)

