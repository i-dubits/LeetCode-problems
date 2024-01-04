#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        first = 0
        second = len(numbers) - 1
        
        while first <= second:
            if numbers[first] + numbers[second] > target:
                second -= 1
            elif numbers[first] + numbers[second] < target:
                first += 1
            else:
                return [first+1, second+1]
        
            
#numbers = [2,7,11,15]; target = 9
#numbers = [2,3,4]; target = 6
numbers = [-1,0]; target = -1

sol = Solution()

print(sol.twoSum(numbers, target))

