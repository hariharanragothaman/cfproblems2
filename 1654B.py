#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : 1654B.py
# Author            : cppygod
# Date              : 23.03.2022
# Last Modified Date: 23.03.2022
# Last Modified By  : cppygod
# -*- coding: utf-8 -*-
# @Author: hariharanragothaman
# @Date:   2022-03-23 20:11:42
# @Last Modified by:   hariharanragothaman
# @Last Modified time: 2022-03-23 20:47:05


import os, sys, math, cmath, time, collections
from collections import deque, Counter, OrderedDict, defaultdict
from heapq import nsmallest, nlargest, heapify, heappop, heappush, heapreplace
from math import ceil, floor, log, log2, sqrt, gcd, factorial, pow, pi
from bisect import bisect_left, bisect_right

# SOME GENERAL HELPER
def input_as_array(): return list(map(int, input().split()))

start_time = time.time()


def main():
    s = input()
    n = len(s)
    ctr = Counter(s)

    i = 0
    while i < n:
        if ctr[s[i]] > 1:
            ctr[s[i]] -= 1;
        else:
            break 
        i += 1
    print(s[i:])

if __name__ == "__main__":
    if os.path.exists('data.in'):
        sys.stdin = open("data.in", "r")
        sys.stdout = open("data.out", "w")

    testcases = int(input())
    for i in range(testcases):
        main()

    # If it's local - Print this O/P
    if os.path.exists('data.in'):
        print(f"Time Elapsed: {time.time() - start_time} seconds")
        sys.stdout.close()
