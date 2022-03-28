#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : 1366B.py
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
    n, x, m = input_as_array()
    A = [0] * (n+1)
    A[x] = 1
    print(A)

    for i in range(m):
        l, r = input_as_array()
    print("***************************")


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
