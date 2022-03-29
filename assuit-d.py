#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : assuit-d.py
# Author            : cppygod
# Date              : 25.03.2022
# Last Modified Date: 25.03.2022
# Last Modified By  : cppygod
# -*- coding: utf-8 -*-
# @Author: hariharanragothaman
# @Date:   2022-03-25 00:17:01
# @Last Modified by:   hariharanragothaman
# @Last Modified time: 2022-03-25 01:31:07

import os, sys, math, cmath, time, collections
from collections import deque, Counter, OrderedDict, defaultdict
from heapq import nsmallest, nlargest, heapify, heappop, heappush, heapreplace
from math import ceil, floor, log, log2, sqrt, gcd, factorial, pow, pi
from bisect import bisect_left, bisect_right

# SOME GENERAL HELPER
def input_as_array(): return list(map(int, input().split()))

start_time = time.time()


def solve(n, ans):
    if n == 0:
        ans = ans[::-1]
        print(*ans)
        return
    else:
        ans.append(str(n%10))
        n = n // 10
        solve(n, ans)

def main():
    n = int(input())
    if n == 0:
        print('0')
    else:
        solve(n, ans=[])

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
