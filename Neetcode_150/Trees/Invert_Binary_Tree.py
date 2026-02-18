

from typing import Optional
from trees_utils import TreeNode, list_to_tree

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root


def full_pipeline(p):
    sol = Solution()
    tree = list_to_tree(p)
    res = sol.invertTree(tree)
    # print(res)
    return res


root = [1,2,3,4,5,6,7]
print( full_pipeline(root) )


str_list = [
    [1,2,3,4,5,6,7],
    [3,2,1],
    []
]

for str_curr in str_list:
    print( full_pipeline(str_curr) )