#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : most_frequent_substring.py
# Author            : cppygod
# Date              : 24.01.2022
# Last Modified Date: 24.01.2022
# Last Modified By  : cppygod
# -*- coding: utf-8 -*-
# File              : most_frequent_substring.py
# Author            : cppygod
# Date              : 24.01.2022
# Last Modified By  : cppygod

from collections import defaultdict, Counter 

s = input()
low = int(input())
high = int(input())
unique = int(input())


def substr_efficient(s, low, high, unique):
    n = len(s)
    p = 53
    m = 10**9 + 9

    # Pre-computing the powers of 31
    power_mod = [1]
    for i in range(1, n):
        power_mod.append((power_mod[-1] * p) % m)

    # Do prefix-sum of hash-values
    hash_values = [0] * (n + 1)
    for i in range(n):
        hash_values[i + 1] = (hash_values[i] + (ord(s[i]) - ord("a") + 1) * power_mod[i]) % m

    def unique_char(ss):
        ctr = Counter(ss)
        if len(ctr) <= unique:
            return True
        return False

    hashmap = defaultdict(int)


    for length in range(low, high+1):
        for i in range(0, n - length + 1):
            string = s[i : i + length]
            print("The string is:", string)
            if unique_char(string):
                current_hash = (hash_values[i + length] + m - hash_values[i]) % m
                current_hash = (current_hash * power_mod[n - i - length]) % m
                hashmap[current_hash] += 1
    print(hashmap)





def substr(s, low, high, unique):
    h = defaultdict(int)
    n = len(s)
    for i in range(n):
        for j in range(i, n):
            substr = s[i:j+1]
            if low <= len(substr) <= high and len(set(substr)) <= unique:
                h[substr] += 1

    max_key = max(h, key = lambda k:h[k])
    print(h)
    print(max_key, h[max_key])



substr_efficient(s, low, high, unique)
