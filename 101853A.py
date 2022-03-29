#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : 101853A.py
# Author            : cppygod
# Date              : 10.02.2022
# Last Modified Date: 11.02.2022
# Last Modified By  : cppygod

import sys, math, cmath, time, collections
from collections import deque, Counter, OrderedDict, defaultdict
from heapq import nsmallest, nlargest, heapify, heappop, heappush, heapreplace
from math import ceil, floor, log, log2, sqrt, gcd, factorial, pow, pi
from bisect import bisect_left, bisect_right
from itertools import chain, permutations, combinations

# SOME GENERAL HELPER
def input_as_array(): return list(map(int, input().split()))

start_time = time.time()

def main():
    n, q = input_as_array()
    arr = input_as_array()

    ctr = Counter(arr)

    for _ in range(q):
        _query = input_as_array()
        if len(_query) == 1:
            ctr[0] += 1
            print(len(ctr) - 1)
        else:
            t, p, v  = _query 
            current  = arr[p-1]
            ctr[current] -= 1
            if ctr[current] == 0:
                del ctr[current]
            arr[p-1] = v
            ctr[v] += 1
            

if __name__ == "__main__":
    ONLINE_JUDGE = True

    # If it's Local - Get I/P from file
    if not ONLINE_JUDGE:
        sys.stdin = open("data.in", "r")
        sys.stdout = open("data.out", "w")

    testcases = int(input())
    for i in range(testcases):
        main()

    # If it's local - Print this O/P
    if not ONLINE_JUDGE:
        print(f"Time Elapsed: {time.time() - start_time} seconds")
        sys.stdout.close()
