
from typing import Optional
from trees_utils import TreeNode, list_to_tree


class Solution:
    def isSameTree(self, t_1: Optional[TreeNode], t_2: Optional[TreeNode]) -> bool:
        if t_1 is None and t_2 is None:
            return True
        elif t_1 is not None and t_2 is not None:
            if t_1.val != t_2.val:
                return False

            res_l = self.isSameTree(t_1.left, t_2.left)
            res_r = self.isSameTree(t_1.right, t_2.right)

            return res_r and res_l

        else:
            return False



def full_pipeline(p):
    sol = Solution()
    r1, r2 = p[0], p[1]
    tree1 = list_to_tree(r1)
    tree2 = list_to_tree(r2)
    res = sol.isSameTree(tree1, tree2)
    # res.display()
    return res

root = [[1,2,3], [1,2,3]]
print( full_pipeline(root) )


str_list = [
    [[1,2,3], [1,2,3]],
    [[1,2], [1,"null",2]],
    [[1,2,1], [1,1,2]],
]

for str_curr in str_list:
    print( full_pipeline(str_curr) )