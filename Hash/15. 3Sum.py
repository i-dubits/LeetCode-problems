#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from IPython.core.debugger import set_trace

import numpy as np
from collections import Counter

# https://leetcode.com/problems/3sum/solutions/3109452/c-easiest-beginner-friendly-sol-set-two-pointer-approach-o-n-2-time-and-o-n-space/?orderBy=most_votes


class Solution:
    def threeSum(self, nums):
        nums.sort()
        nums_a = np.array(nums)
        
        if nums_a[0] > 0:
            return []
        
        #set_trace()        
        answ_list = []
        answ_list_counters = []
        for i, el in enumerate(nums_a):
            target = 0 - el
            
            for j, el_2 in enumerate(nums_a):     
                if i != j:
                    target_2 = target - el_2
                    
                    for k, el_3 in enumerate(nums_a):
                        if el_3 == target_2 and i != j and i != k and j != k:
                            #set_trace()
                            cand = [el, el_2, el_3]
                            cand_counter = Counter(cand)
                            if cand_counter not in answ_list_counters:
                                answ_list.append(cand)
                                answ_list_counters.append(cand_counter)                            
        
        return answ_list
    
class Solution_new:
    def threeSum(self, nums):
        nums.sort()
        #nums_a = np.array(nums)
        
        if nums[0] > 0:
            return []
        
        value_indx_dict = {}
        for ind, val in enumerate(nums):
            if val not in value_indx_dict.keys():
                value_indx_dict[val] = [ind]
            else:
                value_indx_dict[val].extend([ind])
        #set_trace()        
        answ_list = []
        answ_list_counters = []
        for i, el in enumerate(nums):
            target = 0 - el
            
            for j, el_2 in enumerate(nums):     
                if i != j:
                    target_2 = target - el_2
                    
                    if target_2 in value_indx_dict.keys():
                        indx_list = value_indx_dict[target_2]
                        cands = [[el, el_2, nums[ind]] for ind in indx_list if ind != i and ind != j]
                        
                        cand_counters = [Counter(cand) for cand in cands]
                        for cand_counter, cand in zip(cand_counters, cands):
                            if cand_counter not in answ_list_counters:
                                answ_list.append(cand)
                                answ_list_counters.append(cand_counter)                            
        
        return answ_list
    
class Solution_new_2:
    def threeSum(self, nums):
        nums.sort()
        #nums_a = np.array(nums)
        '''
        if nums[0] > 0:
            return []
        '''
        value_indx_dict = {}
        for ind, val in enumerate(nums):
            if val not in value_indx_dict.keys():
                value_indx_dict[val] = [ind]
            else:
                value_indx_dict[val].extend([ind])
        #set_trace()        
        answ_list = []
        answ_list_set = []
        for i, el in enumerate(nums):
            target = 0 - el
            
            for j, el_2 in enumerate(nums):     
                if i != j:
                    target_2 = target - el_2
                    
                    if target_2 in value_indx_dict.keys():
                        indx_list = value_indx_dict[target_2]
                        cands = [[el, el_2, nums[ind]] for ind in indx_list if ind != i and ind != j]
                        
                        for cand in cands:
                            curr_set = set(cand)
                            #set_trace()
                            if curr_set not in answ_list_set:
                                answ_list_set.append(curr_set)
                                answ_list.append(cand)
        
        return answ_list
    
class Solution_new_3:
    def threeSum(self, nums):
        nums.sort()
        #nums_a = np.array(nums)
        
        if nums[0] > 0:
            return []
        if nums[0] == 0 and len(set(nums)) == 1:
            return [[0,0,0]]
        
        value_indx_dict = {}
        for ind, val in enumerate(nums):
            if val not in value_indx_dict.keys():
                value_indx_dict[val] = [ind]
            else:
                value_indx_dict[val].extend([ind])
        #set_trace()        
        answ_list = []
        answ_list_set = []
        for i, el in enumerate(nums):
            target = 0 - el
            
            for j, el_2 in enumerate(nums):     
                if i != j:
                    target_2 = target - el_2
                    
                    if target_2 in value_indx_dict.keys():
                        indx_list = value_indx_dict[target_2]
                        cands = [[el, el_2, nums[ind]] for ind in indx_list if ind != i and ind != j]
                        answ_list.extend(cands)
        
        
        answ_list = set(tuple(sorted(l)) for l in answ_list)
        return list(answ_list)
    
