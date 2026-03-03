
from typing import List, Optional
from trees_utils import TreeNode, list_to_tree

import math

class Solution:

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.preorder = preorder
        self.inorder = inorder
        self.glob_ind = 0
        self.inorder_val_to_ind = {}

        for i, val in enumerate(self.inorder):
            self.inorder_val_to_ind[val] = i

        root = self.buildRec(0, len(self.inorder) - 1)

        return root

    def buildRec(self, l, r):

        if l > r:
            return None

        curr_node_val = self.preorder[self.glob_ind]
        self.glob_ind += 1
        curr_ind = self.inorder_val_to_ind[curr_node_val]

        curr_el = TreeNode(curr_node_val)

        curr_el.left = self.buildRec(l, curr_ind - 1)
        curr_el.right = self.buildRec(curr_ind + 1, r)

        return curr_el




def full_pipeline(p):
    sol = Solution()
    preorder, inorder = p

    res = sol.buildTree(preorder, inorder)
    return res


# root = [[1,2,3,4], [2,1,3,4]]
root = [[1], [1]]
full_pipeline(root).display()


str_list = [
    [[1,2,3,4], [2,1,3,4]],
    [[1], [1]],
]

for str_curr in str_list:
    full_pipeline(str_curr).display()
