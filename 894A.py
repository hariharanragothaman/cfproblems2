#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : 894A.py
# Author            : cppygod
# Date              : 10.02.2022
# Last Modified Date: 11.02.2022
# Last Modified By  : cppygod

import sys, math, cmath, time, collections
from collections import deque, Counter, OrderedDict, defaultdict
from heapq import nsmallest, nlargest, heapify, heappop, heappush, heapreplace
from math import ceil, floor, log, log2, sqrt, gcd, factorial, pow, pi
from bisect import bisect_left, bisect_right
from itertools import chain, permutations, combinations

# SOME GENERAL HELPER
def input_as_array(): return list(map(int, input().split()))

start_time = time.time()

def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(0, 4))

def main():
    s = input()
    string = "QAQ"
    """
    Find how many subsequences of QAQ are there
    """
    cnt = 0
    for c in powerset(s):
        if c == ('Q', 'A', 'Q'):
            cnt += 1
    print(cnt)



if __name__ == "__main__":
    ONLINE_JUDGE = True

    # If it's Local - Get I/P from file
    if not ONLINE_JUDGE:
        sys.stdin = open("data.in", "r")
        sys.stdout = open("data.out", "w")

    testcases = 1
    for i in range(testcases):
        main()

    # If it's local - Print this O/P
    if not ONLINE_JUDGE:
        print(f"Time Elapsed: {time.time() - start_time} seconds")
        sys.stdout.close()
