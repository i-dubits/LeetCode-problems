from typing import Optional, List
from trees_utils import TreeNode, list_to_tree
from collections import deque


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        total_count = 0
        def find_rec(root, max_val = None):
            nonlocal total_count
            if root is None:
                return

            if max_val is None:
                max_val = root.val

            if max_val <= root.val:
                total_count += 1
                max_val = root.val

            find_rec(root.left, max_val=max_val)
            find_rec(root.right, max_val=max_val)

        find_rec(root, max_val = None)
        return total_count



def full_pipeline(root):
    sol = Solution()
    root = list_to_tree(root)
    res = sol.goodNodes(root)
    return res


root = [2,1,1,3,"null",1,5]
print( full_pipeline(root) )


str_list = [
    [2,1,1,3,"null",1,5],
    [1,2,-1,3,4],
]

for str_curr in str_list:
    print( full_pipeline(str_curr) )