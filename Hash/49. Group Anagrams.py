#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/group-anagrams/description/

from IPython.core.debugger import set_trace

class Solution:
    
    def groupAnagrams(self, strs):

        res = []
        str_dict = {}
        for curr_str in strs:
            curr_str_sorted = ''.join(sorted(curr_str))
            
            if curr_str_sorted not in str_dict:
                str_dict[curr_str_sorted] = [curr_str]
            
            else:
                str_dict[curr_str_sorted].append(curr_str)
                
        for _,v in str_dict.items():
            res.append(v)
        
        return res



def full_pipeline(strs):
    sol = Solution()
    
    res = sol.groupAnagrams(strs)
    print(res)
    