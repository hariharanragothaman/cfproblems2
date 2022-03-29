#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : 43B.py
# Author            : cppygod
# Date              : 24.03.2022
# Last Modified Date: 24.03.2022
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
    s1 = input()
    s2 = input()
    ctr1 = Counter(s1)
    ctr2 = Counter(s2)
    del ctr1[' ']
    del ctr2[' ']
    for k, v in ctr2.items():
            if ctr1[k] < v:
                    print("NO")
                    return
    print("YES")
    return


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
