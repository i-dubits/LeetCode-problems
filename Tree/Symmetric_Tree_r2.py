
from typing import Optional
from trees_utils import TreeNode, list_to_tree

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root.left is None and root.right is None:
            return True

        res = self.symRec(root.right, root.left)
        return res

    def symRec(self, root_1: TreeNode, root_2: TreeNode):
        if root_1 is None and root_2 is None:
            return True
        elif root_1 is not None and root_2 is not None:

            if root_1.val != root_2.val:
                return False

            res_1 = self.symRec(root_1.left, root_2.right)
            res_2 = self.symRec(root_1.right, root_2.left)

            return res_1 and res_2

        else:
            return False



def full_pipeline(p):
    sol = Solution()
    tree = list_to_tree(p)
    res = sol.isSymmetric(tree)
    # res.display()
    return res

root = [1,2,2,3,4,4,3]
print( full_pipeline(root) )


str_list = [
    [1,2,2,3,4,4,3],
    [1,2,2,"null",3,"null",3],
]

for str_curr in str_list:
    print( full_pipeline(str_curr) )