#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : tmp.py
# Author            : cppygod
# Date              : 28.01.2022
# Last Modified Date: 10.03.2022
# Last Modified By  : cppygod

import time
start_time = time.time()

def get_columns(matrice):
    return zip(*matrice)

def solve(A):
    matrix = []
    for _item in A:
        matrix.append(_item["object"])

    matrix = [c[::-1] for c in matrix]

    cnt = 0 
    for c in get_columns(matrix):
        return c

def main():
    """
    Just getting basic I/P
    """
    A = [
    {'label': 'a',
     'object': [1,2,3]
    },
    {'label': 'b',
     'object': [4,5,6]
    },
    {'label': 'c',
     'object': [7,8,9]
    },
    {'label': 'd',
     'object': [12,3]
    }
    ]
    ans = solve(A)
    print(*ans)

main()
print(f"Time Elapsed: {time.time() - start_time} seconds")
