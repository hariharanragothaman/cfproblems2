#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : 1644A.py
# Author            : cppygod
# Date              : 28.01.2022
# Last Modified Date: 22.02.2022
# Last Modified By  : cppygod
import sys, math, cmath, time, collections
from collections import deque, Counter, OrderedDict, defaultdict
from heapq import nsmallest, nlargest, heapify, heappop, heappush, heapreplace
from math import ceil, floor, log, log2, sqrt, gcd, factorial, pow, pi
from bisect import bisect_left, bisect_right

# SOME GENERAL HELPER
def input_as_array(): return list(map(int, input().split()))

start_time = time.time()


def main():
    ctr = Counter()
    s = input()
    def solve(s):
        for char in s:
            if char in "rgb":
                ctr[char] += 1
            elif char in "RGB":
                if ctr.get(char.lower(), 0) < 1:
                    return "NO"
                else:
                    continue
        return "YES"

    ans = solve(s)
    print(ans)

if __name__ == "__main__":
    LOCAL = False
    #LOCAL = True

    # If it's Local - Get I/P from file
    if LOCAL:
        sys.stdin = open("data.in", "r")
        sys.stdout = open("data.out", "w")

    testcases = int(input())
    for i in range(testcases):
        main()

    # If it's local - Print this O/P
    if LOCAL:
        print(f"Time Elapsed: {time.time() - start_time} seconds")
        sys.stdout.close()
