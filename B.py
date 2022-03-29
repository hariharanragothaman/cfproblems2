#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : B.py
# Author            : cppygod
# Date              : 28.01.2022
# Last Modified Date: 23.02.2022
# Last Modified By  : cppygod

import os
from io import BytesIO, IOBase
import sys, math, cmath, time, collections
from collections import deque, Counter, OrderedDict, defaultdict
from heapq import nsmallest, nlargest, heapify, heappop, heappush, heapreplace
from math import ceil, floor, log, log2, sqrt, gcd, factorial, pow, pi
from bisect import bisect_left, bisect_right
from itertools import permutations, combinations, combinations_with_replacement


# SOME GENERAL HELPER
def input_as_array(): return list(map(int, input().split()))

start_time = time.time()


def main():
    n = int(input())
    arr = input_as_array()
    ans = []
    ctr = Counter(arr)

    ctr = {k:v for k, v in sorted(ctr.items(), key=lambda x: x[1])}
    hmap = deque([])
    for k, v in ctr.items():
        hmap.append((k, v))

    print(hmap)
    sep = 0
    for i in range(1, n+1):
        if i == 1:
            ans.append(len(hmap))
        else:
            val, cnt = hmap.popleft()
            if cnt > 1:
                hmap.appendleft((val, cnt-1))
            
            sep += 1
            ans.append(len(hmap) + sep)
        print(hmap)
    print(*ans)
    print("*************")

if __name__ == "__main__":
    if os.path.exists('data.in'):
        sys.stdin = open("data.in", "r")
        sys.stdout = open("data.out", "w")

    testcases = int(input())
    for i in range(testcases):
        main()

    if os.path.exists('data.in'):
        print(f"Time Elapsed: {time.time() - start_time} seconds")
        sys.stdout.close()
