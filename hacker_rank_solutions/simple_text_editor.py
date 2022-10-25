#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Jaime Bowen Varela


# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())

inputs = []
for i in range(n):
    lol = input()
    lol = lol.split()
    inputs.append(lol)
line = ""
line0 = ""
pass_results = [line]
resets = 0
for n, i in enumerate(inputs):
    inst = i[0]
    try:
        val = i[1]
    except:
        val = 0
    if inst == "1":
        line = line + val
        pass_results.append(line)
    elif inst == "3":
        index = int(val) - 1
        print(line[index])
    elif inst == "2":
        index = int(val)
        line = line[:-index]
        pass_results.append(line)
    elif inst == "4":
        line = pass_results[-2]
        pass_results.pop()
    else:
        pass
