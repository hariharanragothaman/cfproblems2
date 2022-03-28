#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : tmp2.py
# Author            : cppygod
# Date              : 10.03.2022
# Last Modified Date: 10.03.2022
# Last Modified By  : cppygod

import time 
from collections import defaultdict 

start_time = time.time()

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

g = defaultdict(list)

for it in A:
    g[it['label']] = it['object']

ans = []
for key, value in g.items():
    ans.append(value[-1])

print(ans)

print(f"Time Elapsed: {time.time() - start_time} seconds")
