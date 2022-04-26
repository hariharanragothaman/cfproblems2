#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : 1650A.py
# Author            : cppygod
# Date              : 11.02.2022
# Last Modified Date: 08.03.2022
# Last Modified By  : cppygod

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
    char = input()
    n = len(s)

    idx = []
    for i, c in enumerate(s, 1):
        if c == char:
            idx.append(i)

    for _id in idx:
        after = n - _id 
        before = n - after - 1
        if after % 2 == 0 and before % 2 == 0:
            print("YES")
            return 

    if char not in s:
        print("NO")
        return 
    elif char == s[0] or char == s[-1]:
        print("YES")
        return 

    print("NO")


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
