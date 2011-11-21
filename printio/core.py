#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2011, Mike Taylor
#
# This file is part of printio released under MIT license.
# See the LICENSE for more information.

"""

Pretty-up your data for print or display.

"""

import re
import sys
try:
    from cStringIO import StringIO
    
except:
    from StringIO import StringIO


class PrettyValue(object):
    """Pretty up a value by converting to string.
    
    Examples:
    >>> pv = PrettyValue('+10.2f')
    >>> pv.format('23.4567')
    '+    23.46'
    
    >>> pv = PrettyValue('^10s', fill='*')
    >>> pv.format('Center')
    '**Center**'
    """
    def __init__(self, rawtext=None,
                       fill=None,
                       align=None,
                       width=None):
        """
        :param rawtext: (optional) type of value to format.
            * 's': string
            * 'i': integer
            * 'f': float
            * '%': percent
        :param fill: (optional) character to fill leftover space.
        :param align: (optional) align the value in the total space.
            * left: left-align value (default for strings).
            * center: center-align value.
            * right: right-align value.
            * rightpad: right-align numeric values with padding
                after sign (default for numbers).
        :param width: (optional) length of formatted string.
        """
        self.aligns = {}
        self.aligns['<'] = ('left', '<')
        self.aligns['^'] = ('center', '^')
        self.aligns['>'] = ('right', '>')
        self.aligns['='] = ('rightpad', '=')
        
        self.aligns['left'] = self.aligns['<']
        self.aligns['center'] = self.aligns['^']
        self.aligns['right'] = self.aligns['>']
        self.aligns['rightpad'] = self.aligns['=']
        
        self.validsigns = ('+', '-', ' ')
        
        self.validstrings = ('s', '')
        self.validints = ('d','i')
        self.validfloats = ('f', '%')
        
        self.validnums = []
        self.validnums.extend(self.validints)
        self.validnums.extend(self.validfloats)
        
        self.knowntypes = []
        self.knowntypes.extend(self.validstrings)
        self.knowntypes.extend(self.validnums)
        
        _text = r"""
                 ([<^>=]{1})?   #0 or 1 align specifier
                 ([\s+-]{1})?   #0 or 1 sign specifier
                 (\s+)?         #0 or 1 spaces that shouldn't be there.
                 (\d+)?         #0 or 1 width specifier
                 (\.+\d+)?      #decimal and precision specifier
                 (.+)?$         #what's left 
                """
        
        self.regex = re.compile(_text, re.VERBOSE)
        
        self.setoptions(rawtext,
                        fill=fill,
                        align=align,
                        width=width)
        
    def setoptions(self, rawtext=None,
                         fill=None,
                         align=None,
                         width=None):
        """Set the formatting options for the values passed.
        
        :param rawtext: (optional) type of value to format.
            * 's': string
            * 'i': integer
            * 'f': float
            * '%': percent
        :param fill: (optional) character to fill leftover space.
        :param align: (optional) align the value in the total space.
            * left: left-align value (default for strings).
            * center: center-align value.
            * right: right-align value.
            * rightpad: right-align numeric values with padding
                after sign (default for numbers).
        :param width: (optional) length of formatted string.
        """
        self.maxwidth = 0
        
        self.set_fill(fill)
        
        options = self.parse_rawtype(rawtext)
        
        self.set_atype(options['atype'])
        
        if align:
            self.set_align(align)
            
        else:
            self.set_align(options['align'])
        
        self.set_sign(options['sign'])
        
        if width:
            self.set_width(width)
            
        else:
            self.set_width(options['width'])
        
        self.set_precision(options['precision'])
        
        
    def parse_rawtype(self, rawtype=None):
        """Returns the various format specifiers parsed from the 
        string, rawtype.
        
        :param rawtext: (optional) type of value to format.
            * 's': string
            * 'i': integer
            * 'f': float
            * '%': percent
        :rtype: dictionary of format specifiers.
        """
        results = {}
        results['atype'] = None
        results['align'] = None
        results['sign'] = None
        results['width'] = None
        results['precision'] = None
        
        if not rawtype:
            return results
            
        rawtype = rawtype.rstrip()
        
        match = self.regex.search(rawtype)
        if not match:
            return results
            
        groups = match.groups()
        
        bar = 0
        results['align'] = groups[bar]
        
        bar += 1
        results['sign'] = groups[bar]
        
        bar += 2
        if groups[bar]:
            results['width'] = int(groups[bar])
            
        bar += 1
        if groups[bar]:
            results['precision'] = int(groups[bar].lstrip('.'))
        
        bar += 1
        if groups[bar]:
            results['atype'] = groups[bar].strip()
            
        return results

    
    def set_atype(self, atype=None):
        """
        :param atype: (optional) type of value to format.
            * 's': string
            * 'i': integer
            * 'f': float
            * '%': percent
        """
        self.atype = ''
        self._atype = ''
        self.typesummary = ''
        
        if atype:
            self.atype = atype
            self._atype = atype
            
            if atype == 'i':
                self._atype = 'd'
        
        if self.atype in self.validstrings:
            self.typesummary = 'str'
            return None
            
        if self.atype in self.validints:
            self.typesummary = 'int'
            return None
            
        if self.atype in self.validfloats:
            self.typesummary = 'float'
            return None
            
        self.typesummary = 'unknown'
        if len(self.atype) <= 1:
            msg = "invalid atype: '%s'" % self.atype
            raise ValueError(msg)
    
    
    def set_align(self, align=None):
        """Sets the alignment options for the formatted value.
            
        :param align: (optional) align the value in the total space.
            * left or <: left-align value (default for strings).
            * center or ^: center-align value.
            * right or >: right-align value (default for numbers).
            * rightpad or =: right-align number with padding after sign.
        """
        self.align = ''
        
        if not align:
            if self.atype in self.validnums:
                self.align = '='
                
            else:
                self.align = '<'
                
            return None
            
        if align not in self.aligns:
            msg = "invalid align:'%s', atype:'%s'" % (align, self.atype)
            raise ValueError(msg)
            
        _alignment, _align = self.aligns[align]
        
        if _align == '=' and self.atype not in self.validnums:
            msg = "invalid align for non-numeric types: "
            msg = "%s align:'%s', atype:'%s'" % (msg, align, self.atype)
            raise ValueError(msg)
            
        self.align = _align

    def set_fill(self, fill=None):
        """Specify how to fill the remaining space in the string.
        
        :param fill: (optional) fill character for the leftover space.
        """
        self.fill = ''
        
        if fill or fill == 0 or fill == ' ':
            self.fill = str(fill)


    def set_sign(self, sign=None):
        """Specify how to sign the numeric value in the string.
        
        :param sign: (optional) show the sign of the field.
            * '+': show '+' if positive number and '-' if negative.
            * '-': only show '-' for negative numbers.
            * ' ': show ' ' for positive numbers, '-' if negative.
        """
        self.sign = ''
        
        if not sign:
            if self.atype in self.validnums:
                self.sign = '-'
               
            return None

        if self.atype not in self.validnums:
            msg = "sign invalid for non-numeric types: "
            msg = "%s sign:'%s', atype:'%s'" % (msg, sign, self.atype)
            raise ValueError(msg)
    
        if sign not in self.validsigns:
            msg = "sign invalid specifier: "
            msg = "%s sign:'%s', atype:'%s'" % (msg, sign, self.atype)
            raise ValueError(msg)
    
        self.sign = sign


    def set_width(self, width=None):
        """Specify the length of the formatted string.
        
        :param width: (optional) size of the destination string.
        """
        self.width = ''
        if width:
            self.width = int(width)
    
    def set_precision(self, precision=None):
        """Specify how many decimal points to show.
        
        :param precision: (optional) how many digits to the right of the
            decimal place to show.
                * default is 4.
        """
        self.precision = ''
        
        if not precision:
            if self.atype in self.validfloats:
                self.precision = 4
                
            return None
        
        if self.atype not in self.validfloats:
            msg = "precision invalid for non-float types, "
            msg = "%s precision:'%s', atype:'%s'" % (msg, precision, self.atype)
            raise ValueError(msg)
            
        try:
            self.precision = int(precision)
            
        except ValueError:
            msg = "invalid precision specifier, "
            msg = "%s precision:'%s', atype:'%s'" % (msg, precision, self.atype)
            raise ValueError(msg)

    def format(self, value):
        """Returns a formatted string based on the format specifiers.
        
        :param value: value to format.
        :rtype: pretty formatted string.
        """
        newvalue = value
        newatype = self._atype
        
        if self.typesummary == 'str':
            newvalue = str(value)
            
        elif self.typesummary == 'int':
            newvalue = int(value)
            
        elif self.typesummary == 'float':
            newvalue = float(value)
            
        elif self.typesummary == 'unknown':
            formatspecs = '{0:%s}' % (newatype,)
            newvalue = formatspecs.format(newvalue)
            newatype = 's'
        
        newprecision = ''
        if self.precision:
            newprecision = '.%s' % self.precision
            
        formatspecs = '{%s:%s%s%s%s%s%s}' % (0,
                                             self.fill,
                                             self.align,
                                             self.sign,
                                             self.width,
                                             newprecision,
                                             newatype)

        #print formatspecs
        result = formatspecs.format(newvalue)

        newwidth = len(result)
        if newwidth > self.maxwidth:
            self.maxwidth = newwidth
            
        return result


