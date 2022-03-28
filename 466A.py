#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : 466A.py
# Author            : cppygod
# Date              : 28.01.2022
# Last Modified Date: 23.02.2022
# Last Modified By  : cppygod

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
    """
    To find the minimum sum that needs to be spent

        5 2 2 3
       
        1 ticket costs 2$
        2 tickets costs 3$
        I need to get 5 tickets 
        2 + 2 + 1
        3$ + 3$ + 2


        So - I split n rides into m segments.
        for each m segment -
                I can pay - special ticket cost flat (or) single ticket cost for each ticket.
        for remaining
             I can pay just buy another special ticket (or) single ticket cost for each ticket.
    """
    
    total_rides, m, one_ticket_cost, special_ticket_cost = input_as_array()
    q, r = divmod(total_rides , m)
    ans = (q * min(special_ticket_cost, m * one_ticket_cost)) + min((r * one_ticket_cost), special_ticket_cost)
    print(ans)

if __name__ == "__main__":
    if os.path.exists('data.in'):
        sys.stdin = open("data.in", "r")
        sys.stdout = open("data.out", "w")

    testcases = 1
    for i in range(testcases):
        main()

    if os.path.exists('data.in'):
        print(f"Time Elapsed: {time.time() - start_time} seconds")
        sys.stdout.close()
