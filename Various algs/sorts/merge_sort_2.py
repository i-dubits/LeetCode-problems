#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from IPython.core.debugger import set_trace


from random import randint 

def swap(l1, i, j):
    tmp = l1[i]
    l1[i] = l1[j]
    l1[j] = tmp


def merge(arr1, arr2):
    i = 0
    j = 0
    k = 0
    
    res = [0]*(len(arr1) + len(arr2))
    
    while i < len(arr1) or j < len(arr2):
        
        if i == len(arr1) and j < len(arr2):
            res[k] = arr2[j]
            j+=1
            k+=1
            continue
            
        if i < len(arr1) and j == len(arr2):
            res[k] =  arr1[i]
            i+=1
            k+=1
            continue
        
        if arr1[i] < arr2[j]:
            res[k] = arr1[i]
            i+=1
            k+=1
        else:
            res[k] = arr2[j]
            j+=1
            k+=1
            
    return res
        
    
class Solution:
    
    def __init__(self):
        self.nums = []
    
    def sortArray(self, nums):
        
        self.nums = nums
        
        res = self.merge_sort(nums)
        return res
    
    def merge_sort(self, arr):
        if len(arr) <= 1:
            return arr
        
        mid = (len(arr)-1) // 2
        
        arr1 = self.merge_sort(arr[0: mid+1])
        arr2 = self.merge_sort(arr[mid+1: len(arr)])
        res = merge(arr1, arr2)
        
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