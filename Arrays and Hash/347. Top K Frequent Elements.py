#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import Counter

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
            self.cnt = Counter(nums)
            m_c = self.cnt.most_common(k)
            return [curr[0] for curr in m_c]
        
nums = [1]
k = 1
        
sol = Solution()
print(sol.topKFrequent(nums, k))
