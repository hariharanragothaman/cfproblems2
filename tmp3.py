#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : tmp3.py
# Author            : cppygod
# Date              : 28.01.2022
# Last Modified Date: 10.03.2022
# Last Modified By  : cppygod

import time
start_time = time.time()

def solve(A):
    ans = [item["object"][-1] for item in A]
    return ans 

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
