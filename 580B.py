#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : 580B.py
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

def solve(arr, n, min_diff):
    # We want max profit so taking the greedy approach
    arr = sorted(arr)
    ans, mx = 0, 0
    j = 0

    """
    We need to choose a subsegment that where the minimum diff  is <= threshold
    So we sort them according to the money they have..

    """
    for i in range(n):
        ans += arr[i][1]

        while arr[i][0] - arr[j][0] >= min_diff:
            ans -= arr[j][1]
            j += 1
       
        mx = max(mx, ans)
    print(mx)


def main():
    n, min_diff = input_as_array()
    arr = []
    for i in range(n):
        m, ff = input_as_array()
        arr.append((m, ff))
    solve(arr, n, min_diff)

if __name__ == "__main__":
    LOCAL = False
    #LOCAL = True

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
