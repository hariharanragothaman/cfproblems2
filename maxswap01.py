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
p = 31
m = 10 ** 9 + 9
def compute_hash(s):
    n = len(s)

    power_mod = [1]
    for i in range(n):
        power_mod.append((power_mod[-1] * p) % m)

    hash_values = [0] * (n + 1)

    for i in range(n):
        hash_values[i + 1] = (
            hash_values[i] + (ord(s[i]) - ord("a") + 1) * power_mod[i]
        ) % m

    return hash_values


def count_occurences(text, pattern):
    """
    :param pattern: Pattern Text
    :param text: I/P text
    :return:
    """
    text_length = len(text)
    pattern_length = len(pattern)

    power_mod = [1]
    for i in range(text_length):
        power_mod.append((power_mod[-1] * p) % m)
    # print(f"The power mod is: {[power_mod]}")

    hash_values = [0] * (text_length + 1)

    for i in range(text_length):
        hash_values[i + 1] = (
            hash_values[i] + (ord(text[i]) - ord("a") + 1) * power_mod[i]
        ) % m
    # print("The string hash values are:", hash_values)

    pattern_hash = 0
    for i in range(pattern_length):
        pattern_hash += ((ord(pattern[i]) - ord("a") + 1) * power_mod[i]) % m
    # print("The pattern hash is:", pattern_hash)

    occurences = []

    i = 0
    while i + pattern_length - 1 < text_length:
        field_hash = (hash_values[i + pattern_length] - hash_values[i] + m) % m
        if field_hash == pattern_hash * power_mod[i] % m:
            occurences.append(i)
        i += 1

    return len(occurences)


def main():
    n = int(input())
    s = input()

    even_map = defaultdict(int)
    odd_map = defaultdict(int)

    for i, c in enumerate(s):
        if i % 2 == 0:
            even_map[c] += 1
        elif i % 2 != 0:
            odd_map[c] += 1
    # print("The even map is:",even_map)
    # print("The odd map is:", odd_map)

    ans = ""
    switch = False
    for i in range(n):
        if i % 2 == 0:
            if switch == False:   
                if even_map['0'] > 0:
                    ans += '0'
                    even_map['0'] -= 1
                    switch = False
                else:
                    ans += '1'
                    switch = True
            else:
                if even_map['1'] > 0:
                    ans += '1'
                    even_map['1'] -= 1
                else:
                    ans += '0'

        elif i % 2 != 0:
            if switch == False:
                if odd_map['1'] > 0:
                    ans += '1'
                    odd_map['1'] -= 1
                    switch = False
                else:
                    ans += '0'
                    switch = True
            elif switch == True:
                if odd_map['0'] > 0:
                    ans += '0'
                    odd_map['0'] -= 1
                else:
                    ans += '1'

    op = count_occurences(ans, "01")
    print(op)
    # print("******************")

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
