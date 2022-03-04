#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : 584A.py
# Author            : cppygod
# Date              : 23.01.2022
# Last Modified Date: 03.03.2022
# Last Modified By  : cppygod

import os, sys, math, cmath, time, collections
from collections import deque, Counter, OrderedDict, defaultdict
from heapq import nsmallest, nlargest, heapify, heappop, heappush, heapreplace
from math import ceil, floor, log, log2, sqrt, gcd, factorial, pow, pi
from bisect import bisect_left, bisect_right
from io import BytesIO, IOBase
from functools import reduce


start_time = time.time()


def main():
    n, t = list(map(int, input().split()))


if __name__ == "__main__":
    LOCAL = False

    # If it's Local - Get I/P from file
    if LOCAL:
        sys.stdin = open("data.in", "r")
        sys.stdout = open("data.out", "w")

    testcases = int(input())
    for i in range(testcases):
        main()

    # If it's local - Print this O/P
    if LOCAL:
        print(f"Time Elapsed: {time.time() - start_time} seconds")
