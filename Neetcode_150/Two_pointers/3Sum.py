

from typing import List

class Solution:

    nums_count: dict = None
    ans: set() = None

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        self.nums_count = {}
        self.ans = set()

        for num in nums:
            if num not in self.nums_count:
                self.nums_count[num] = 1
            else:
                self.nums_count[num] += 1

        for ind, exclude_num in enumerate(nums):
            target = -exclude_num
            self.twoSum(nums, ind, exclude_num, target)

        ans_list = [list(triple) for triple in self.ans]

        return ans_list

    def twoSum(self, nums, ind, exclude_num: int, target: int):
        self.nums_count[exclude_num] -= 1

        for ind_curr, num in enumerate(nums):
            if ind_curr != ind:
                num_cand = target - num
                self.nums_count[num] -= 1
                if num_cand in self.nums_count and self.nums_count[num_cand] > 0:
                    curr_triple = tuple(sorted((exclude_num, num, target - num)))
                    self.ans.add(curr_triple)

                self.nums_count[num] += 1

        self.nums_count[exclude_num] += 1



def full_pipeline(numbers):
    sol = Solution()
    ans = sol.threeSum(numbers)
    return ans


numbers = [-1,0,1,2,-1,-4]


print( full_pipeline(numbers) )


str_list = [
    [-1,0,1,2,-1,-4],
    [0,1,1],
    [0,0,0],

]

for str_curr in str_list:
    print( full_pipeline(str_curr) )