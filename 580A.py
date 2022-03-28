#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : 580A.py
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
from itertools import permutations, combinations, combinations_with_replacement


# SOME GENERAL HELPER
def input_as_array(): return list(map(int, input().split()))

start_time = time.time()


def main():
    n = int(input())
    arr = input_as_array()
    max_cnt = 1
    cnt = 1

    for i in range(1, n):
        if arr[i] >= arr[i-1]:
            cnt += 1
            max_cnt = max(cnt, max_cnt)
        else:
            cnt = 1
    print(max_cnt)

if __name__ == "__main__":
    if os.path.exists('data.in'):
        sys.stdin = open("data.in", "r")
        sys.stdout = open("data.out", "w")

    testcases = 1
    for i in range(testcases):
        main()

    if os.path.exists('data.in'):
        print(f"Time Elapsed: {time.time() - start_time} seconds")
        sys.stdout.close()
