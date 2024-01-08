#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter_s1 = Counter(s1)
        curr_counter = Counter()
        
        if len(s2) == 1:
            if s1 == s2:
                return True
            else:
                False
        
        begin = 0
        end = 0
        
        while end != len(s2):
            if s2[end] in counter_s1:
                if curr_counter[s2[end]] < counter_s1[s2[end]]:
                    curr_counter[s2[end]] += 1
                    if curr_counter == counter_s1:
                        return True
                    end += 1
                else:
                   curr_counter[s2[begin]] -= 1
                   begin += 1
            else:
                if curr_counter: 
                    curr_counter = Counter()
                begin = end + 1
                end = end + 1
        
        if curr_counter == counter_s1:
            return True 
        else:
            return False
                    

#s1 = "ab"
#s2 = "eidbaooo"

s1 = "ab"
s2 = "eidboaoo"

sol = Solution()


print(sol.checkInclusion(s1, s2))