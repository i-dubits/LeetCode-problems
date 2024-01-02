#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
     
    def check_seq(self, number):
        local_counter = 1
        curr_number = number
        
        while curr_number - 1 in self.nums_dict and self.nums_dict[curr_number - 1] == False:
            curr_number -= 1
            local_counter += 1
            self.nums_dict[curr_number] = True
            
        curr_number = number
        while curr_number + 1 in self.nums_dict and self.nums_dict[curr_number + 1] == False:
            curr_number += 1
            local_counter += 1
            self.nums_dict[curr_number] = True
            
        return local_counter    
    
    def longestConsecutive(self, nums: list[int]) -> int:
        
        if len(nums) == 0:
            return 0
        
        self.nums_dict = {num:False for num in nums}
        counter = 1
        
        for num in nums:
            local_counter = self.check_seq(num)
            counter = max(counter, local_counter)
        
        return counter
            
#nums = [4, 3, 2, 1]          
#nums = [100,4,200,1,3,2]
#nums = [0,3,7,2,5,8,4,6,0,1]
#nums = [0]
nums = [9,1,4,7,3,-1,0,5,8,-1,6]
sol = Solution()

print(sol.longestConsecutive(nums))

