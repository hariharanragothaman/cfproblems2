#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : 1382A.py
# Author            : cppygod
# Date              : 11.02.2022
# Last Modified Date: 05.03.2022
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
    n, m = input_as_array()
    A = input_as_array()
    B = input_as_array()
    # Find the smallest array that is a subsequence of A and B

    A = set(A)
    B = set(B)
    C = A.intersection(B)

    if len(C) > 0:
        print("YES")
        print(1, C.pop())
    else:
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
