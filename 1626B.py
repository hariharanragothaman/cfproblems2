import sys, math, cmath, time, collections
from collections import deque, Counter, OrderedDict, defaultdict
from heapq import nsmallest, nlargest, heapify, heappop, heappush, heapreplace
from math import ceil, floor, log, log2, sqrt, gcd, factorial, pow, pi
from bisect import bisect_left, bisect_right

# SOME GENERAL HELPER
def input_as_array(): return list(map(int, input().split()))

start_time = time.time()


def main():
    level  = int(input())
    spawn = input_as_array()
    health = input_as_array()
    mx = max(spawn)
    PS = [0] * (mx+1)
    hmap = dict(zip(spawn, health))
    print("The dict is:", hmap)
    print("The spwan time is:", spawn)
    print("The health is:", health)
    for i in range(len(PS)):
        PS[i] = hmap.get(i, 0)
    print("PS is:", PS)

    # Monotonic increasing
    # Change PS to monotonically increasing

    prev = PS[1]
    for i in range(2, len(PS)):
        if prev > PS[i]:
            PS[i] = prev
            prev = PS[i]

    print("The updated PS is:", PS)

    print("*******************")


if __name__ == "__main__":
    LOCAL = True

    # If it's Local - Get I/P from file
    if LOCAL:
        sys.stdin = open("../io/data.in", "r")
        sys.stdout = open("../io/data.out", "w")

    testcases = int(input())
    for i in range(testcases):
        main()

    # If it's local - Print this O/P
    if LOCAL:
        print(f"Time Elapsed: {time.time() - start_time} seconds")
        sys.stdout.close()
