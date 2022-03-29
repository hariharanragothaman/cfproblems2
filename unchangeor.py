# -*- coding: utf-8 -*-
# @Author: hariharanragothaman
# @Date:   2022-03-24 00:27:11
# @Last Modified by:   hariharanragothaman
# @Last Modified time: 2022-03-24 02:22:25

import os, sys, math, cmath, time, collections
from collections import deque, Counter, OrderedDict, defaultdict
from heapq import nsmallest, nlargest, heapify, heappop, heappush, heapreplace
from math import ceil, floor, log, log2, sqrt, gcd, factorial, pow, pi
from bisect import bisect_left, bisect_right

# SOME GENERAL HELPER
def input_as_array(): return list(map(int, input().split()))

start_time = time.time()


def main():
    N = int(input())

    """
    A = list(range(N+1))
    n = len(A)
    cnt = 0
    for i in range(1, n):
        A[i] = A[i] | A[i-1]
        if A[i] == A[i-1]:
            cnt += 1

    for i in range(n):
        print(i, A[i])
    print(cnt)
    print("*********************")
    """
    # till a new bit is introduced, we have the same value
    s = bin(N)[2:]
    n = len(s)
    print(N-len(s))

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
