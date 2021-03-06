# -*- coding: utf-8 -*-
# @Author: hariharanragothaman
# @Date:   2022-03-27 01:16:13
# @Last Modified by:   hariharanragothaman
# @Last Modified time: 2022-04-11 14:44:45

import os, sys, math, cmath, time, collections
from collections import deque, Counter, OrderedDict, defaultdict
from heapq import nsmallest, nlargest, heapify, heappop, heappush, heapreplace
from math import ceil, floor, log, log2, sqrt, gcd, factorial, pow, pi
from bisect import bisect_left, bisect_right
from functools import reduce

# SOME GENERAL HELPER
def input_as_array(): return list(map(int, input().split()))

start_time = time.time()


def main():
    a, b = input_as_array()
    if min(a, b) <= 1:
        print(-1)
        return
    if gcd(a, b) > 1:
        print(0)
        return
    else:
        print(1)
        return

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
