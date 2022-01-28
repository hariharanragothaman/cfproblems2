#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : p12.py
# Author            : cppygod
# Date              : 23.01.2022
# Last Modified Date: 23.01.2022
# Last Modified By  : cppygod


"""
2 1 3 4
1 2 3 4

3 1 2 4
1 2 3 4

3 2 1 4
1 2 3 4


"""
from collections import defaultdict


def solve(arr, sarr):
    g = defaultdict(int)
    if arr == sarr:
        print("yes")
        res = [1, 1]
        print(*res)

    else:
        for a, b in zip(arr, sarr):
            g[a] = b
        for k, v in g.items():
            if g[v] != k:
                print("no")
                return

        i = 1
        res = []
        for a, b in zip(arr, sarr):
            if a != b:
                res.append(i)
            i += 1
        p1 = res[0] - 1
        p2 = res[-1] - 1
        can = arr[:p1] + arr[p1:p2+1][::-1] + arr[p2+1:]
        if can == sarr:
            print("yes")
            print(res[0], res[-1])
        else:
            print("no")

n = int(input())
arr = list(map(int, input().split()))
sarr = sorted(arr)
solve(arr, sarr)
