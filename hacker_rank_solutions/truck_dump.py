#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Jaime Bowen Varela
def solve(petrol, distance, n):
    start, tank = 0, 0
    for i in range(n):  # Start from each index
        start = i
        tank = 0  # Reset the tank for each iteration
        for j in range(n):
            current = (
                start + j
            ) % n  # 0         #To make the index in range for circular array
            print(current)
            tank += (
                petrol[current] - distance[current]
            )  # Add the petrol and subtract the petrol required to reach next station
            if (
                tank < 0
            ):  # If petrol in tank becomes negative, we cannot complete the loop
                break
            if j == n - 1:  # If we visit all n pumps, task is completed
                return start


petrol = [10, 4]
distance = [13, 1]
print(solve(petrol, distance, 2))
