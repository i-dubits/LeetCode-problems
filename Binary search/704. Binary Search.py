#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from IPython.core.debugger import set_trace

class SolutionOld:
    def search(self, nums, target) -> int:
        
        
        #set_trace()
        guess_ind = len(nums)//2
        guess = nums[guess_ind]
        
        up = len(nums) - 1
        low = 0
        
        while(1):
            if guess == target:
                return guess_ind
            
            if guess > target:
                if guess_ind != 0 and guess_ind != len(nums) - 1:
                    guess_ind = guess_ind // 2
                    guess = nums[guess_ind]
                else:
                    return -1
                           
            elif guess < target:
                if guess_ind != 0 and guess_ind != len(nums) - 1:
                    guess_ind = guess_ind + (len(nums) - guess_ind) // 2
                    guess = nums[guess_ind]
                else:
                    return -1

class Solution:
    def search(self, nums, target) -> int:
        
        guess_ind = len(nums)//2 - 1 if len(nums)%2 == 0 else len(nums)//2
        guess = nums[guess_ind]
        
        upi = len(nums) - 1
        lowi = 0
        
        #set_trace()
        while(1):
            
            if guess == target:
                return guess_ind
            
            if guess > target:
                
                if upi != lowi and upi != lowi + 1:
                    upi = guess_ind
                    guess_ind = (upi - lowi) // 2
                    guess = nums[guess_ind]
                elif upi == lowi + 1:
                    lowi = upi
                    guess_ind = upi
                    guess = nums[guess_ind]
                elif upi == lowi:
                    return -1
                           
            elif guess < target:
                if upi != lowi and upi != lowi + 1:
                    lowi = guess_ind
                    guess_ind = lowi + (upi - lowi) // 2
                    guess = nums[guess_ind]
                elif upi == lowi + 1:
                    lowi = upi
                    guess_ind = upi
                    guess = nums[guess_ind]
                elif upi == lowi:
                    return -1

            
def test_sol(nums, target):
    sol = Solution()
    res = sol.search(nums, target)
    
    return res