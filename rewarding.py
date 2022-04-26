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
    A = sorted(A, reverse=True)
    # print(A)

    i = 0
    j = n - 2

    sm_red = 0
    sm_blue = A[n - 1]
    red_cnt = 0
    blue_cnt = 1

    """
    cnt of blue should be greater than red
    sum of red must be greater than blue

    """
    while i < j:
        if sm_red > sm_blue and red_cnt < blue_cnt:
            print("YES")
            # print("**************")
            return
        sm_red += A[i]
        sm_blue += A[j]
        i += 1
        j -= 1
        red_cnt += 1
        blue_cnt += 1
        # print("Sum red:", sm_red, red_cnt)
        # print("Sum blue", sm_blue, blue_cnt)

    if sm_red > sm_blue and red_cnt < blue_cnt:
        print("YES")
        return
    else:
        print("NO")


if __name__ == "__main__":
    if os.path.exists("data.in"):
        sys.stdin = open("data.in", "r")
        sys.stdout = open("data.out", "w")

    testcases = int(input())
    for i in range(testcases):
        main()

    # If it's local - Print this O/P
    if os.path.exists("data.in"):
        print(f"Time Elapsed: {time.time() - start_time} seconds")
        sys.stdout.close()
