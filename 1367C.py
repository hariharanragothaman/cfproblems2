#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : 1367C.py
# Author            : cppygod
# Date              : 28.01.2022
# Last Modified Date: 23.02.2022
# Last Modified By  : cppygod

import os
from io import BytesIO, IOBase
import sys, math, cmath, time, collections
from collections import deque, Counter, OrderedDict, defaultdict
from heapq import nsmallest, nlargest, heapify, heappop, heappush, heapreplace
from math import ceil, floor, log, log2, sqrt, gcd, factorial, pow, pi
from bisect import bisect_left, bisect_right
from itertools import permutations, combinations, combinations_with_replacement, groupby 

# SOME GENERAL HELPER
def input_as_array(): return list(map(int, input().split()))

start_time = time.time()


def main():
    n, k = input_as_array()
    A = [int(c) for c in input()]
    """
    Thoughts:
        The number of 0's to 1 is what we need
        We need to change the value greedily.
        Finally we can send changed - original difference

        We need to do - all(s[i] == '0' for i in range(start, end)))
        but that will TLE....

        We can have a running count?
    """
    
    prev = sum(A)
    s = 0

    for i in range(min(k, n)):
        s += A[i]
    
    for i in range(n):
        if i + k < n:
            s += A[i + k]
        if s == 0:
            A[i] = 1
            s += 1
 
        if 0 <= i - k:
            s -= A[i - k]
    
    print(sum(A) - prev)

if __name__ == "__main__":
    if os.path.exists('data.in'):
        sys.stdin = open("data.in", "r")
        sys.stdout = open("data.out", "w")

    testcases = int(input())
    for i in range(testcases):
        main()

    if os.path.exists('data.in'):
        print(f"Time Elapsed: {time.time() - start_time} seconds")
        sys.stdout.close()
