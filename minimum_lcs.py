#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : 1650B.py
# Author            : cppygod
# Date              : 11.02.2022
# Last Modified Date: 11.03.2022
# Last Modified By  : cppygod

import os, sys, math, cmath, time, collections
from collections import deque, Counter, OrderedDict, defaultdict
from heapq import nsmallest, nlargest, heapify, heappop, heappush, heapreplace
from math import ceil, floor, log, log2, sqrt, gcd, factorial, pow, pi
from bisect import bisect_left, bisect_right

# SOME GENERAL HELPER
def input_as_array(): return list(map(int, input().split()))

start_time = time.time()

from difflib import SequenceMatcher


def find_length(A, B):
    if set(A).isdisjoint(B):
        return 0
    a, b, size = SequenceMatcher(None, A, B, autojunk=False).find_longest_match(
        0, len(A), 0, len(B)
    )
    return size

def main():
    """
    return S & T which are permutations of A
    such as LCS(S, T) is as minimum as possible.
    return the minimum length.
    """
    n = int(input())
    A = input()
    print("The I/P string is:", A)
    print(A)
    print("*********************")


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
