#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/container-with-most-water/

from IPython.core.debugger import set_trace

def vol(k):
    higher = 100_000
    smaller = 100_000
    
    #set_trace()
    for i in range(k-1, -1, -1):
        if height[k] <= height[i]:
            higher = i
        else:
            smaller = i
            
    if higher < smaller:
        return height[k]*(k - higher)
    else:
        return height[smaller]*(k - smaller)

class Solution:
    def maxArea(self, height):
        dp = [0]*len(height)

        for i in range(1, len(height)):
            dp[i] = max(dp[i-1], vol(i))
            
        return dp[len(height)-1]
    
    
#height = [1,8,6,2,5,4,8,3,7]
#height = [1,1]
#height = [1,2]
height = [1,2,4,3]

dp = [0]*len(height)

for i in range(1, len(height)):
    dp[i] = max(dp[i-1], vol(i))
    
print(dp[len(height)-1])

