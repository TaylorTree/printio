#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2011, Mike Taylor
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
from core import PrettySeries


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
        
        
class PrettySeries_TestCase(unittest.TestCase):
    def setUp(self):
        pass
        
    def test_format_list(self):
        ps = PrettySeries()
        
        ps.addcolumn(0, 'i')
        ps.addcolumn(1, cname='Column2')
        ps.addcolumn(2, '+5.2f')
        
        series = []
        series.append([0, 'yhoo', 23.45])
        series.append([1, 'goog', 200.4565])
        series.append([2, 'newp', 1.00])
        
        results = ps.format(series)
        
        self.assertEquals(results[0], ['0', 'Column2', '2      '])
        self.assertEquals(results[1], ['0', 'yhoo   ', '+ 23.45'])
        self.assertEquals(results[2], ['1', 'goog   ', '+200.46'])
        self.assertEquals(results[3], ['2', 'newp   ', '+  1.00'])
        
    def test_format_list_noheader(self):
        ps = PrettySeries()
        
        ps.addcolumn(0, 'i')
        ps.addcolumn(1, cname='Column2')
        ps.addcolumn(2, '+5.2f')
        
        series = []
        series.append([0, 'yhoo', 23.45])
        series.append([1, 'goog', 200.4565])
        series.append([2, 'newp', 1.00])
        
        results = ps.format(series, useheader=False)
        
        self.assertEquals(results[0], ['0', 'yhoo   ', '+ 23.45'])
        self.assertEquals(results[1], ['1', 'goog   ', '+200.46'])
        self.assertEquals(results[2], ['2', 'newp   ', '+  1.00'])
        
    
    def test_format_list_nocolumns(self):
        ps = PrettySeries()
        
        series = []
        series.append([0, 'yhoo', 23.45])
        series.append([1, 'goog', 200.4565])
        series.append([2, 'newp', 1.00])
        
        results = ps.format(series)
        
        self.assertEquals(results[0], ['0', '1   ', '2       '])
        self.assertEquals(results[1], ['0', 'yhoo', '23.45   '])
        self.assertEquals(results[2], ['1', 'goog', '200.4565'])
        self.assertEquals(results[3], ['2', 'newp', '1.0     '])
        
        
    def test_text_list(self):
        ps = PrettySeries()
        
        ps.addcolumn(0, 'i')
        ps.addcolumn(1, cname='Column2')
        ps.addcolumn(2, '+5.2f')
        
        series = []
        series.append([0, 'yhoo', 23.45])
        series.append([1, 'goog', 200.4565])
        series.append([2, 'newp', 1.00])
        
        results = ps.text(series).split('\n')
        
        self.assertEquals(results[0], '+---+---------+---------+')
        self.assertEquals(results[1], '| 0 | Column2 | 2       |')
        self.assertEquals(results[2], '+---+---------+---------+')
        self.assertEquals(results[3], '| 0 | yhoo    | + 23.45 |')
        self.assertEquals(results[4], '| 1 | goog    | +200.46 |')
        self.assertEquals(results[5], '| 2 | newp    | +  1.00 |')
        self.assertEquals(results[6], '+---+---------+---------+')
        
    def test_format_dict(self):
        ps = PrettySeries()
        
        ps.addcolumn('bar', 'i')
        ps.addcolumn('sym', cname='Symbol')
        ps.addcolumn('close', '+5.2f')
        
        series = []
        series.append({'bar':0, 'sym':'yhoo', 'close':23.45})
        series.append({'bar':1, 'sym':'goog', 'close':200.4565})
        series.append({'bar':2, 'sym':'newp', 'close':1.00})
        
        results = ps.format(series)
        
        self.assertEquals(results[0], ['bar', 'Symbol', 'close  '])
        self.assertEquals(results[1], ['  0', 'yhoo  ', '+ 23.45'])
        self.assertEquals(results[2], ['  1', 'goog  ', '+200.46'])
        self.assertEquals(results[3], ['  2', 'newp  ', '+  1.00'])
        
    def test_format_dict_nocolumns(self):
        ps = PrettySeries()
        
        series = []
        series.append({'bar':0, 'sym':'yhoo', 'close':23.45})
        series.append({'bar':1, 'sym':'goog', 'close':200.4565})
        series.append({'bar':2, 'sym':'newp', 'close':1.00})
        
        results = ps.format(series)
        
        self.assertEquals(results[0], ['close   ', 'bar', 'sym '])
        self.assertEquals(results[1], ['23.45   ', '0  ', 'yhoo'])
        self.assertEquals(results[2], ['200.4565', '1  ', 'goog'])
        self.assertEquals(results[3], ['1.0     ', '2  ', 'newp'])
    
    def test_text_dict(self):
        ps = PrettySeries()
        
        ps.addcolumn('bar', 'i')
        ps.addcolumn('sym', cname='Symbol')
        ps.addcolumn('close', '+5.2f')
        
        series = []
        series.append({'bar':0, 'sym':'yhoo', 'close':23.45})
        series.append({'bar':1, 'sym':'goog', 'close':200.4565})
        series.append({'bar':2, 'sym':'newp', 'close':1.00})
        
        results = ps.text(series).split('\n')
        
        self.assertEquals(results[0], '+-----+--------+---------+')
        self.assertEquals(results[1], '| bar | Symbol | close   |')
        self.assertEquals(results[2], '+-----+--------+---------+')
        self.assertEquals(results[3], '|   0 | yhoo   | + 23.45 |')
        self.assertEquals(results[4], '|   1 | goog   | +200.46 |')
        self.assertEquals(results[5], '|   2 | newp   | +  1.00 |')
        self.assertEquals(results[6], '+-----+--------+---------+')
        
    
    def test_format_fill(self):
        ps = PrettySeries()
        
        ps.addcolumn(0, 'i')
        ps.addcolumn(1, vfill='.', cname='Column2')
        ps.addcolumn(2, '+5.2f', cname='Close', cformat='^', cfill='_')
        
        series = []
        series.append([0, 'yhoo', 23.45])
        series.append([1, 'goog', 200.4565])
        series.append([2, 'newp', 1.00])
        
        results = ps.format(series)
        
        self.assertEquals(results[0], ['0', 'Column2', '_Close_'])
        self.assertEquals(results[1], ['0', 'yhoo...', '+ 23.45'])
        self.assertEquals(results[2], ['1', 'goog...', '+200.46'])
        self.assertEquals(results[3], ['2', 'newp...', '+  1.00'])
        
    def test_format_invalids(self):
        ps = PrettySeries()
        
        ps.addcolumn('open')
        
        series = []
        series.append({'bar': 0, 'sym':'yhoo', 'close':23.45})
        
        self.assertRaises(KeyError, ps.format, series)
        
        ps = PrettySeries()
        
        ps.addcolumn(2)
        
        series = []
        series.append([0, 'yhoo'])
        
        self.assertRaises(IndexError, ps.format, series)
        
        

if __name__ == "__main__":
    unittest.main()