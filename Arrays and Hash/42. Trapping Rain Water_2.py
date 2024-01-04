#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Solution:
                    
    def trap(self, height: list[int]) -> int:
        next_greater_right = Solution.max_right(height)
        next_greater_left = Solution.max_left(height)
    
        used_pairs = set()
    
        volume = 0
        for i in range(len(height)):
            if next_greater_right[i] == -1 or next_greater_left[i] == -1:
                continue
            else:
                if (next_greater_right[i], next_greater_left[i]) not in used_pairs: 
                    h_r = height[next_greater_right[i]]
                    h_l = height[next_greater_left[i]]
                    volume += (min(h_r, h_l) - height[i]) * (next_greater_right[i] - next_greater_left[i] - 1)
                    used_pairs.add((next_greater_right[i], next_greater_left[i]))
                
        return volume
        
    @staticmethod
    def max_right(arr):
        right_arr = [-1] * len(arr)
        my_stack = []
        
        if len(arr) == 1:
            return right_arr
        
        my_stack.append([0, arr[0]])
        for i in range(1, len(arr)):
            if my_stack and arr[i] < my_stack[-1][1]:
                my_stack.append([i, arr[i]])
            else:
                while my_stack and my_stack[-1][1] < arr[i]:
                    curr = my_stack.pop()
                    right_arr[curr[0]] = i
                my_stack.append([i, arr[i]])
                    
        return right_arr
    @staticmethod
    def max_left(arr):
        left_arr = [-1] * len(arr)
        arr_reverse = arr[::-1]
        answ = Solution.max_right(arr_reverse)
        
        answ = answ[::-1]
        answ = [len(answ) - el - 1 if el != -1 else -1 for el in answ ]
                    
        return answ

                

#height = [0,1,0,2,1,0,1,3,2,1,2,1]
#height = [4,2,0,3,2,5]
#height = [0, 2, 0]
#height = [4,9,4,5,3,2]
#height = [9,6,8,8,5,6,3]

sol = Solution()

print(sol.trap(height))

