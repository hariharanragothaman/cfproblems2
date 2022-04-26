# -*- coding: utf-8 -*-
# @Author: hariharanragothaman
# @Date:   2022-03-25 16:49:22
# @Last Modified by:   hariharanragothaman
# @Last Modified time: 2022-03-25 18:41:41

import os, sys, math, cmath, time, collections
from collections import deque, Counter, OrderedDict, defaultdict
from heapq import nsmallest, nlargest, heapify, heappop, heappush, heapreplace
from math import ceil, floor, log, log2, sqrt, gcd, factorial, pow, exp
from bisect import bisect_left, bisect_right
from functools import reduce

# SOME GENERAL HELPER

def input_as_array(): return list(map(int, input().split()))

start_time = time.time()


def main():
	n, x = input_as_array()
	A = input_as_array()
	cnt = 0
	print("The initial array is:", A)
	print("*****************")

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
