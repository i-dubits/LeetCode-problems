#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# https://leetcode.com/problems/merge-intervals/

from IPython.core.debugger import set_trace



class Solution:
    
    def key_func(self, my_list):
        return my_list[0]
    
    def merge(self, intervals):
        
        intervals = sorted(intervals, key = self.key_func)
        
        if len(intervals) in [0, 1]:
            return intervals
        
        ignore_index = []
        #set_trace()
        for i in range(1, len(intervals)):
            
            if intervals[i-1][1] < intervals[i][0]:
                continue
            else:
                if intervals[i-1][1] >= intervals[i][1]:
                    intervals[i][0] = intervals[i-1][0]
                    intervals[i][1] = intervals[i-1][1]
                    ignore_index.append(i-1)
                    
                    
                elif intervals[i-1][1] < intervals[i][1]:  
                    intervals[i][0] = intervals[i-1][0]
                    ignore_index.append(i-1)
        
        res = []
        for i in range(len(intervals)):
            if i not in ignore_index:
                res.append(intervals[i])

        return res
    
class Solution_2:
    
    def merge(self, intervals):
        
        intervals = sorted(intervals, key = lambda x: x[0])
        
        if len(intervals) in [0, 1]:
            return intervals
        
        merge_list = []
        curr_merge = []
        #set_trace()
        curr_merge = intervals[0]
        for i in range(1, len(intervals)):
            
            if curr_merge[1] < intervals[i][0]:
                merge_list.append(curr_merge)
                curr_merge = intervals[i]
            elif curr_merge[1] < intervals[i][1]:
                #set_trace()
                curr_merge[1] = intervals[i][1]
        
        merge_list.append(curr_merge)
        
        return merge_list

def full_pipeline(l1):
    sol = Solution_2()
    
    res = sol.merge(l1)
    print(res)
    return res
    
    
def test_sort(sort_method):
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