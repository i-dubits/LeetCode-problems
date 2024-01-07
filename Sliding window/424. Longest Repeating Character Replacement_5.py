#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import deque
from collections import Counter

# https://www.youtube.com/watch?v=gqXU1UyA8pk

class Solution:
    
    def characterReplacement(self, s: str, k: int) -> int:
        
        if len(s) == 1:
            return 1
        
        length = min(len(s), k + 1)
        begin = 0
        end = 1
        
        subst_numb = 0
        subst_counter = Counter()
        
        subst_counter[s[begin]] += 1
        i = 0
        while end != len(s):
            subst_counter[s[end]] += 1
            if end - begin + 1 - subst_counter.most_common(1)[0][1] <= k:
                length = max(length, end - begin + 1)
                end += 1
            else:
                while end - begin + 1 - subst_counter.most_common(1)[0][1] > k and begin <= end:
                    subst_counter[s[begin]] -= 1
                    begin += 1
                length = max(length, end - begin + 1)
                end += 1
                
        return length
                    

#s = "abkfkc"
#k = 1

#s = "ddadd"
#k = 1

#s = "ABAB"
#k = 2

#s = "AAAA"
#k = 0

#s = 'SCDCSONAJN'
#k = 4

s = 'KRSCDCSONAJNHLBMDQGIFCPEKPOHQIHLTDIQGEKLRLCQNBOHNDQGHJPNDQPERNFSSSRDEQLFPCCCARFMDLHADJADAGNNSBNCJQOF'
k = 4

#s = "AABABBA"
#k = 1

sol = Solution()

#print(Solution.right_equal(s))

print(sol.characterReplacement(s, k))