class PrettySeries(object):
    """Pretty-up a series of values based on various formatting
    options.
    
    Examples:
    >>> series = [['yhoo', 23.4564], ['goog', 200]]
    >>> ps = PrettySeries()
    >>> ps.addcolumn(0, cname='Symbol')
    >>> ps.addcolumn(1, '+.2f', cname='Closing Price')
    >>> results = ps.format(series)
    >>> results[0]
    ['Symbol', 'Closing Price']
    >>> results[1]
    ['yhoo  ', '+       23.46']
    >>> results[2]
    ['goog  ', '+      200.00']
    """
    def __init__(self):
        self.columns = []
        self.cformatters = {}
        self.vformatters = {}

    def addcolumn(self, 
                  key, 
                  vformat=None, 
                  vfill=None,
                  cname=None, 
                  cformat=None,
                  cfill=None):
        """Specify column attributes for prettying up your series.
        
        :param key: index of the list or the key of the dict to format.
        :param vformat: (optional) format specifier of the values 
            for the column.
        :param vfill: (optional) fill character for the values.
        :param cname: (optional) name of the column.
        :param cformat: (optional) format specifier for the column name.
        :param cfill: (optional) fill character for the column name.
        """
                  
        if not cname:
            cname = key
            
        self.vformatters[key] = PrettyValue(vformat, vfill)
        
        self.cformatters[key] = PrettyValue(cformat, cfill)
        
        self.columns.append([key, cname])
        
    def text(self, series, useheader=True):
        """
        >>> lol = []
        >>> lol.append([0, 'yhoo', 23.45])
        >>> lol.append([1, 'goog', 200.4565])
        >>> lol.append([2, 't', 1.00])
        >>> keys = ['bar', 'symbol', 'close']
        >>> lod = [dict(zip(keys, x)) for x in lol]
        >>> ps = PrettySeries()
        >>> for row in ps.format(lol): print row
        """
        records = self.format(series, useheader)
        
        if not records:
            return ''
        
        output = StringIO()
        
        #build the header record.
        dashes = '+'
        bar = 0
        
        headers = '|'
        for value in records[0]:
            headers = ''.join((headers, ' ', value, ' |'))
            dashes = ''.join((dashes, '-' * (len(value) + 2), '+'))
        
        if useheader:
            line = ''.join((dashes, '\n'))
            output.write(line)
            line = ''.join((headers, '\n'))
            output.write(line)
            bar += 1
        
        
        details = records[bar:]
        
        if details:
            line = ''.join((dashes, '\n'))
            output.write(line)
            
            for values in details:
                rows = '|'
                for value in values:
                    rows = ''.join((rows, ' ', value, ' |'))
                    
                line = ''.join((rows, '\n'))
                output.write(line)
            
            
        lines = output.getvalue()
        
        if lines:
            lines = ''.join((lines, dashes))
        
        return lines
        
    
    def format(self, series, useheader=True):
        """Return a pretty formatted list of lists based on the 
        format specifiers of the columns.
        
        :param series: list of lists or dicts to pretty format.
        :useheader: (optional) whether to display the column header.
            * default is True
        """
        results = []
        
        sizes = {}
        
        #-------------------------------------------------------------------------------------------------
        #if user doesn't provide a set of columns then provide default column headings.  Either:
        #   * indicies from a list or
        #   * keys from a dictionary.
        #-------------------------------------------------------------------------------------------------
        if not self.columns:
            if not series:
                return results
                
            try:
                keys = series[0].keys()
                
            except AttributeError:
                keys = range(len(series[0]))
                
            for key in keys:
                self.addcolumn(key)
                
        for key, cname in self.columns:
            sizes[key] = 0
            
        #This is the 1st pass to determine the maximum size of each column.
        for row in series:
            for key, cname in self.columns:
                pv = self.vformatters[key]
                try:
                    oldvalue = row[key]
                    
                except KeyError:
                    msg = "Invalid key: '%s' row: %s" % (key, row)
                    raise KeyError(msg)
                
                newvalue = pv.format(oldvalue)
                if pv.maxwidth > sizes[key]:
                    sizes[key] = pv.maxwidth
    
        #Build the column headings with the maximum size of the column.
        headers = []
        for key, cname in self.columns:
            pc = self.cformatters[key]
            newcolumn = pc.format(cname)
            
            pv = self.vformatters[key]
            if pv.maxwidth > pc.maxwidth:
                pc.set_width(pv.maxwidth)
                pv.set_width(pv.maxwidth)
                
                newcolumn = pc.format(cname)
            
            else:
                pv.set_width(pc.maxwidth)
                
            headers.append(newcolumn)

        if useheader:
            results.append(headers)
        
        #Now that you know the maximum size of the columns...format based on that size.
        for row in series:
            record = []
            for key, cname in self.columns:
                pv = self.vformatters[key]
                newvalue = pv.format(row[key])
                record.append(newvalue)
    
            results.append(record)
    
        
        return results

def _testit(verbose=None):
    import doctest
    doctest.testmod(verbose=verbose)

if __name__ == "__main__":
    _testit()
    #print "** Need to create an autonum column for reporting **"
    #print "** Need to add test cases for autonum **"
    #print "** Need to add tb_html **"
    #print "** Need to add pre_html **"
    