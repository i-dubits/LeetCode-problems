#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    
    def __init__(self):
        self.m = None
        self.n = None
    
    def indexMax(self, index):
        row = index // self.n
        column = index % self.n
        
        return row, column
        
    def searchMatrix(self, matrix, target):
        self.m = len(matrix)
        self.n = len(matrix[0])
       
        l = -1
        r = self.m * self.n
        
        while l != r - 1:
            m = (r + l) // 2
            curr_row, curr_column = self.indexMax(m)
            if matrix[curr_row][curr_column] < target:
                l = m
            elif matrix[curr_row][curr_column] > target:
                r = m
            elif matrix[curr_row][curr_column] == target:
                return True
            
        return False
        
    
def full_pipeline(matrix, target):
    sol = Solution()
    
    res = sol.searchMatrix(matrix, target)
    print(res)
    return res