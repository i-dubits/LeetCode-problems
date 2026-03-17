#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/container-with-most-water/

from IPython.core.debugger import set_trace


    
#height = [1,8,6,2,5,4,8,3,7]
#height = [1,1]
#height = [1,2]
#height = [1,2,4,3]
height = [2,3,10,5,7,8,9]


i = 0
j = len(height) - 1

vol_i = 0
vol_j = 0
answ = 0

#set_trace()
vol = (j - i) * min(height[i], height[j])
while i < j:
    i+=1
    if i != j:
        vol_i = (j - i) * min(height[i], height[j])
    j-=1 
    if i != j:
        vol_j = (j - i) * min(height[i], height[j])

    if vol < vol_i:
        vol = vol_i
    if vol < vol_j:
        vol = vol_j

print(vol)