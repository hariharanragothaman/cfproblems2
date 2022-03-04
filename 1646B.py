#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : B.py
# Author            : cppygod
# Date              : 11.02.2022
# Last Modified Date: 04.03.2022
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
    n = int(input())
    arr = input_as_array()
    arr = sorted(arr, reverse=True)
    # sum of red > sum of blue 
    # count of red < count of blue

    rcnt, bcnt = 0, n
    sr, sb = 0, sum(arr)

    for num in arr:
        if rcnt < bcnt and sr > sb:
            print("YES")
            return 
        
        sr += num 
        sb -= num 

        rcnt += 1
        bcnt -= 1

    print("NO")

if __name__ == "__main__":
    #LOCAL = False 
    LOCAL = True 
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
