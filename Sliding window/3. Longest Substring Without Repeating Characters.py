#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        string_dict = {}
        res_string = ''
        max_len = 1
        
        if s == ' ':
            return 1
        
        if s == '':
            return 0
        
        for i, ch in enumerate(s):
            found = res_string.find(ch)
            if found == -1:
                res_string += ch
            else:
                max_len = max(max_len, len(res_string))
                res_string = res_string[found+1:] + ch
        
        max_len = max(max_len, len(res_string))       
        return max_len
        
#s = 'abcabcbb'
#s = 'bbbbb'
#s = "pwwkew"
#s = 'b'
s = 'au'
sol = Solution()



print(sol.lengthOfLongestSubstring(s))