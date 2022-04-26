# -*- coding: utf-8 -*-
# @Author: hariharanragothaman
# @Date:   2022-03-25 16:06:24
# @Last Modified by:   hariharanragothaman
# @Last Modified time: 2022-03-25 16:11:48

import os, sys, math, cmath, time, collections
from collections import deque, Counter, OrderedDict, defaultdict
from heapq import nsmallest, nlargest, heapify, heappop, heappush, heapreplace
from math import ceil, floor, log, log2, sqrt, gcd, factorial, pow, pi
from bisect import bisect_left, bisect_right

# SOME GENERAL HELPER
def input_as_array():
    return list(map(int, input().split()))


start_time = time.time()


def main():
    x1, x2, x3 = input_as_array()

    # Ensure x2 is always lesser than x3
    if x2 > x3:
        x2, x3 = x3, x2

    # all of them are between 1 and 10^5
    # So by this point x2 is always lesser than x3
    # x1 is where Perfect lives.

    dist = 0

    if x1 < x2 or x1 > x3:
        dist = abs(x2 - x1) + abs(x3 - x2) + abs(x3 - x1)
    elif x1 >= x2:
        dist = 2 * (abs(x1 - x2) + abs(x1 - x3))
    print(dist)


if __name__ == "__main__":
    if os.path.exists("data.in"):
        sys.stdin = open("data.in", "r")
        sys.stdout = open("data.out", "w")

    testcases = 1
    for i in range(testcases):
        main()

    # If it's local - Print this O/P
    if os.path.exists("data.in"):
        print(f"Time Elapsed: {time.time() - start_time} seconds")
        sys.stdout.close()
