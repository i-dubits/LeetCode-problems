from typing import Optional, List
from trees_utils import TreeNode, list_to_tree
from collections import deque


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        self.inv_rec(root)
        return root

    def inv_rec(self, curr_node: TreeNode):
        if curr_node is None:
            return

        curr_node.left, curr_node.right = curr_node.right, curr_node.left
        self.inv_rec(curr_node.left)
        self.inv_rec(curr_node.right)

def full_pipeline(root_list):
    sol = Solution()
    root = list_to_tree(root_list)
    res = sol.invertTree(root)
    res.display()
    return res


# root_list = [1,2,3,4,5,6,7]
root_list = []
print( full_pipeline(root_list) )


str_list = [
    [1,2,3,4,5,6,7],
    [3,2,1],
    [],
]

for str_curr in str_list:
    print( full_pipeline(str_curr) )