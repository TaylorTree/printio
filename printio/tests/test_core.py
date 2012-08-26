#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2012, Mike Taylor
#
# This file is part of printio released under MIT license.
# See the LICENSE for more information.
"""

Test the core module.

"""

import os
import sys
import unittest
import datetime

libpath = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if not libpath in sys.path:
    sys.path.insert(1, libpath)
del libpath

from core import PrettyValue
from core import PrettyValues


class PrettyValue_ParseTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_test_strings(self):
        pv = PrettyValue('s')
        self.assertEquals(pv.atype, 's')
        self.assertEquals(pv.align, '<')
        self.assertEquals(pv.width, '')
        self.assertEquals(pv.sign, '')
        self.assertEquals(pv.precision, '')

    def test_parse_rawtype_default(self):
        pv = PrettyValue()

        results = pv.parse_rawtype()
        self.assertEquals(results['atype'], None)
        self.assertEquals(results['align'], None)
        self.assertEquals(results['width'], None)
        self.assertEquals(results['sign'], None)
        self.assertEquals(results['precision'], None)

    def test_parse_rawtype_str(self):
        pv = PrettyValue()

        results = pv.parse_rawtype('s')
        self.assertEquals(results['atype'], 's')
        self.assertEquals(results['align'], None)
        self.assertEquals(results['width'], None)
        self.assertEquals(results['sign'], None)
        self.assertEquals(results['precision'], None)

    def test_parse_rawtype_int(self):
        pv = PrettyValue()

        results = pv.parse_rawtype('i')
        self.assertEquals(results['atype'], 'i')
        self.assertEquals(results['align'], None)
        self.assertEquals(results['width'], None)
        self.assertEquals(results['sign'], None)
        self.assertEquals(results['precision'], None)

    def test_parse_rawtype_float(self):
        pv = PrettyValue()

        results = pv.parse_rawtype('f')
        self.assertEquals(results['atype'], 'f')
        self.assertEquals(results['align'], None)
        self.assertEquals(results['width'], None)
        self.assertEquals(results['sign'], None)
        self.assertEquals(results['precision'], None)

    def test_parse_rawtype_date(self):
        pv = PrettyValue()

        results = pv.parse_rawtype('%Y-%m-%d')
        self.assertEquals(results['atype'], '%Y-%m-%d')
        self.assertEquals(results['align'], None)
        self.assertEquals(results['width'], None)
        self.assertEquals(results['sign'], None)
        self.assertEquals(results['precision'], None)

    def test_parse_rawtype_width(self):
        pv = PrettyValue()

        results = pv.parse_rawtype('5')
        self.assertEquals(results['atype'], None)
        self.assertEquals(results['align'], None)
        self.assertEquals(results['width'], 5)
        self.assertEquals(results['sign'], None)
        self.assertEquals(results['precision'], None)

        results = pv.parse_rawtype('5s')
        self.assertEquals(results['atype'], 's')
        self.assertEquals(results['align'], None)
        self.assertEquals(results['width'], 5)
        self.assertEquals(results['sign'], None)
        self.assertEquals(results['precision'], None)

        results = pv.parse_rawtype('5i')
        self.assertEquals(results['atype'], 'i')
        self.assertEquals(results['align'], None)
        self.assertEquals(results['width'], 5)
        self.assertEquals(results['sign'], None)
        self.assertEquals(results['precision'], None)

        results = pv.parse_rawtype('5f')
        self.assertEquals(results['atype'], 'f')
        self.assertEquals(results['align'], None)
        self.assertEquals(results['width'], 5)
        self.assertEquals(results['sign'], None)
        self.assertEquals(results['precision'], None)

        results = pv.parse_rawtype('5%Y-%m-%d')
        self.assertEquals(results['atype'], '%Y-%m-%d')
        self.assertEquals(results['align'], None)
        self.assertEquals(results['width'], 5)
        self.assertEquals(results['sign'], None)
        self.assertEquals(results['precision'], None)

    def test_parse_rawtype_sign(self):
        pv = PrettyValue()

        results = pv.parse_rawtype('-')
        self.assertEquals(results['atype'], None)
        self.assertEquals(results['align'], None)
        self.assertEquals(results['width'], None)
        self.assertEquals(results['sign'], '-')
        self.assertEquals(results['precision'], None)

        results = pv.parse_rawtype('+')
        self.assertEquals(results['atype'], None)
        self.assertEquals(results['align'], None)
        self.assertEquals(results['width'], None)
        self.assertEquals(results['sign'], '+')
        self.assertEquals(results['precision'], None)

        results = pv.parse_rawtype('-5')
        self.assertEquals(results['atype'], None)
        self.assertEquals(results['align'], None)
        self.assertEquals(results['width'], 5)
        self.assertEquals(results['sign'], '-')
        self.assertEquals(results['precision'], None)

        results = pv.parse_rawtype('+5')
        self.assertEquals(results['atype'], None)
        self.assertEquals(results['align'], None)
        self.assertEquals(results['width'], 5)
        self.assertEquals(results['sign'], '+')
        self.assertEquals(results['precision'], None)

        results = pv.parse_rawtype('-s')
        self.assertEquals(results['atype'], 's')
        self.assertEquals(results['align'], None)
        self.assertEquals(results['width'], None)
        self.assertEquals(results['sign'], '-')
        self.assertEquals(results['precision'], None)

        results = pv.parse_rawtype('+s')
        self.assertEquals(results['atype'], 's')
        self.assertEquals(results['align'], None)
        self.assertEquals(results['width'], None)
        self.assertEquals(results['sign'], '+')
        self.assertEquals(results['precision'], None)

        results = pv.parse_rawtype(' -i')
        self.assertEquals(results['atype'], '-i')
        self.assertEquals(results['align'], None)
        self.assertEquals(results['width'], None)
        self.assertEquals(results['sign'], ' ')
        self.assertEquals(results['precision'], None)

        results = pv.parse_rawtype('-i')
        self.assertEquals(results['atype'], 'i')
        self.assertEquals(results['align'], None)
        self.assertEquals(results['width'], None)
        self.assertEquals(results['sign'], '-')
        self.assertEquals(results['precision'], None)

        results = pv.parse_rawtype('- i')
        self.assertEquals(results['atype'], 'i')
        self.assertEquals(results['align'], None)
        self.assertEquals(results['width'], None)
        self.assertEquals(results['sign'], '-')
        self.assertEquals(results['precision'], None)

        results = pv.parse_rawtype('+i')
        self.assertEquals(results['atype'], 'i')
        self.assertEquals(results['align'], None)
        self.assertEquals(results['width'], None)
        self.assertEquals(results['sign'], '+')
        self.assertEquals(results['precision'], None)

        results = pv.parse_rawtype('+ i')
        self.assertEquals(results['atype'], 'i')
        self.assertEquals(results['align'], None)
        self.assertEquals(results['width'], None)
        self.assertEquals(results['sign'], '+')
        self.assertEquals(results['precision'], None)

        results = pv.parse_rawtype('-f')
        self.assertEquals(results['atype'], 'f')
        self.assertEquals(results['align'], None)
        self.assertEquals(results['width'], None)
        self.assertEquals(results['sign'], '-')
        self.assertEquals(results['precision'], None)

        results = pv.parse_rawtype('- f')
        self.assertEquals(results['atype'], 'f')
        self.assertEquals(results['align'], None)
        self.assertEquals(results['width'], None)
        self.assertEquals(results['sign'], '-')
        self.assertEquals(results['precision'], None)

        results = pv.parse_rawtype('+f')
        self.assertEquals(results['atype'], 'f')
        self.assertEquals(results['align'], None)
        self.assertEquals(results['width'], None)
        self.assertEquals(results['sign'], '+')
        self.assertEquals(results['precision'], None)

        results = pv.parse_rawtype('+ f')
        self.assertEquals(results['atype'], 'f')
        self.assertEquals(results['align'], None)
        self.assertEquals(results['width'], None)
        self.assertEquals(results['sign'], '+')
        self.assertEquals(results['precision'], None)

        results = pv.parse_rawtype(' %Y-%m-%d')
        self.assertEquals(results['atype'], '%Y-%m-%d')
        self.assertEquals(results['align'], None)
        self.assertEquals(results['width'], None)
        self.assertEquals(results['sign'], ' ')
        self.assertEquals(results['precision'], None)

        results = pv.parse_rawtype('-%Y-%m-%d')
        self.assertEquals(results['atype'], '%Y-%m-%d')
        self.assertEquals(results['align'], None)
        self.assertEquals(results['width'], None)
        self.assertEquals(results['sign'], '-')
        self.assertEquals(results['precision'], None)

        results = pv.parse_rawtype('- %Y-%m-%d')
        self.assertEquals(results['atype'], '%Y-%m-%d')
        self.assertEquals(results['align'], None)
        self.assertEquals(results['width'], None)
        self.assertEquals(results['sign'], '-')
        self.assertEquals(results['precision'], None)

        results = pv.parse_rawtype('+%Y-%m-%d')
        self.assertEquals(results['atype'], '%Y-%m-%d')
        self.assertEquals(results['align'], None)
        self.assertEquals(results['width'], None)
        self.assertEquals(results['sign'], '+')
        self.assertEquals(results['precision'], None)

        results = pv.parse_rawtype('+ %Y-%m-%d')
        self.assertEquals(results['atype'], '%Y-%m-%d')
        self.assertEquals(results['align'], None)
        self.assertEquals(results['width'], None)
        self.assertEquals(results['sign'], '+')
        self.assertEquals(results['precision'], None)

    def test_parse_rawtype_align(self):
        pv = PrettyValue()

        results = pv.parse_rawtype('>')
        self.assertEquals(results['atype'], None)
        self.assertEquals(results['align'], '>')
        self.assertEquals(results['width'], None)
        self.assertEquals(results['sign'], None)
        self.assertEquals(results['precision'], None)

        results = pv.parse_rawtype('<')
        self.assertEquals(results['atype'], None)
        self.assertEquals(results['align'], '<')
        self.assertEquals(results['width'], None)
        self.assertEquals(results['sign'], None)
        self.assertEquals(results['precision'], None)

        results = pv.parse_rawtype('^')
        self.assertEquals(results['atype'], None)
        self.assertEquals(results['align'], '^')
        self.assertEquals(results['width'], None)
        self.assertEquals(results['sign'], None)
        self.assertEquals(results['precision'], None)

        results = pv.parse_rawtype('>i')
        self.assertEquals(results['atype'], 'i')
        self.assertEquals(results['align'], '>')
        self.assertEquals(results['width'], None)
        self.assertEquals(results['sign'], None)
        self.assertEquals(results['precision'], None)

        results = pv.parse_rawtype('^.2f')
        self.assertEquals(results['atype'], 'f')
        self.assertEquals(results['align'], '^')
        self.assertEquals(results['width'], None)
        self.assertEquals(results['sign'], None)
        self.assertEquals(results['precision'], 2)

        results = pv.parse_rawtype('^-.2f')
        self.assertEquals(results['atype'], 'f')
        self.assertEquals(results['align'], '^')
        self.assertEquals(results['width'], None)
        self.assertEquals(results['sign'], '-')
        self.assertEquals(results['precision'], 2)

        results = pv.parse_rawtype('=+5.2f')
        self.assertEquals(results['atype'], 'f')
        self.assertEquals(results['align'], '=')
        self.assertEquals(results['width'], 5)
        self.assertEquals(results['sign'], '+')
        self.assertEquals(results['precision'], 2)

        results = pv.parse_rawtype('> %Y-%m-%d')
        self.assertEquals(results['atype'], '%Y-%m-%d')
        self.assertEquals(results['align'], '>')
        self.assertEquals(results['width'], None)
        self.assertEquals(results['sign'], ' ')
        self.assertEquals(results['precision'], None)

    def test_parse_rawtype_precision(self):
        pv = PrettyValue()

        results = pv.parse_rawtype('.')
        self.assertEquals(results['atype'], '.')
        self.assertEquals(results['align'], None)
        self.assertEquals(results['width'], None)
        self.assertEquals(results['sign'], None)
        self.assertEquals(results['precision'], None)

        results = pv.parse_rawtype('.f')
        self.assertEquals(results['atype'], '.f')
        self.assertEquals(results['align'], None)
        self.assertEquals(results['width'], None)
        self.assertEquals(results['sign'], None)
        self.assertEquals(results['precision'], None)

        results = pv.parse_rawtype('.2s')
        self.assertEquals(results['atype'], 's')
        self.assertEquals(results['align'], None)
        self.assertEquals(results['width'], None)
        self.assertEquals(results['sign'], None)
        self.assertEquals(results['precision'], 2)

        results = pv.parse_rawtype('.2i')
        self.assertEquals(results['atype'], 'i')
        self.assertEquals(results['align'], None)
        self.assertEquals(results['width'], None)
        self.assertEquals(results['sign'], None)
        self.assertEquals(results['precision'], 2)

        results = pv.parse_rawtype('5.2f')
        self.assertEquals(results['atype'], 'f')
        self.assertEquals(results['align'], None)
        self.assertEquals(results['width'], 5)
        self.assertEquals(results['sign'], None)
        self.assertEquals(results['precision'], 2)

        results = pv.parse_rawtype('.2f')
        self.assertEquals(results['atype'], 'f')
        self.assertEquals(results['align'], None)
        self.assertEquals(results['width'], None)
        self.assertEquals(results['sign'], None)
        self.assertEquals(results['precision'], 2)

        results = pv.parse_rawtype('.2 f')
        self.assertEquals(results['atype'], 'f')
        self.assertEquals(results['align'], None)
        self.assertEquals(results['width'], None)
        self.assertEquals(results['sign'], None)
        self.assertEquals(results['precision'], 2)

        results = pv.parse_rawtype('-.2f')
        self.assertEquals(results['atype'], 'f')
        self.assertEquals(results['align'], None)
        self.assertEquals(results['width'], None)
        self.assertEquals(results['sign'], '-')
        self.assertEquals(results['precision'], 2)

        results = pv.parse_rawtype('- .2f')
        self.assertEquals(results['atype'], 'f')
        self.assertEquals(results['align'], None)
        self.assertEquals(results['width'], None)
        self.assertEquals(results['sign'], '-')
        self.assertEquals(results['precision'], 2)

        results = pv.parse_rawtype('5.2f')
        self.assertEquals(results['atype'], 'f')
        self.assertEquals(results['align'], None)
        self.assertEquals(results['width'], 5)
        self.assertEquals(results['sign'], None)
        self.assertEquals(results['precision'], 2)

        results = pv.parse_rawtype('+5.2f')
        self.assertEquals(results['atype'], 'f')
        self.assertEquals(results['align'], None)
        self.assertEquals(results['width'], 5)
        self.assertEquals(results['sign'], '+')
        self.assertEquals(results['precision'], 2)

        results = pv.parse_rawtype('%H:%M.%S')
        self.assertEquals(results['atype'], '%H:%M.%S')
        self.assertEquals(results['align'], None)
        self.assertEquals(results['width'], None)
        self.assertEquals(results['sign'], None)
        self.assertEquals(results['precision'], None)


