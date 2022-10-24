#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Jaime Bowen Varela
def minimumBribes(q):
    bribes = 0
    for i in range(len(q)-1,-1,-1):
        print(f"i:{i}\n")
        if q[i] - (i + 1) > 2:
            print('Too chaotic')
            return
        for j in range(max(0, q[i] - 2),i):
            print(max(0,q[i]-2),i)
            if q[j] > q[i]:
                bribes+=1
    print(bribes)

def minimumBribes2(q):
    bribe = 0
    for i in range(len(q)-1,0,1):
        print(q)
        if q[i] != i+1:
            if q[i-1] == i+1:
                bribe +=1
                q[i-1],q[i] = q[i],q[i-1] # swapping values for counting
            elif q[i-2] ==i+1:
                bribe +=2
                q[i-2],q[i-1],q[i] = q[i-1],q[i],q[i-2]
            else:
                print("Too chaotic")
                return 
    print(bribe)
line = [3,1,2,4]
minimumBribes2(line)
