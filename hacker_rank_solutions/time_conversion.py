#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Jaime Bowen Varela
def timeConversion(s):
    # Write your code here
    if s[-2:] == "PM":
        if s[0:2] == "12":
            pass
        else:
            s = s.replace(s[0:2], str(int(s[0:2]) + 12))
        s = s.replace("PM", "")
    else:
        s = s.replace("AM", "")
        if s[0:2] == "12":
            s = s.replace(s[0:2], "00")
    return s


test = "07:05:45PM"
output = "19:05:45"

if output == timeConversion(test):
    print("Good")
