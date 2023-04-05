#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from IPython.core.debugger import set_trace

class Solution:
    def fourSum(self, nums, target):
        nums.sort()
        
        my_set = set()
        for p_1 in range(len(nums)):
            for p_2 in range(p_1+1, len(nums)):
                i = p_2 + 1
                j = len(nums) - 1
                
                if p_1 == 1:
                    #set_trace()
                    pass
                while i < j:
                    curr_sum = nums[p_1] + nums[p_2] + nums[i] + nums[j]
                    
                    if curr_sum == target:
                        my_set.add((nums[p_1], nums[p_2], nums[i], nums[j]))
                        i += 1
                        j-=1
                    
                    elif curr_sum > target:
                        j-=1
                    
                    elif curr_sum < target:
                        i += 1
                    
        return my_set
        
        
        
def full_pipeline(nums, target):
    
    sol = Solution()
    res = sol.fourSum(nums, target)
    print(res)
    return res

def common_elements(list1, list2):
    return [element for element in list1 if element in list2]