#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from IPython.core.debugger import set_trace


from random import randint 

def swap(l1, i, j):
    tmp = l1[i]
    l1[i] = l1[j]
    l1[j] = tmp

class Solution:
    

    def countSort_old(self, nums):
        
        res = [0]*len(nums)
        
        min_el = min(nums)
        max_el = max(nums)
        
        if min_el < 0 or min_el > 0:
            shift = -1 * min_el            
        else:
            shift = 0
        
        counts = [0]*(max_el - min_el + 1) 
        
        for num in nums:
            counts[num + shift] += 1
        
        #set_trace()
        pos = 0
        for k in range(max_el - min_el + 1):       
            while counts[k] != 0:
                res[pos] = k - shift
                pos += 1
                counts[k] -= 1        
        return res
    
    def sortArray(self, nums):
        
        min_el = min(nums)
        max_el = max(nums)
        
        if min_el < 0 or min_el > 0:
            shift = -1 * min_el            
        else:
            shift = 0
        
        counts = [0]*(max_el - min_el + 1) 
        
        for num in nums:
            counts[num + shift] += 1
        
        cumsum = [sum(counts[0:i]) for i in range(1, len(counts)+1)]
        res = [0]*len(nums)
        for i in range(len(nums)-1, -1, -1):
            res[cumsum[nums[i] + shift] - 1] = nums[i]
            cumsum[nums[i] + shift] -= 1
        
        return res
    

def full_pipeline(l1):
    sol = Solution()
    
    #res = sol.sortArray(l1)
    res = sol.countSort_old(l1)
    print(res)
    return res
    
    

def test_quick_sort(sort_method):
    # Test empty list
    assert sort_method([]) == []

    # Test list with one element
    assert sort_method([1]) == [1]

    # Test list with two elements
    assert sort_method([2, 1]) == [1, 2]

    # Test list with three elements
    assert sort_method([3, 2, 1]) == [1, 2, 3]

    # Test list with repeated elements
    assert sort_method([5, 2, 8, 2, 5]) == [2, 2, 5, 5, 8]

    # Test list with negative numbers
    assert sort_method([-3, 0, 4, -1, 2]) == [-3, -1, 0, 2, 4]

    # Test list already sorted
    assert sort_method([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    # Test list in reverse order
    assert sort_method([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]    