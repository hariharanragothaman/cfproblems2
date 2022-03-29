# -*- coding: utf-8 -*-
# @Author: hariharanragothaman
# @Date:   2022-03-24 16:26:37
# @Last Modified by:   hariharanragothaman
# @Last Modified time: 2022-03-24 16:29:52

import os, sys, math, cmath, time, collections
from collections import deque, Counter, OrderedDict, defaultdict
from heapq import nsmallest, nlargest, heapify, heappop, heappush, heapreplace
from math import ceil, floor, log, log2, sqrt, gcd, factorial, pow, pi
from bisect import bisect_left, bisect_right

# SOME GENERAL HELPER
def input_as_array(): return list(map(int, input().split()))

start_time = time.time()

def solve(i, n):
	if i <= n:
		print(i)
		solve(i+1, n)
	else:
		return

def main():
    n = int(input())
    solve(1, n)


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
