#!/bin/python3

import math
import os
import random
import re
import sys
import pytest


if __name__ == '__main__':

    a = int(input())
    b = int(input())

    # check for valid input range for a and b
    if(1 <= a <= 100) and (1 <= b <= 100):
        # do operations - print output
        print(a + b)
        print(a - b)
        print(a * b)