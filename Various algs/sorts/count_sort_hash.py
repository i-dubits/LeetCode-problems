#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from IPython.core.debugger import set_trace


from random import randint 
from collections import Counter

def swap(l1, i, j):
    tmp = l1[i]
    l1[i] = l1[j]
    l1[j] = tmp

class Solution:
        
    def sortArray(self, nums):
        
        counts = {}
        
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1 
        
        min_el = min(nums)
        max_el = max(nums)
        
        res = []
        for i in range(min_el, max_el + 1):
            if i in counts:
                while counts[i] != 0:
                    res.append(i)
                    counts[i] -= 1
        return res
    

def full_pipeline(l1):
    sol = Solution()
    
    res = sol.sortArray(l1)
    print(res)
    
    

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