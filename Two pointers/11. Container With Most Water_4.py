#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/container-with-most-water/
    
#height = [1,8,6,2,5,4,8,3,7]
#height = [1,1]
#height = [1,2]
#height = [1,2,4,3]
height = [2,3,10,5,7,8,9]

first = 0
second = len(height) - 1

vol_max = 0
vol_curr = 0

while first != second:
    vol_curr = (second - first)*min(height[first], height[second])
    if vol_curr > vol_max:
        vol_max = vol_curr
        
    if height[first] <= height[second]:
        first += 1
    else:
        second -= 1
        
print(vol_max)
        
        
        
        

