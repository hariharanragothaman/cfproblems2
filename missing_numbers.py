# -*- coding: utf-8 -*-
# @Author: hariharanragothaman
# @Date:   2022-03-25 16:49:22
# @Last Modified by:   hariharanragothaman
# @Last Modified time: 2022-03-25 18:41:41

import os, sys, math, cmath, time, collections
from collections import deque, Counter, OrderedDict, defaultdict
from heapq import nsmallest, nlargest, heapify, heappop, heappush, heapreplace
from math import ceil, floor, log, log2, sqrt, gcd, factorial, pow, pi
from bisect import bisect_left, bisect_right
from functools import reduce

# SOME GENERAL HELPER

def factors(n):
    return set(
        reduce(
            list.__add__,
            ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0),
        )
    )

def input_as_array(): return list(map(int, input().split()))

start_time = time.time()


def main():
	x1, x2, x3, x4 = input_as_array()
	A = [x1, x2, x3, x4]
	absA = sorted(abs(c) for c in A)
	div, mul = absA[0], absA[-1]

	negflag = False
	if div not in A or mul not in A:
		negflag = True

	# print("The neg flag is:", negflag)
	# print("The absolute values are:", absA)
	# print("The values are:", add, sub, mul, div)
	# Getting the various candidates
	ff = factors(mul)
	# print("The factors are:",ff)

	if not negflag:
		for facts in ff:
			a, b  = facts, mul // facts
			candidate1 = [(a+b), (a-b), (a//b), (a*b)]
			candidate2 = [(a+b), (b-a), (b//a), (a*b)]
			# print(candidate2)
			# print(candidate1)
			if Counter(A) == Counter(candidate1):
				print(a, b)
				# print("The values are", a, b)
				return
			elif Counter(A) == Counter(candidate2):
				print(b, a)
				# print("The values are", b, a)
	else:
		# Then a or b is -ve then figuring out the possiblities
		# Atmost only one value is negative.
		for facts in ff:
			a, b = facts, mul // facts
			if a < b:
				a, b = b, a
			b = b * -1
			candidate = [a+b, a-b, (a//b), (a*b)]
			if Counter(candidate) == Counter(A):
				print(a, b)
				# print("The values are", a, b)
				return
		pass
	print(-1, -1)
	return


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
