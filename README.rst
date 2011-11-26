printio
=======
*printio* is a MIT licensed pretty printing library implemented in Python.

Format a value(s) for printing or display using Python's built-in String Format library.

Most of the string formatting options from the Format Specification Mini-Language are available.  See the formatting options here:
    http://docs.python.org/release/3.1.2/library/string.html#format-specification-mini-language


Features
--------
 - Align values to the left, right, or center.
 - Pad and fill values.
 - Sign numerical values.
 - Convert integers to float.
 - Specify precision for floating values - values are rounded up.
 - Convert numbers to percentage formats.  Ex. 0.10 ~ 10.0000%
 - Add column headers or utilize default headers for your values.
 - Column widths are automatically sized based on maximum width of the values.
 - Choose which columns to format in your values.
 - Ability to print to 'text' similar to how MySQL displays output to the console.


Overview
--------
The major functions of printio:

 - *PrettyValue():*
    Formats a single value to a string.

 - *PrettyValues():*
    Formats a list or dict of values.
        - format: will return a list of strings including the header.
        - text: will return a string similar to MySQL's console display format.

    
License
-------
Made available under the MIT License.


Usage
-----
First, some housekeeping items...

Import the library ::
    
    >>> from printio import PrettyValue
    >>> from printio import PrettyValues

Create a list of values you wish to format. ::

    >>> lol = []
    >>> lol.append([0, 'yhoo', 23.45])
    >>> lol.append([1, 'goog', 200.4565])
    >>> lol.append([2, 't', 1.00])
    
Let's also create a list of dictionaries to format as well. ::
    
    >>> keys = ['bar', 'symbol', 'close']
    >>> lod = [dict(zip(keys, x)) for x in lol]
    
Now, let's get down to business...
    
Format a string with a width of 10, center-aligned, and filled with '-'. ::
    
    >>> value = 'yhoo'
    >>> pv = PrettyValue('^10', fill='-')
    >>> pv.format(value)
    ---yhoo---

Format a float with a decimal precision of 1. ::
    
    >>> value = 23.45599
    >>> pv = PrettyValue('.1f')
    >>> pv.format(value)
    '23.5'

Format a float into a percentage. ::
    
    >>> value = 0.025
    >>> pv = PrettyValue('.2%')
    >>> pv.format(value)
    '2.50%'

Format a list. ::
    
    >>> pv = PrettyValues()
    >>> for row in pv.format(lol[0]): print row
    ['0', '1   ', '2    ']
    ['0', 'yhoo', '23.45']
    
Format a dict. ::
    
    >>> pv = PrettyValues()
    >>> pv.addcol('bar')
    >>> pv.addcol('symbol')
    >>> pv.addcol('close')
    >>> for row in pv.format(lod[0]): print row
    ['bar', 'symbol', 'close']
    ['0  ', 'yhoo  ', '23.45']
    
Format a list of lists. ::
    
    >>> pv = PrettyValues()
    >>> for row in pv.format(*lol): print row
    ['0', '1   ', '2       ']
    ['0', 'yhoo', '23.45   ']
    ['1', 'goog', '200.4565']
    ['2', 't   ', '1.0     ']

Same as above but this time in text. ::
    
    >>> pv = PrettyValues()
    >>> results = pv.text(*lol)
    >>> print results
    +---+------+----------+
    | 0 | 1    | 2        |
    +---+------+----------+
    | 0 | yhoo | 23.45    |
    | 1 | goog | 200.4565 |
    | 2 | t    | 1.0      |
    +---+------+----------+

Want to add better column names? ::
    
    >>> pv.addcol(0, cname='Bar')
    >>> pv.addcol(1, cname='Symbol')
    >>> pv.addcol(2, cname='Close')
    >>> print pv.text(*lol)
    +-----+--------+----------+
    | Bar | Symbol | Close    |
    +-----+--------+----------+
    | 0   | yhoo   | 23.45    |
    | 1   | goog   | 200.4565 |
    | 2   | t      | 1.0      |
    +-----+--------+----------+

Print only the Close column, always show sign, and format with decimal precision of 2. ::
    
    >>> pv = PrettyValues()
    >>> pv.addcol(2, '+.2f', cname='Close')
    >>> print pv.text(*lol)
    +---------+
    | Close   |
    +---------+
    | + 23.45 |
    | +200.46 |
    | +  1.00 |
    +---------+

Print list of dictionaries with the numerical settings for the bar & close. ::
    
    >>> pv = PrettyValues()
    >>> pv.addcol('bar', 'i')
    >>> pv.addcol('symbol')
    >>> pv.addcol('close', '.2f')
    >>> print pv.text(*lod)
    +-----+--------+--------+
    | bar | symbol | close  |
    +-----+--------+--------+
    |   0 | yhoo   |  23.45 |
    |   1 | goog   | 200.46 |
    |   2 | t      |   1.00 |
    +-----+--------+--------+


Roadmap
-------
* Add option to display title in addition to column headings.
* Add autonum column ability.
* Add tb_html to format to a html table.
* Add pre_html to format <pre> html </pre>.


For additional information, please email:
    mike@taylortree.com