# -*- coding: utf-8 -*-
# @Author: hariharanragothaman
# @Date:   2022-03-24 15:51:25
# @Last Modified by:   hariharanragothaman
# @Last Modified time: 2022-03-24 15:57:18

import os, sys, math, cmath, time, collections
from collections import deque, Counter, OrderedDict, defaultdict
from heapq import nsmallest, nlargest, heapify, heappop, heappush, heapreplace
from math import ceil, floor, log, log2, sqrt, gcd, factorial, pow, pi
from bisect import bisect_left, bisect_right

# SOME GENERAL HELPER
def input_as_array(): return list(map(int, input().split()))

start_time = time.time()


def main():
    n, q = input_as_array()
    i = 0
    ctr = Counter()
    while i < q:
        op, x = input_as_array()
        if op == 1:
            ctr[x] += 1
        else:
            print(ctr[x])
        i += 1



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
