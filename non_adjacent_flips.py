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
    s = input()
    ctr = Counter(s)
    if ctr["1"] == 0:
        print(0)
        return
    else:
        hmap = defaultdict(list)
        for i, val in enumerate(s):
            if val == "1":
                hmap[val].append(i)
        A = hmap["1"]
        # print("A is", A)

        # # Now to see minimum moves to collect the indices
        tmp = []
        tmp.append(A[0])
        q = deque(A[1:])
        # print("The q is:", q)
        # print("The tmp is:", tmp)
        # print("------------------------------")

        cnt = 0
        tmp2 = []
        while q:
            # print("Entering Q")
            # print("The q is:", q)
            node = q.popleft()
            # print("The node is:", node)
            if node - tmp[-1] > 1:
                tmp.append(node)
            elif node - tmp[-1] < 1:
                cnt += 1
                tmp = []
                tmp.append(node)
            else:
                q.append(node)

            # print("########################")
        print(cnt + 1)

    # print("**********")


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
