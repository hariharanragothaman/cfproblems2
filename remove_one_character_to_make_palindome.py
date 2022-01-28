#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : remove_one_character_to_make_palindome.py
# Author            : cppygod
# Date              : 24.01.2022
# Last Modified Date: 24.01.2022
# Last Modified By  : cppygod


def is_palindrome(s):
    return s == s[::-1]

def make_palindrome_by_removing_one_char(s):
    n = len(s)
    low, high = 0, n-1

    while low < high:
        # We can compare matches
        if s[low] == s[high]:
            low += 1
            high -= 1

        else:
            # Remove low
            candidate = s[:low] + s[low+1:]
            print("The candidate after removing low is:", candidate)
            if is_palindrome(candidate):
                return low
            # Remove high
            candidate = s[:high] + s[high+1:]
            print("The candidate after removing high is:", candidate)
            if is_palindrome(candidate):
                return high
            
            return -1



s = input()
res = make_palindrome_by_removing_one_char(s)
if res == -1:
    print("Not possible")
else:
    print(res)
