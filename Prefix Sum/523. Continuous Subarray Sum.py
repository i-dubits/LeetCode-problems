from collections import Counter

class Solution:
    def checkSubarraySum(self, nums, k: int) -> bool:
        prefix_sum = []
        prefix_sum.append(nums[0])
        for i in range(1, len(nums)):
            prefix_sum.append( prefix_sum[i - 1] + nums[i])

        prefix_sum_rest = [pref % k for pref in prefix_sum]

        if len(nums) == 1:
            return False

        if len(nums) == 2:
            if sum(nums)%k == 0:
                return True
            else:
                return False


        pref_dict = {}
        for i in range(len(prefix_sum_rest)):
            if prefix_sum_rest[i] == 0 and i != 0:
                return True
            if prefix_sum_rest[i] in pref_dict:
                if i - pref_dict[prefix_sum_rest[i]] > 1:
                    return True
            else:
                pref_dict[prefix_sum_rest[i]] = i
        return False



sol = Solution()
# lst = [23,2,4,6,7]
# k=6
# lst = [23,2,4,6,6]
# k=7
# lst = [1, 2, 12]
# k=6
# lst = [23,2,6,4,7]
# k=6
# lst = [23,2,6,4,7]
# k=13
# lst = [5,0,0,0]
# k=3
lst = [0,1,0,3,0,4,0,4,0]
k=5

print(sol.checkSubarraySum(lst, k))


