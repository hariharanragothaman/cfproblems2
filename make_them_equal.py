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
    # Minimum number of ops to make array gooda
    hmap = {"odd": 0, "even": 0}
    for c in A:
        if c & 1:
            hmap["odd"] += 1
        else:
            hmap["even"] += 1

    if hmap["odd"] == 0 or hmap["even"] == 0:
        print(0)
        return
    elif hmap["even"] >= hmap["odd"]:
        # make all odd numbers -> even
        if hmap["odd"] % 2 == 0:
            ans = hmap["odd"] // 2
            print(ans)
            return
        else:
            print(hmap["even"])
            return

    elif hmap["odd"] > hmap["even"]:
        # Make all even numbers -> odd
        # Again check if odd cnt is even or not
        if hmap["odd"] % 2 == 0:
            print(min(hmap["odd"] // 2, hmap["even"]))
            return
        else:
            print(hmap["even"])
            return


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
