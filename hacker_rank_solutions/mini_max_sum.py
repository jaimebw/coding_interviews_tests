#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Jaime Bowen Varela
def miniMaxSum(arr):
    # Write your code here
    min_val = min(arr)
    max_val = max(arr)
    all_sum = 0

    for i in arr:
        all_sum += i
    print(all_sum - max_val, all_sum - min_val)


test = [1, 2, 3, 4, 5]

miniMaxSum(test)
