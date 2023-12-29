#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from IPython.core.debugger import set_trace



import numpy as np

class Solution:
    def singleNumber(self, nums):
        
        #set_trace()
        my_set = set()
        for curr in nums:
            #nums.remove(curr)            
            if curr in my_set:
                my_set.remove(curr)
            else:
                my_set.add(curr)                
            
        el = next(iter(my_set))            
        return el
       
def pipeline(nums):
    
    sol = Solution()
    el = sol.singleNumber(nums)
    print(el)
    return el