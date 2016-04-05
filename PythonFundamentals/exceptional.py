"""A module for demonstrating exceptions"""
# the import pint_function is needed because this is Python 2.7
from __future__ import print_function
from math import log
import sys

def convert(s):
    """Convert to an integer."""
    x = -1
    try:
        x = int(s)
        print("Conversion succeeded! x = ", x)
    except(ValueError, TypeError) as e:
        # print function accepts a the file parameter as a keyword argument
        # this is possible due to the import statement above
        print("Conversion failed: {}".format(str(e)), file = sys.stderr)
    return x

def string_log(s):
    v = convert(s)
    return log(v)
