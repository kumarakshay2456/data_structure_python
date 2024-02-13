from os import *
from sys import *
from collections import *
from math import *


def findCommonElements(a,b,c):
    # Write your code here.
    # Return a list containing all common elements.
    if len(a) <= len(b) and len(a) <= len(c):
        return [arr for arr in set(a) if arr in b and arr in c]
    elif len(b) <= len(a) and len(b) <= len(c):
        return [arr for arr in set(b) if arr in a and arr in c]
    else:
        return [arr for arr in set(c) if arr in b and arr in a]



