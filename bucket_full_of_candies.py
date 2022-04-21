#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : bucket_full_of_candies.py
# Author            : cppygod
# Date              : 20.04.2022
# Last Modified Date: 20.04.2022
# Last Modified By  : cppygod

import os, sys, math, cmath, time, collections
from collections import deque, Counter, OrderedDict, defaultdict
from heapq import nsmallest, nlargest, heapify, heappop, heappush, heapreplace
from math import ceil, floor, log, log2, sqrt, gcd, factorial, pow, pi
from bisect import bisect_left, bisect_right
from functools import reduce

# SOME GENERAL HELPER
def input_as_array(): return list(map(int, input().split()))

def debug():
    if os.path.exists('data.in'):
        print("**********************")

def debug2(value):
    if os.path.exists('data.in'):
        print(value)

start_time = time.time()


def solve(n, m, l): 
    bucket_size = n + 1
    while n > 0:
         q, r = divmod(m, bucket_size)
         print("The q and r are", q, r)
         m = r
         n -= 1
         bucket_size -= 1
         debug2(m)


def main():
    n, m, l = input_as_array()
    solve(n, m, l)
    debug()


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
