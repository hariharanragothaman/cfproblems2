#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : 702B.py
# Author            : cppygod
# Date              : 10.02.2022
# Last Modified Date: 10.02.2022
# Last Modified By  : cppygod

import sys, math, cmath, time, collections
from collections import deque, Counter, OrderedDict, defaultdict
from heapq import nsmallest, nlargest, heapify, heappop, heappush, heapreplace
from math import ceil, floor, log, log2, sqrt, gcd, factorial, pow, pi
from bisect import bisect_left, bisect_right

# SOME GENERAL HELPER
def input_as_array(): return list(map(int, input().split()))

start_time = time.time()


def main():
    n = int(input())
    arr = input_as_array()
    P = [1 << c for c in range(1, 31)]


    """
    As you are going, keep collecting
    Instead of collecting everything at the beginning, if order is important.
    Here the ordering is i < j
    So we are collecting from the left.
    """
    hashmap = dict()
    cnt = 0
    for num in arr:
        for power in P:
            cnt += hashmap.get(power - num, 0)
        hashmap[num] = hashmap.get(num, 0) + 1;
    
    print(cnt)

if __name__ == "__main__":
    ONLINE_JUDGE = True

    # If it's Local - Get I/P from file
    if not ONLINE_JUDGE:
        sys.stdin = open("data.in", "r")
        sys.stdout = open("data.out", "w")

    testcases = 1
    for i in range(testcases):
        main()

    # If it's local - Print this O/P
    if not ONLINE_JUDGE:
        print(f"Time Elapsed: {time.time() - start_time} seconds")
        sys.stdout.close()
