#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import Counter

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        self.cnt = Counter(nums)
        for el in self.cnt:
            if self.cnt[el] > 1:
                return True
        return False
            
nums = [1,1,1,3,3,4,3,2,4,2]
sol = Solution()
print(sol.containsDuplicate(nums))