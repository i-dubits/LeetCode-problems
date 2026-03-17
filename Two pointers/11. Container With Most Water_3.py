#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/container-with-most-water/

from IPython.core.debugger import set_trace

def vol(k):
    vol_max = 0
    #set_trace()
    for i in range(k-1, -1, -1):
        vol_curr = (k - i) * min(height[i], height[k])
        vol_max = vol_curr if vol_curr > vol_max else vol_max
    return vol_max

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
#height = [2,3,10,5,7,8,9]


dp = [0]*len(height)

for i in range(1, len(height)):
    dp[i] = max(dp[i-1], vol(i))
    
print(dp[len(height)-1])

