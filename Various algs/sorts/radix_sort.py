#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from IPython.core.debugger import set_trace


class Solution:
    
    def countSort(self, nums, digit):
        
        digits_arr = [self.idigit(num, digit) for num in nums]
        res = [0]*len(nums)
        
        min_el = min(digits_arr)
        max_el = max(digits_arr)
        
        if min_el < 0 or min_el > 0:
            shift = -1 * min_el            
        else:
            shift = 0
        
        counts = [0]*(max_el - min_el + 1)
        for i, num in enumerate(nums):
            counts[digits_arr[i] + shift] += 1
        
        cumsum = [sum(counts[0:i]) for i in range(1, len(counts)+1)]
        res = [0]*len(nums)
        for i in range(len(nums)-1, -1, -1):
            
            res[cumsum[digits_arr[i] + shift] - 1] = nums[i]
            cumsum[digits_arr[i] + shift] -= 1
            
        
        return res 
    
    def idigit(self, numb, i):
        '''Return i-th digit of the numb from the end
        
        if i-th digit does not exist, return 0
        i starts with one'''
        
        for k in range(i):
            if k == i - 1:
                digit = numb % 10
                break
            else:
                numb = numb // 10
        
        return digit
    
    
    def sortArray(self, nums):
        
        
        
        neg_arr = []
        pos_arr = []
        for el in nums:
            if el < 0:
                neg_arr.append(el)
            else:
                pos_arr.append(el)
        
        if neg_arr != []:
            neg_arr = [-el for el in neg_arr] 
            for digit in range(1,6):
                neg_arr = self.countSort(neg_arr, digit)
            
            neg_arr.reverse()
            neg_arr = [-el for el in neg_arr]    

        if pos_arr != []:
            for digit in range(1,6):
                #set_trace()
                pos_arr = self.countSort(pos_arr, digit)    
    
        neg_arr.extend(pos_arr)
        return neg_arr

def full_pipeline(l1):
    sol = Solution()
    
    res = sol.sortArray(l1)
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