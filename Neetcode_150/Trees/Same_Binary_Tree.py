
from typing import Optional
from trees_utils import TreeNode, list_to_tree

class Solution:


    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if p is None and q is None:
            return True

        elif p is not None and q is not None:
            if p.val != q.val:
                return False

            prev_ans = self.isSameTree(p.left, q.left)
            if prev_ans is False:
                return False
            prev_ans = self.isSameTree(p.right, q.right)
            if prev_ans is False:
                return False

            return True

        else:
            return False



def full_pipeline(root_1, root_2):
    sol = Solution()
    tree_1 = list_to_tree(root_1)
    tree_2 = list_to_tree(root_2)
    res = sol.isSameTree(tree_1, tree_2)
    return res


root_1, root_2 = [1,2,3], [1,2,3]
print( full_pipeline(root_1, root_2) )


str_list = [
    [[1,2,3], [1,2,3]],
    [[4,7], [4,"null",7]],
    [[1,2,3], [1,3,2]],
]

for str_curr in str_list:
    print( full_pipeline(*str_curr) )