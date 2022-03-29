# -*- coding: utf-8 -*-
# @Author: Hariharan Ragothaman
# @Date:   2022-03-27 10:37:57
# @Last Modified by:   Hariharan Ragothaman
# @Last Modified time: 2022-03-27 10:56:39

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
	s = input()
	# female = 1, male = 0
	cnt = 0
	for left in range(n):
		for right in range(left, n):
			substring = s[left : right + 1]
			ctr = Counter(substring)
			if ctr['0'] > ctr['1']:
				print("The substring is:", substring, left)
				diff = ctr['0'] - ctr['1']
				print("The diff is:", diff)
				cnt += diff
				s = s[:left] + s[left:right+1] + ("1" * diff) + s[right+1:]
			else:
				continue
			print("updated value of s is:", s)
			print("The cnt is:", cnt)
		print("-----------------------------")
	print("*************************")


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
