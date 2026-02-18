
from typing import Optional
from trees_utils import TreeNode, list_to_tree

class Solution:

    ans = None

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode | int, q: TreeNode | int) -> TreeNode:
        self.search_common(root, p, q)
        return self.ans

    def search_common(self, root: TreeNode, p: TreeNode | int, q: TreeNode | int):
        if isinstance(p, TreeNode):
            p = p.val
        if isinstance(q, TreeNode):
            q = q.val

        if root:
            if root.val == p or root.val == q:
                self.ans = root
                return
            elif root.val > p and root.val > q:
                self.search_common(root.left, p, q)
            elif root.val < p and root.val < q:
                self.search_common(root.right, p, q)
            else:
                self.ans = root
                return

        else:
            return


def full_pipeline(root, p, q):
    sol = Solution()
    tree = list_to_tree(root)
    res = sol.lowestCommonAncestor(tree, p, q)
    print(res.val)
    return res



root = [5,3,8,1,4,7,9,"null",2]
p, q = 3, 8
print( full_pipeline(root, p, q) )


str_list = [
    [[5,3,8,1,4,7,9,"null",2], 3, 8],
    [[5,3,8,1,4,7,9,"null",2], 3, 4],

]

for str_curr in str_list:
    print( full_pipeline(*str_curr) )