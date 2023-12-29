#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/valid-anagram/

from IPython.core.debugger import set_trace

from collections import defaultdict

class Solution:
    
    def isAnagram(self, s: str, t: str) -> bool:
        
        init_dict = defaultdict(int)
        for char in s:
            init_dict[char] += 1
        
        for char in t:
            if char not in init_dict:
                return 0
            else:
                init_dict[char] -= 1
        
        for _,v in init_dict.items():
            if v != 0:
                return 0
            
        return 1



def full_pipeline(s,t):
    sol = Solution()
    
    res = sol.isAnagram(s, t)
    print(res)
    