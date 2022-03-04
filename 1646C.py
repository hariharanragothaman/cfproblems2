#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : 1646C.py
# Author            : cppygod
# Date              : 11.02.2022
# Last Modified Date: 04.03.2022
# Last Modified By  : cppygod
# NECESSARY IMPORTS
import os, sys, math, cmath, time, collections
from collections import deque, Counter, OrderedDict, defaultdict
from heapq import nsmallest, nlargest, heapify, heappop, heappush, heapreplace
from math import ceil, floor, log, log2, sqrt, gcd, factorial, pow, pi
from bisect import bisect_left, bisect_right
from itertools import accumulate, permutations, combinations, combinations_with_replacement
from io import BytesIO, IOBase
from functools import reduce


# SOME GENERAL HELPER
def input_as_array(): return list(map(int, input().split()))

start_time = time.time()

def main(SS):
    n = int(input())
    
    # Every number can be represented as a power of 2
    # Maxlimit we use all the powers - 40 
    res = 40
    
    for t in range(1 << len(SS)):
        sm = 0
        for i in range(len(SS)):
          if (t >> i) & 1: 
              sm += SS[i]
        
        if n - sm >= 0: 
            res = min(res, bin(t).count("1") + bin(n - sm).count("1"))
    print(res)

if __name__ == "__main__":
    LOCAL = False

    # If it's Local - Get I/P from file
    if LOCAL:
        sys.stdin = open("data.in", "r")
        sys.stdout = open("data.out", "w")

    testcases = int(input())
    
    # Common-area to do some calculation for all test-cases

    m = 10 ** 12
    SS = []
    f, x = 2, 3

    while f <= m:
        f *= x
        SS.append(f)
        x += 1

    for i in range(testcases):
        main(SS)

    # Common-area Ends for all test-cases

    # If it's local - Print this O/P
    if LOCAL:
        print(f"Time Elapsed: {time.time() - start_time} seconds")
        sys.stdout.close()