class PrettyValue_FormatTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_format_default(self):
        pv = PrettyValue()
        results = pv.format('test')
        self.assertEquals(results, 'test')

        pv = PrettyValue('10')
        results = pv.format('test')
        self.assertEquals(results, 'test      ')

        pv = PrettyValue('>10')
        results = pv.format('test')
        self.assertEquals(results, '      test')

        pv = PrettyValue('^10')
        results = pv.format('test')
        self.assertEquals(results, '   test   ')

        pv = PrettyValue('10')
        results = pv.format(5.25)
        self.assertEquals(results, '5.25      ')

        self.assertRaises(ValueError, PrettyValue, '=10')

        self.assertRaises(ValueError, PrettyValue, '-10')

        self.assertRaises(ValueError, PrettyValue, '10.2')

    def test_format_strings(self):
        pv = PrettyValue('s')
        results = pv.format('test')
        self.assertEquals(results, 'test')

        pv = PrettyValue('10s')
        results = pv.format('test')
        self.assertEquals(results, 'test      ')

        pv = PrettyValue('>10s')
        results = pv.format('test')
        self.assertEquals(results, '      test')

        pv = PrettyValue('^10s')
        results = pv.format('test')
        self.assertEquals(results, '   test   ')

        pv = PrettyValue('10s')
        results = pv.format(5.25)
        self.assertEquals(results, '5.25      ')

        self.assertRaises(ValueError, PrettyValue, '=10s')

        self.assertRaises(ValueError, PrettyValue, '=10s')

        self.assertRaises(ValueError, PrettyValue, '-10s')

        self.assertRaises(ValueError, PrettyValue, '10.2s')

    def test_format_ints(self):
        pv = PrettyValue('i')
        results = pv.format('5')
        self.assertEquals(results, '5')

        #no sign just size
        pv = PrettyValue('10i')
        results = pv.format('5')
        self.assertEquals(results, '         5')

        pv = PrettyValue('<10i')
        results = pv.format('5')
        self.assertEquals(results, '5         ')

        pv = PrettyValue('^10i')
        results = pv.format('5')
        self.assertEquals(results, '    5     ')

        pv = PrettyValue('< 10i')
        results = pv.format('5')
        self.assertEquals(results, ' 5        ')

        #positive sign and size
        pv = PrettyValue('+10i')
        results = pv.format('5')
        self.assertEquals(results, '+        5')

        pv = PrettyValue('>+10i')
        results = pv.format('5')
        self.assertEquals(results, '        +5')

        pv = PrettyValue('<+10i')
        results = pv.format('5')
        self.assertEquals(results, '+5        ')

        pv = PrettyValue('^+10i')
        results = pv.format('5')
        self.assertEquals(results, '    +5    ')

        #negative number and size
        pv = PrettyValue('10i')
        results = pv.format('-5')
        self.assertEquals(results, '-        5')

        pv = PrettyValue('>10i')
        results = pv.format('-5')
        self.assertEquals(results, '        -5')

        pv = PrettyValue('< 10i')
        results = pv.format('-5')
        self.assertEquals(results, '-5        ')

        pv = PrettyValue('<10i')
        results = pv.format('-5')
        self.assertEquals(results, '-5        ')

        pv = PrettyValue('^10i')
        results = pv.format('-5')
        self.assertEquals(results, '    -5    ')

        #test float conversion to int formatting
        pv = PrettyValue('i')
        results = pv.format(5.25)
        self.assertEquals(results, '5')

        pv = PrettyValue(' i')
        results = pv.format(5)
        self.assertEquals(results, ' 5')

        pv = PrettyValue(' i')
        results = pv.format(-5)
        self.assertEquals(results, '-5')

        pv = PrettyValue('+10i')
        results = pv.format(5)
        self.assertEquals(results, '+        5')

        self.assertRaises(ValueError, PrettyValue, '10.2i')

        pv = PrettyValue('i')
        self.assertRaises(ValueError, pv.format, 'test')

    def test_format_floats(self):
        #default precision is used of 4 and it does round up.
        pv = PrettyValue('f')
        results = pv.format('5.256678')
        self.assertEquals(results, '5.2567')

        #no sign just size
        pv = PrettyValue('10f')
        results = pv.format('5.256678')
        self.assertEquals(results, '    5.2567')

        #same size but small precision
        pv = PrettyValue('10.2f')
        results = pv.format('5.256678')
        self.assertEquals(results, '      5.26')

        #same size but bigger precision
        pv = PrettyValue('10.8f')
        results = pv.format(5.256678)
        self.assertEquals(results, '5.25667800')

        pv = PrettyValue('<10.2f')
        results = pv.format(5.256678)
        self.assertEquals(results, '5.26      ')

        pv = PrettyValue('^10.1f')
        results = pv.format(5)
        self.assertEquals(results, '   5.0    ')

        pv = PrettyValue('< 10f')
        results = pv.format(5)
        self.assertEquals(results, ' 5.0000   ')

        #positive sign and size
        pv = PrettyValue('+10f')
        results = pv.format(5)
        self.assertEquals(results, '+   5.0000')

        pv = PrettyValue('>+10.1f')
        results = pv.format(5)
        self.assertEquals(results, '      +5.0')

        pv = PrettyValue('<+10.1f')
        results = pv.format(5.256)
        self.assertEquals(results, '+5.3      ')

        pv = PrettyValue('^+10.1f')
        results = pv.format(5.233)
        self.assertEquals(results, '   +5.2   ')

        #negative number and size
        pv = PrettyValue('10f')
        results = pv.format('-5.25634')
        self.assertEquals(results, '-   5.2563')

        pv = PrettyValue('>10.2f')
        results = pv.format('-5.33333')
        self.assertEquals(results, '     -5.33')

        pv = PrettyValue('< 10f')
        results = pv.format('-5.3333')
        self.assertEquals(results, '-5.3333   ')

        pv = PrettyValue('<10.2f')
        results = pv.format(-5.256)
        self.assertEquals(results, '-5.26     ')

        pv = PrettyValue('^10.2f')
        results = pv.format('-5')
        self.assertEquals(results, '  -5.00   ')

        pv = PrettyValue(' f')
        results = pv.format(5)
        self.assertEquals(results, ' 5.0000')

        pv = PrettyValue(' f')
        results = pv.format(-5)
        self.assertEquals(results, '-5.0000')

        pv = PrettyValue('f')
        self.assertRaises(ValueError, pv.format, 'test')

    def test_format_percents(self):
        pv = PrettyValue('.2%')
        results = pv.format('.0525')
        self.assertEquals(results, '5.25%')

        pv = PrettyValue('%')
        results = pv.format('1')
        self.assertEquals(results, '100.0000%')

    def test_format_unknowns(self):
        d = datetime.datetime(2010, 7, 4, 12, 15, 58)

        pv = PrettyValue('%Y-%m-%d')
        results = pv.format(d)
        self.assertEquals(results, '2010-07-04')

        self.assertRaises(ValueError, PrettyValue, ' %Y-%m-%d')

        pv = PrettyValue('>10%Y')
        results = pv.format(d)
        self.assertEquals(results, '      2010')

    def test_format_fill(self):
        pv = PrettyValue('10s', fill='*')
        results = pv.format('test')
        self.assertEquals(results, 'test******')

        pv = PrettyValue('^10s', fill='-')
        results = pv.format('test')
        self.assertEquals(results, '---test---')

        pv = PrettyValue('^10i', fill='-')
        results = pv.format('5')
        self.assertEquals(results, '----5-----')

        pv = PrettyValue('^+10.2f', fill='-')
        results = pv.format(5.23456)
        self.assertEquals(results, '--+5.23---')

        pv = PrettyValue('10i', fill=0)
        results = pv.format(5)
        self.assertEquals(results, '0000000005')

        pv = PrettyValue('-10i', fill=0)
        results = pv.format(-5)
        self.assertEquals(results, '-000000005')

        pv = PrettyValue('>10i', fill=0)
        results = pv.format(-5)
        self.assertEquals(results, '00000000-5')

        pv = PrettyValue('=10i', fill=0)
        results = pv.format(-5)
        self.assertEquals(results, '-000000005')

        pv = PrettyValue(' 10i', fill=0)
        results = pv.format(5)
        self.assertEquals(results, ' 000000005')

    def test_maxwidth(self):
        pv = PrettyValue('10s')
        results = pv.format('test')
        self.assertEquals(pv.maxwidth, 10)

        pv = PrettyValue('10s')
        results = pv.format('testing is lots of fun')
        self.assertEquals(pv.maxwidth, 22)

        pv = PrettyValue('i')
        results = pv.format(5123)
        self.assertEquals(pv.maxwidth, 4)

        pv = PrettyValue('5.1f')
        results = pv.format(5123.23456)
        self.assertEquals(pv.maxwidth, 6)


