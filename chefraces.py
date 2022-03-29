# -*- coding: utf-8 -*-
# @Author: hariharanragothaman
# @Date:   2022-03-25 16:16:57
# @Last Modified by:   hariharanragothaman
# @Last Modified time: 2022-03-25 16:19:10

import os, sys, math, cmath, time, collections
from collections import deque, Counter, OrderedDict, defaultdict
from heapq import nsmallest, nlargest, heapify, heappop, heappush, heapreplace
from math import ceil, floor, log, log2, sqrt, gcd, factorial, pow, pi
from bisect import bisect_left, bisect_right

# SOME GENERAL HELPER
def input_as_array(): return list(map(int, input().split()))

start_time = time.time()


def main():
	x, y, a, b = input_as_array()
	cnt = 0
	if x != a and x != b:
		cnt += 1
	if y != a and y != b:
		cnt += 1
	print(cnt)


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
