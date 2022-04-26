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
    n = int(input())
    A = input_as_array()

    total = sum(A)

    if total & 1:
        print("NO")
        return

    target = sum(A) // 2
    ctr = Counter(A)

    for i in range(n):
        if A[i] > target:
            continue
        if target - A[i] == A[i]:
            if ctr[A[i]] > 1:
                print("YES")
                return
        else:
            if ctr[target - A[i]] != 0:
                print("YES")
                return
    print("NO")


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
