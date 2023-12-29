#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/find-all-anagrams-in-a-string/

from IPython.core.debugger import set_trace

from collections import defaultdict

class Solution:
    
    def findAnagrams(self, s: str, p: str):
        res = []
        
        dict_p = defaultdict(int)
        for char in p:
            dict_p[char] += 1
        
        dict_wind = defaultdict(int)
        if len(s) < len(p):
            return []
        wind = [s[i] for i in range(len(p))]
        for char in wind:
            dict_wind[char] += 1

        if dict_wind == dict_p:
            res.append(0)

        i = 1
        #set_trace()
        while i + len(p) <= len(s):
            
            dict_wind[s[i-1]] -= 1
            if dict_wind[s[i-1]] == 0:
                del dict_wind[s[i-1]]
            dict_wind[s[i+len(p)-1]] += 1
            
            if dict_wind == dict_p:
                res.append(i) 
            i+=1
            
        return res

def full_pipeline(s,p):
    sol = Solution()
    
    res = sol.findAnagrams(s, p)
    print(res)
    