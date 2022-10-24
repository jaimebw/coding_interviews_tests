#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Jaime Bowen Varela
import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    sum_p,sum_zero, sum_neg = 0,0,0
    for i in arr:
        if i >0:
            sum_p +=1
        elif i == 0:
            sum_zero +=1
        else:
            sum_neg +=1
    
    print(sum_p/len(arr))
    print(sum_neg/len(arr))
    print(sum_zero/len(arr))


test_input = [-4,3,-9,0,4,1]

plusMinus(test_input)

