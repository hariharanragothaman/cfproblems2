#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : 580C.py
# Author            : cppygod
# Date              : 28.01.2022
# Last Modified Date: 22.02.2022
# Last Modified By  : cppygod

import os
from io import BytesIO, IOBase
import sys, math, cmath, time, collections
from collections import deque, Counter, OrderedDict, defaultdict
from heapq import nsmallest, nlargest, heapify, heappop, heappush, heapreplace
from math import ceil, floor, log, log2, sqrt, gcd, factorial, pow, pi
from bisect import bisect_left, bisect_right
from itertools import permutations, combinations, combinations_with_replacement


# SOME GENERAL HELPER
def input_as_array(): return list(map(int, input().split()))

start_time = time.time()


def main():
    n, m = input_as_array()
    has_cat = [0] + input_as_array()
    

    g = defaultdict(list)
    for i in range(n-1):
        u, v = input_as_array()
        g[u].append(v)
        g[v].append(u)

    
    print(g)

    q = deque([])
    q.append((1, 0, 0))


    cnt = 0
    while q:
        k, c, p = q.pop()
        
        # crucial trick.. that I have done....
        c = has_cat[k] * (c+1)

        if c > m:
            continue 
        
        if len(g[k]) == 1 and k != 1:
            cnt += 1
            continue 

        for children in g[k]:
            if children != p:
                q.append((children, c, k))

    print(cnt)



if __name__ == "__main__":
    #LOCAL = False
    LOCAL = True

    # If it's Local - Get I/P from file
    if LOCAL:
        sys.stdin = open("data.in", "r")
        sys.stdout = open("data.out", "w")

    testcases = 1
    for i in range(testcases):
        main()

    # If it's local - Print this O/P
    if LOCAL:
        print(f"Time Elapsed: {time.time() - start_time} seconds")
        sys.stdout.close()