class PrettyValues_TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_format_list(self):
        pv = PrettyValues()

        pv.newcol(0, 'i')
        pv.newcol(1, cname='Column2')
        pv.newcol(2, '+5.2f')

        values = [0, 'yhoo', 23.45]

        results = pv.format([values])

        self.assertEquals(results[0], ['0', 'Column2', '2     '])
        self.assertEquals(results[1], ['0', 'yhoo   ', '+23.45'])
        self.assertEquals(len(results), 2)

    def test_format_dict(self):
        pv = PrettyValues()

        pv.newcol('bar', 'i')
        pv.newcol('sym', cname='Column2')
        pv.newcol('close', '+5.2f')

        values = {'bar': 0, 'sym': 'yhoo', 'close': 23.45}

        results = pv.format([values])

        self.assertEquals(results[0], ['bar', 'Column2', 'close '])
        self.assertEquals(results[1], ['  0', 'yhoo   ', '+23.45'])
        self.assertEquals(len(results), 2)

    def test_nokey_dict(self):
        pv = PrettyValues()

        pv.newcol(vformat='i')
        pv.newcol(cname='Column2')
        pv.newcol(vformat='+5.2f')

        values = {'bar': 0, 'sym': 'yhoo', 'close': 23.45}

        self.assertRaises(KeyError, pv.format, [values])

    def test_format_lol(self):
        pv = PrettyValues()

        pv.newcol(0, 'i')
        pv.newcol(1, cname='Column2')
        pv.newcol(2, '+5.2f')

        values = []
        values.append([0, 'yhoo', 23.45])
        values.append([1, 'goog', 200.4565])
        values.append([2, 'newp', 1.00])

        results = pv.format(values)

        self.assertEquals(results[0], ['0', 'Column2', '2      '])
        self.assertEquals(results[1], ['0', 'yhoo   ', '+ 23.45'])
        self.assertEquals(results[2], ['1', 'goog   ', '+200.46'])
        self.assertEquals(results[3], ['2', 'newp   ', '+  1.00'])
        self.assertEquals(len(results), 4)

    def test_nokey_lol(self):
        pv = PrettyValues()

        pv.newcol(vformat='i')
        pv.newcol(cname='Column2')
        pv.newcol(vformat='+5.2f')

        values = []
        values.append([0, 'yhoo', 23.45])
        values.append([1, 'goog', 200.4565])
        values.append([2, 'newp', 1.00])

        results = pv.format(values)

        self.assertEquals(results[0], ['0', 'Column2', '2      '])
        self.assertEquals(results[1], ['0', 'yhoo   ', '+ 23.45'])
        self.assertEquals(results[2], ['1', 'goog   ', '+200.46'])
        self.assertEquals(results[3], ['2', 'newp   ', '+  1.00'])
        self.assertEquals(len(results), 4)

    def test_dupcol_lol(self):
        pv = PrettyValues()

        pv.newcol(vformat='i')
        pv.newcol(cname='Column2')
        pv.newcol(1)

        values = []
        values.append([0, 'yhoo', 23.45])
        values.append([1, 'goog', 200.4565])
        values.append([2, 'newp', 1.00])

        results = pv.format(values)

        self.assertEquals(results[0], ['0', 'Column2', '1   '])
        self.assertEquals(results[1], ['0', 'yhoo   ', 'yhoo'])
        self.assertEquals(results[2], ['1', 'goog   ', 'goog'])
        self.assertEquals(results[3], ['2', 'newp   ', 'newp'])
        self.assertEquals(len(results), 4)

    def test_format_lol_noheader(self):
        pv = PrettyValues()

        pv.newcol(0, 'i')
        pv.newcol(1, cname='Column2')
        pv.newcol(2, '+5.2f')

        values = []
        values.append([0, 'yhoo', 23.45])
        values.append([1, 'goog', 200.4565])
        values.append([2, 'newp', 1.00])
        values.append([3, 'nan', 'nan'])
        values.append([4, 'newp', 'inf'])
        values.append([5, 'newp', '-inf'])

        results = pv.format(values, useheader=False)

        self.assertEquals(results[0], ['0', 'yhoo', '+ 23.45'])
        self.assertEquals(results[1], ['1', 'goog', '+200.46'])
        self.assertEquals(results[2], ['2', 'newp', '+  1.00'])
        self.assertEquals(results[3], ['3', 'nan ', '    nan'])
        self.assertEquals(results[4], ['4', 'newp', '+   inf'])
        self.assertEquals(results[5], ['5', 'newp', '-   inf'])
        self.assertEquals(len(results), 6)

    def test_format_lol_inf_1(self):
        pv = PrettyValues()

        pv.newcol(0, 'i')
        pv.newcol(1, cname='Column2')
        pv.newcol(2, '+1.1f')

        values = []
        values.append([0, 'yhoo', 2])
        values.append([1, 'goog', 5])
        values.append([2, 'newp', 1])
        values.append([3, 'nan', 'nan'])
        values.append([4, 'newp', 'inf'])
        values.append([5, 'newp', '-inf'])

        results = pv.format(values, useheader=False)

        self.assertEquals(results[0], ['0', 'yhoo', '+2.0'])
        self.assertEquals(results[1], ['1', 'goog', '+5.0'])
        self.assertEquals(results[2], ['2', 'newp', '+1.0'])
        self.assertEquals(results[3], ['3', 'nan ', ' nan'])
        self.assertEquals(results[4], ['4', 'newp', '+inf'])
        self.assertEquals(results[5], ['5', 'newp', '-inf'])
        self.assertEquals(len(results), 6)

    def test_format_lol_inf_2(self):
        pv = PrettyValues()

        pv.newcol(0, 'i')
        pv.newcol(1, cname='Column2')
        pv.newcol(2, '=1.1f')

        values = []
        values.append([0, 'yhoo', 2])
        values.append([1, 'goog', 5])
        values.append([2, 'newp', 1])
        values.append([3, 'nan', 'nan'])
        values.append([4, 'newp', 'inf'])
        values.append([5, 'newp', '-inf'])

        results = pv.format(values, useheader=False)

        self.assertEquals(results[0], ['0', 'yhoo', ' 2.0'])
        self.assertEquals(results[1], ['1', 'goog', ' 5.0'])
        self.assertEquals(results[2], ['2', 'newp', ' 1.0'])
        self.assertEquals(results[3], ['3', 'nan ', ' nan'])
        self.assertEquals(results[4], ['4', 'newp', ' inf'])
        self.assertEquals(results[5], ['5', 'newp', '-inf'])
        self.assertEquals(len(results), 6)

    def test_format_lol_inf_3(self):
        pv = PrettyValues()

        pv.newcol(0, 'i')
        pv.newcol(1, cname='Column2')
        pv.newcol(2, '=5.1f')

        values = []
        values.append([0, 'yhoo', 2])
        values.append([1, 'goog', 5])
        values.append([2, 'newp', 1])
        values.append([3, 'nan', 'nan'])
        values.append([4, 'newp', 'inf'])
        values.append([5, 'newp', '+inf'])
        values.append([6, 'newp', '-inf'])

        results = pv.format(values, useheader=False)

        self.assertEquals(results[0], ['0', 'yhoo', '  2.0'])
        self.assertEquals(results[1], ['1', 'goog', '  5.0'])
        self.assertEquals(results[2], ['2', 'newp', '  1.0'])
        self.assertEquals(results[3], ['3', 'nan ', '  nan'])
        self.assertEquals(results[4], ['4', 'newp', '  inf'])
        self.assertEquals(results[5], ['5', 'newp', '  inf'])
        self.assertEquals(results[6], ['6', 'newp', '- inf'])
        self.assertEquals(len(results), 7)

    def test_format_lol_inf_4(self):
        pv = PrettyValues()

        pv.newcol(0, 'i')
        pv.newcol(1, cname='Column2')
        pv.newcol(2, '=+5.1f')

        values = []
        values.append([0, 'yhoo', 2])
        values.append([1, 'goog', 5])
        values.append([2, 'newp', 1])
        values.append([3, 'nan', 'nan'])
        values.append([4, 'newp', 'inf'])
        values.append([5, 'newp', '+inf'])
        values.append([6, 'newp', '-inf'])

        results = pv.format(values, useheader=False)

        self.assertEquals(results[0], ['0', 'yhoo', '+ 2.0'])
        self.assertEquals(results[1], ['1', 'goog', '+ 5.0'])
        self.assertEquals(results[2], ['2', 'newp', '+ 1.0'])
        self.assertEquals(results[3], ['3', 'nan ', '  nan'])
        self.assertEquals(results[4], ['4', 'newp', '+ inf'])
        self.assertEquals(results[5], ['5', 'newp', '+ inf'])
        self.assertEquals(results[6], ['6', 'newp', '- inf'])
        self.assertEquals(len(results), 7)

    def test_format_lol_nocolumns(self):
        pv = PrettyValues()

        values = []
        values.append([0, 'yhoo', 23.45])
        values.append([1, 'goog', 200.4565])
        values.append([2, 'newp', 1.00])

        results = pv.format(values)

        self.assertEquals(results[0], ['0', '1   ', '2       '])
        self.assertEquals(results[1], ['0', 'yhoo', '23.45   '])
        self.assertEquals(results[2], ['1', 'goog', '200.4565'])
        self.assertEquals(results[3], ['2', 'newp', '1.0     '])
        self.assertEquals(len(results), 4)

    def test_text_lol(self):
        pv = PrettyValues()

        pv.newcol(0, 'i')
        pv.newcol(1, cname='Column2')
        pv.newcol(2, '+5.2f')

        values = []
        values.append([0, 'yhoo', 23.45])
        values.append([1, 'goog', 200.4565])
        values.append([2, 'newp', 1.00])

        results = pv.text(values).split('\n')

        self.assertEquals(results[0], '+---+---------+---------+')
        self.assertEquals(results[1], '| 0 | Column2 | 2       |')
        self.assertEquals(results[2], '+---+---------+---------+')
        self.assertEquals(results[3], '| 0 | yhoo    | + 23.45 |')
        self.assertEquals(results[4], '| 1 | goog    | +200.46 |')
        self.assertEquals(results[5], '| 2 | newp    | +  1.00 |')
        self.assertEquals(results[6], '+---+---------+---------+')
        self.assertEquals(len(results), 7)

    def test_text_title1(self):
        pv = PrettyValues()

        pv.newcol(0, 'i')
        pv.newcol(1, cname='Column2')
        pv.newcol(2, '+5.2f')

        values = []
        values.append([0, 'yhoo', 23.45])
        values.append([1, 'goog', 200.4565])
        values.append([2, 'newp', 1.00])

        results = pv.text(values, title="Test Title 1").split('\n')

        self.assertEquals(results[0], '+-----------------------+')
        self.assertEquals(results[1], '|     Test Title 1      |')
        self.assertEquals(results[2], '+---+---------+---------+')
        self.assertEquals(results[3], '| 0 | Column2 | 2       |')
        self.assertEquals(results[4], '+---+---------+---------+')
        self.assertEquals(results[5], '| 0 | yhoo    | + 23.45 |')
        self.assertEquals(results[6], '| 1 | goog    | +200.46 |')
        self.assertEquals(results[7], '| 2 | newp    | +  1.00 |')
        self.assertEquals(results[8], '+---+---------+---------+')
        self.assertEquals(len(results), 9)

    def test_text_title_trunc(self):
        pv = PrettyValues()

        pv.newcol(0, 'i')
        pv.newcol(1, '+5.2f')

        values = []
        values.append([0, 23.45])
        values.append([1, 200.4565])
        values.append([2, 1.00])

        results = pv.text(values, title="Test Title 2").split('\n')

        self.assertEquals(results[0], '+-------------+')
        self.assertEquals(results[1], '| Test Title  |')
        self.assertEquals(results[2], '+---+---------+')
        self.assertEquals(results[3], '| 0 | 1       |')
        self.assertEquals(results[4], '+---+---------+')
        self.assertEquals(results[5], '| 0 | + 23.45 |')
        self.assertEquals(results[6], '| 1 | +200.46 |')
        self.assertEquals(results[7], '| 2 | +  1.00 |')
        self.assertEquals(results[8], '+---+---------+')
        self.assertEquals(len(results), 9)

    def test_text_title_small(self):
        pv = PrettyValues()

        pv.newcol(0, 'i')
        pv.newcol(1, '+5.2f')

        values = []
        values.append([0, 23.45])
        values.append([1, 200.4565])
        values.append([2, 1.00])

        results = pv.text(values, title="Title").split('\n')

        self.assertEquals(results[0], '+-------------+')
        self.assertEquals(results[1], '|    Title    |')
        self.assertEquals(results[2], '+---+---------+')
        self.assertEquals(results[3], '| 0 | 1       |')
        self.assertEquals(results[4], '+---+---------+')
        self.assertEquals(results[5], '| 0 | + 23.45 |')
        self.assertEquals(results[6], '| 1 | +200.46 |')
        self.assertEquals(results[7], '| 2 | +  1.00 |')
        self.assertEquals(results[8], '+---+---------+')
        self.assertEquals(len(results), 9)

    def test_text_title_1col(self):
        pv = PrettyValues()

        pv.newcol(0, '+5.2f')

        values = []
        values.append([23.45])
        values.append([200.4565])
        values.append([1.00])

        results = pv.text(values, title="Title").split('\n')

        self.assertEquals(results[0], '+---------+')
        self.assertEquals(results[1], '|  Title  |')
        self.assertEquals(results[2], '+---------+')
        self.assertEquals(results[3], '| 0       |')
        self.assertEquals(results[4], '+---------+')
        self.assertEquals(results[5], '| + 23.45 |')
        self.assertEquals(results[6], '| +200.46 |')
        self.assertEquals(results[7], '| +  1.00 |')
        self.assertEquals(results[8], '+---------+')
        self.assertEquals(len(results), 9)

    def test_format_lod(self):
        pv = PrettyValues()

        pv.newcol('bar', 'i')
        pv.newcol('sym', cname='Symbol')
        pv.newcol('close', '+5.2f')

        values = []
        values.append({'bar': 0, 'sym': 'yhoo', 'close': 23.45})
        values.append({'bar': 1, 'sym': 'goog', 'close': 200.4565})
        values.append({'bar': 2, 'sym': 'newp', 'close': 1.00})

        results = pv.format(values)

        self.assertEquals(results[0], ['bar', 'Symbol', 'close  '])
        self.assertEquals(results[1], ['  0', 'yhoo  ', '+ 23.45'])
        self.assertEquals(results[2], ['  1', 'goog  ', '+200.46'])
        self.assertEquals(results[3], ['  2', 'newp  ', '+  1.00'])
        self.assertEquals(len(results), 4)

    def test_format_lod_nocolumns(self):
        pv = PrettyValues()

        values = []
        values.append({'bar': 0, 'sym': 'yhoo', 'close': 23.45})
        values.append({'bar': 1, 'sym': 'goog', 'close': 200.4565})
        values.append({'bar': 2, 'sym': 'newp', 'close': 1.00})

        results = pv.format(values)

        self.assertEquals(results[0], ['close   ', 'bar', 'sym '])
        self.assertEquals(results[1], ['23.45   ', '0  ', 'yhoo'])
        self.assertEquals(results[2], ['200.4565', '1  ', 'goog'])
        self.assertEquals(results[3], ['1.0     ', '2  ', 'newp'])
        self.assertEquals(len(results), 4)

    def test_text_list(self):
        pv = PrettyValues()

        pv.newcol(0, 'i')
        pv.newcol(1, cname='Column2')
        pv.newcol(2, '+5.2f')

        values = [0, 'yhoo', 23.45]

        results = pv.text([values]).split('\n')

        self.assertEquals(results[0], '+---+---------+--------+')
        self.assertEquals(results[1], '| 0 | Column2 | 2      |')
        self.assertEquals(results[2], '+---+---------+--------+')
        self.assertEquals(results[3], '| 0 | yhoo    | +23.45 |')
        self.assertEquals(results[4], '+---+---------+--------+')
        self.assertEquals(len(results), 5)

    def test_text_dict(self):
        pv = PrettyValues()

        pv.newcol('bar', 'i')
        pv.newcol('sym', cname='Column2')
        pv.newcol('close', '+5.2f')

        values = {'bar': 0, 'sym': 'yhoo', 'close': 23.45}

        results = pv.text([values]).split('\n')

        self.assertEquals(results[0], '+-----+---------+--------+')
        self.assertEquals(results[1], '| bar | Column2 | close  |')
        self.assertEquals(results[2], '+-----+---------+--------+')
        self.assertEquals(results[3], '|   0 | yhoo    | +23.45 |')
        self.assertEquals(results[4], '+-----+---------+--------+')
        self.assertEquals(len(results), 5)

    def test_text_lod(self):
        pv = PrettyValues()

        pv.newcol('bar', 'i')
        pv.newcol('sym', cname='Symbol')
        pv.newcol('close', '+5.2f')

        values = []
        values.append({'bar': 0, 'sym': 'yhoo', 'close': 23.45})
        values.append({'bar': 1, 'sym': 'goog', 'close': 200.4565})
        values.append({'bar': 2, 'sym': 'newp', 'close': 1.00})
        values.append({'bar': 3, 'sym': 'nan', 'close': 'nan'})

        results = pv.text(values).split('\n')

        self.assertEquals(results[0], '+-----+--------+---------+')
        self.assertEquals(results[1], '| bar | Symbol | close   |')
        self.assertEquals(results[2], '+-----+--------+---------+')
        self.assertEquals(results[3], '|   0 | yhoo   | + 23.45 |')
        self.assertEquals(results[4], '|   1 | goog   | +200.46 |')
        self.assertEquals(results[5], '|   2 | newp   | +  1.00 |')
        self.assertEquals(results[6], '|   3 | nan    |     nan |')
        self.assertEquals(results[7], '+-----+--------+---------+')
        self.assertEquals(len(results), 8)

    def test_format_fill(self):
        pv = PrettyValues()

        pv.newcol(0, 'i')
        pv.newcol(1, vfill='.', cname='Column2')
        pv.newcol(2, '+5.2f', cname='Close', cformat='^', cfill='_')

        values = []
        values.append([0, 'yhoo', 23.45])
        values.append([1, 'goog', 200.4565])
        values.append([2, 'newp', 1.00])

        results = pv.format(values)

        self.assertEquals(results[0], ['0', 'Column2', '_Close_'])
        self.assertEquals(results[1], ['0', 'yhoo...', '+ 23.45'])
        self.assertEquals(results[2], ['1', 'goog...', '+200.46'])
        self.assertEquals(results[3], ['2', 'newp...', '+  1.00'])
        self.assertEquals(len(results), 4)

    def test_format_invalids(self):
        pv = PrettyValues()

        pv.newcol('open')

        values = []
        values.append({'bar': 0, 'sym': 'yhoo', 'close': 23.45})

        self.assertRaises(KeyError, pv.format, values)

        pv = PrettyValues()

        pv.newcol(2)

        values = []
        values.append([0, 'yhoo'])

        self.assertRaises(IndexError, pv.format, values)


if __name__ == "__main__":
    unittest.main()
