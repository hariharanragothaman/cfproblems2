# -*- coding: utf-8 -*-
# @Author: hariharanragothaman
# @Date:   2022-03-23 20:51:08
# @Last Modified by:   hariharanragothaman
# @Last Modified time: 2022-03-23 21:00:10

import os, sys, math, cmath, time, collections
from collections import deque, Counter, OrderedDict, defaultdict
from heapq import nsmallest, nlargest, heapify, heappop, heappush, heapreplace
from math import ceil, floor, log, log2, sqrt, gcd, factorial, pow, pi
from bisect import bisect_left, bisect_right

# SOME GENERAL HELPER
def input_as_array(): return list(map(int, input().split()))

start_time = time.time()


def main():
	n = int(input())
	A = input_as_array()
	B = sorted(A, reverse=True)
	mx, mx_next = B[0], B[1]
	print(mx + mx_next)

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
