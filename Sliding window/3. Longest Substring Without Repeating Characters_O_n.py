#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        res_string = ''
        max_len = 0
        
        begin = 0
        
        for i, ch in enumerate(s):
            if ch not in char_set:
                char_set.add(ch)
                max_len = max(max_len, len(char_set))
            else:
                while ch in char_set:
                    char_set.remove(s[begin])
                    begin += 1
                char_set.add(ch)
                    
        max_len = max(max_len, len(char_set))
        return max_len
        
#s = 'abcabcbb'
#s = 'bbbbb'
#s = "pwwkew"
#s = 'b'
s = 'au'
sol = Solution()



print(sol.lengthOfLongestSubstring(s))