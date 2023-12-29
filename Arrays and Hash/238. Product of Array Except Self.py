#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        self.prefix_left = [None] * len(nums)
        self.prefix_right = [None] * len(nums)
        
        self.prefix_left[0] = nums[0]
        self.prefix_right[0] = nums[-1]
        for i, k in zip(range(1, len(nums)), range(len(nums) - 2, -1, -1)):
            self.prefix_left[i] = self.prefix_left[i - 1] * nums[i]
            self.prefix_right[i] = self.prefix_right[i - 1] * nums[k]
         
        res = [None] * len(nums)
        res[0] = self.prefix_right[len(nums) - 1 - 1]
        res[len(nums) - 1] = self.prefix_left[len(nums) - 2]
        k = len(nums) - 1 - 2
        for i in range(1, len(nums) - 1):
            res[i] = self.prefix_left[i - 1] * self.prefix_right[k]
            k -= 1
            
        return res
    
class SolutionO1MemoryComplexity:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        
        res = [None] * len(nums)
        res[0] = 1
        res[1] = nums[0]
        for i in range(2, len(nums)):
            res[i] = res[i-1] * nums[i - 1]
        
        prod = nums[-1]
        for k in range(len(nums) - 2, -1, -1):
            res[k] *= prod
            prod *= nums[k]
            
        return res
        
#nums = [1,2,3,4]
nums = [-1,1,0,-3,3]
sol = SolutionO1MemoryComplexity()

print(sol.productExceptSelf(nums))

