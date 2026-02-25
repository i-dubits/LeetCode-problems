from typing import Optional
from trees_utils import TreeNode, list_to_tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        ans = False

        def run_traversal(root, subroot):
            nonlocal ans
            if root is not None:
                res = self.check_eq(root, subRoot)
                if res:
                    ans = True
                    return

                run_traversal(root.left, subRoot)
                run_traversal(root.right, subRoot)
            else:
                return

        run_traversal(root, subRoot)
        return ans

    def check_eq(self, root_1, root_2):
        if root_1 is not None and root_2 is not None:
            if root_1.val != root_2.val:
                return False

            res_l = self.check_eq(root_1.left, root_2.left)
            res_r = self.check_eq(root_1.right, root_2.right)

            if res_l is False or res_r is False:
                return False
            else:
                return True

        elif root_1 is None and root_2 is None:
            return True
        else:
            return False


def full_pipeline(root, subroot):
    sol = Solution()
    root = list_to_tree(root)
    subroot = list_to_tree(subroot)
    res = sol.isSubtree(root, subroot)
    # print(res)
    return res


root, subroot = [1,2,3,4,5], [2,4,5]
# root = [1,2,3]
print( full_pipeline(root, subroot) )


str_list = [
    [[1,2,3,4,5], [2,4,5]],
    [[1,2,3,4,5,"null","null",6], [2,4,5]],
]

for str_curr in str_list:
    print( full_pipeline(*str_curr) )