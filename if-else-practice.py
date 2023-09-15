#!/bin/python3

import math
import os
import random
import re
import sys
import pytest



if __name__ == '__main__':
    n = int(input().strip())

    # valid range for n 1...100
    if(1 <= n <= 100 ):

        # odd
        if(n % 2):
            print("Weird")

        # even and in weird even range
        elif(6 <= n <= 20): 
            print("Weird")

        # even and not in weird range
        else:
            print("Not Weird")

    else: 
        print("not within the valid range")