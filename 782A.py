#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : 782A.py
# Author            : cppygod
# Date              : 24.03.2022
# Last Modified Date: 24.03.2022
# Last Modified By  : cppygod
# -*- coding: utf-8 -*-
# @Author: hariharanragothaman
# @Date:   2022-03-24 13:41:01
# @Last Modified by:   hariharanragothaman
# @Last Modified time: 2022-03-24 15:45:05

import os, sys, math, cmath, time, collections
from collections import deque, Counter, OrderedDict, defaultdict
from heapq import nsmallest, nlargest, heapify, heappop, heappush, heapreplace
from math import ceil, floor, log, log2, sqrt, gcd, factorial, pow, pi
from bisect import bisect_left, bisect_right

# SOME GENERAL HELPER
def input_as_array(): return list(map(int, input().split()))

start_time = time.time()


def main():
    n = int(input())
    A = input_as_array()
    mx = 0
    ctr = Counter()
    cnt = 0
    for c in A:
        if ctr[c] > 0:
            ctr[c] -= 1
            cnt -= 1
        else:
            ctr[c] += 1
            cnt += 1
        mx = max(mx, cnt)
    print(mx)



if __name__ == "__main__":
    if os.path.exists('data.in'):
        sys.stdin = open("data.in", "r")
        sys.stdout = open("data.out", "w")

    testcases = 1
    for i in range(testcases):
        main()

    # If it's local - Print this O/P
    if os.path.exists('data.in'):
        print(f"Time Elapsed: {time.time() - start_time} seconds")
        sys.stdout.close()
