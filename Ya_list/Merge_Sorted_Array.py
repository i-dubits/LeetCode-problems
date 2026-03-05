from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = m - 1
        p2 = n - 1
        curr_ptr = n + m - 1

        while p1 >= 0 or p2 >= 0:
            if p1 == -1:
                while curr_ptr != -1:
                    nums1[curr_ptr] = nums2[p2]
                    p2 -= 1
                    curr_ptr -= 1
                return nums1
            elif p2 == -1:
                while curr_ptr != -1:
                    nums1[curr_ptr] = nums1[p1]
                    p1 -= 1
                    curr_ptr -= 1
                return nums1
            else:
                if nums1[p1] >= nums2[p2]:
                    nums1[curr_ptr] = nums1[p1]
                    p1 -= 1
                else:
                    nums1[curr_ptr] = nums2[p2]
                    p2 -= 1
                curr_ptr -= 1
        return nums1



def full_pipeline(nums):

    sol = Solution()
    ans = sol.merge(*nums)
    return ans

# numbers = [[10,20,20,40,0,0], 4, [1,2], 2]
numbers = [[1,2,3,0,0,0], 3, [2, 5,6], 3]

print( full_pipeline(numbers) )


str_list = [
    [[10,20,20,40,0,0], 4, [1,2], 2],
    [[0, 0], 0, [1,2], 2],
    [[1,2,3,0,0,0], 3, [2, 5,6], 3]
]

for str_curr in str_list:
    print( full_pipeline(str_curr) )