class Solution_new_4:
    def threeSum(self, nums):
        nums.sort()
        #nums_a = np.array(nums)
        
        if nums[0] > 0:
            return []
        if nums[0] == 0 and len(set(nums)) == 1:
            return [[0,0,0]]
        
        value_indx_dict = {}
        for ind, val in enumerate(nums):
            if val not in value_indx_dict.keys():
                value_indx_dict[val] = [ind]
            else:
                value_indx_dict[val].extend([ind])
        #set_trace()        
        answ_list = []
        answ_list_set = []
        for el, inds_i in value_indx_dict.items():
            target = 0 - el
            
            for el_2, inds_j  in value_indx_dict.items():
                if el_2 != el:
                    target_2 = target - el_2
                    
                    if target_2 != el and target_2 != el_2:
                        if target_2 in value_indx_dict.keys():
                            answ_list.append([el, el_2, target_2])
                        else:
                            if len(inds_i) >=3 and el == 0:
                                answ_list.append([el, el, el])
                            elif len(inds_i) >=2:
                                if -(el+el) in value_indx_dict.keys() and el != 0:
                                    answ_list.append([el, el, -(el+el)])
                            elif len(inds_j) >=2:
                                if -(el_2+el_2) in value_indx_dict.keys() and el_2 != 0:
                                    answ_list.append([el_2, el_2, -(el_2+el_2)])
                    
                    elif target_2 == el_2 and target_2 in value_indx_dict.keys() and target_2 != el:
                        if len(value_indx_dict[target_2])>=2 and el+target_2+target_2==0:
                            answ_list.append([el, target_2, target_2])
                    elif target_2 != el_2 and target_2 in value_indx_dict.keys() and target_2 == el:
                        if len(value_indx_dict[target_2])>=2 and el+target_2+target_2==0:
                            answ_list.append([el, target_2, target_2])
                elif el_2 == el and el == 0:
                    if len(inds_i) >= 3:
                        answ_list.append([el, el, el])
                        
        
        answ_list = set(tuple(sorted(l)) for l in answ_list)
        return list(answ_list)
    
class SolutionLeetCode:
    def threeSum(self, nums):
        nums.sort()
        result = []
        set_trace()
        for left in range(len(nums) - 2): # renamed this to left because this will always be the leftmost pointer in the triplet
            if left > 0 and nums[left] == nums[left - 1]: # this step makes sure that we do not have any duplicates in our result output
                continue 
            mid = left + 1 # renamed this to mid because this is the pointer that is between the left and right pointers
            right = len(nums) - 1
            while mid < right:
                curr_sum = nums[left] + nums[mid] + nums[right]
                if curr_sum < 0:
                    mid += 1 
                elif curr_sum > 0:
                    right -= 1
                else:
                    result.append([nums[left], nums[mid], nums[right]])
                    while mid < right and nums[mid] == nums[mid + 1]: # Another conditional for not calculating duplicates
                        mid += 1
                    while mid < right and nums[right] == nums[right - 1]: # Avoiding duplicates check
                        right -= 1
                    mid += 1
                    right -= 1
        return result

def full_pipeline(nums):
    
    #sol = Solution()
    sol_new = Solution_new()
    #sol = Solution_new_2()
    #sol = Solution_new_3()
    sol_4 = Solution_new_4()
    sol_leet = SolutionLeetCode()
    
    res_new = sol_new.threeSum(nums)
    res_4 = sol_4.threeSum(nums)
    print(res_new)
    sol_leet = sol_leet.threeSum(nums)
    return sol_leet

def common_elements(list1, list2):
    return [element for element in list1 if element in list2]
    