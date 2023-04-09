#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/search-in-rotated-sorted-array/

from IPython.core.debugger import set_trace

class Solution:
    
    def binary_search(self, arr, target):
        l = -1
        r = len(arr)
        while l != r - 1:
            m = (l + r) // 2
            if arr[m] < target:
                l = m
            elif arr[m] > target:
                r = m
            else:
                return m       
        return -1
    
    def search(self, nums, target: int) -> int:
       
       #Find the boundary element between parts of the array 
       l = -1
       r = len(nums) - 1
       
       set_trace()
       while l != r - 1:
           m = (l + r) // 2
           if nums[m] < nums[len(nums) - 1]:
               r = m
           else:
               l = m
       
       if l == -1:
           # array was not rotated
           bound_el = len(nums) - 1
       else:
           bound_el = l

       # binary search on both parts of the array
       res_left = self.binary_search(nums[:bound_el+1], target)
       if bound_el != len(nums) - 1:
           res_right = self.binary_search(nums[bound_el+1:], target)
       else:
           res_right = None
    
       if res_left != -1:
           return res_left 
       elif res_right != None:
           if res_right != -1:
               return res_right + len(nums[:bound_el+1])
       return -1

class Solution_2:

    def binary_search(self, arr, target, start):
        l = -1
        r = len(arr)
        while l != r - 1:
            m = (l + r) // 2
            if arr[m] < target:
                l = m
            elif arr[m] > target:
                r = m
            else:
                return start + m       
        return -1

    def search(self, nums, target: int) -> int:

       # Find the boundary element between parts of the array 
       l = -1
       r = len(nums) - 1
       
       while l != r - 1:
           m = (l + r) // 2
           if nums[m] < nums[len(nums) - 1]:
               r = m
           else:
               l = m
       
       if l == -1:
           # array was not rotated
           bound_el = len(nums) - 1
       else:
           bound_el = l

       # binary search on both parts of the array
       res_left = self.binary_search(nums[:bound_el+1], target, 0)
       res_right = self.binary_search(nums[bound_el+1:], target, bound_el+1)

       if res_left != -1:
           return res_left 
       elif res_right != -1:
           return res_right
       else:
           return -1
       
    
def full_pipeline(nums, target):
    sol = Solution()
    
    res = sol.search(nums, target)
    print(res)
    return res