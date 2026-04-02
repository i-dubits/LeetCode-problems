
from typing import Optional
from trees_utils import TreeNode, list_to_tree


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root.left is None and root.right is None:
            return True

        ans = self.isSymmRec(root.right, root.left)
        return ans

    def isSymmRec(self, root_1, root_2):
        if root_1 is None and root_2 is None:
            return True
        elif (root_1 is not None and root_2 is None) or (root_1 is None and root_2 is not None):
            return False
        elif root_1.val != root_2.val:
            return False
        else:
            first = self.isSymmRec(root_1.left, root_2.right)
            second = self.isSymmRec(root_1.right, root_2.left)
            return first and second



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