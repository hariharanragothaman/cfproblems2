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
from itertools import permutations, combinations

# SOME GENERAL HELPER
def input_as_array():
    return list(map(int, input().split()))


start_time = time.time()


def main():
    n = int(input())
    A = input_as_array()

    cnt = 0
    ans = []
    stack = [A[0]]
    # To find the nearest greater element previous to it.
    for i in range(1, n):
        tmp = []
        while stack and stack[-1] < A[i]:
            stack.pop()
        if stack:
            ans.append(stack[-1])
        else:
            ans.append(-1)
            stack.append(A[i])
    for a, b in zip(A[1:], ans):
        if b != -1:
            cnt += abs(a - b)
    print(cnt)


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
