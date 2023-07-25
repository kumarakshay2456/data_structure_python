"""
you-are-given-an-array-arr-of-size-n-your-task-is-to-find-out-the-sum-of-maximum-and-minimum-elements-in-the-array
"""

from os import *
from sys import *
from collections import *
from math import *


def sumOfMaxMin(arr):
    # Write your code here
    min_number = 999999999999
    max_number = -999999999999
    for i in arr:
        if i >= max_number:
            max_number = i
        if i <= min_number:
            min_number = i
    return min_number + max_number
