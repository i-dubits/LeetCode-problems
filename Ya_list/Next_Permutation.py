from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return

        r = len(nums) - 2
        while r >= 0 and nums[r] >= nums[r + 1]:
            r -= 1
        if r == -1:
            pivot_ind = -1
        else:
            pivot_ind = r

            r = len(nums) - 1
            while r > pivot_ind:
                if nums[r] > nums[pivot_ind]:
                    target_ind = r
                    break
                r -= 1
            nums[pivot_ind], nums[target_ind] = nums[target_ind], nums[pivot_ind]

        # reverse in-place
        l = pivot_ind + 1
        r = len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

        return nums

def full_pipeline(nums):

    sol = Solution()
    ans = sol.nextPermutation(nums)
    return ans

# numbers = [1,2,3]
# numbers = [2,3,1]
numbers = [3,2,1]
# numbers = [1,3,2]
print( full_pipeline(numbers) )

str_list = [
    [1,2,3],
    [3,2,1],
    [1,1,5],
    [2,3,1],
    [1,3,2],
]

for str_curr in str_list:
    print( full_pipeline(str_curr) )