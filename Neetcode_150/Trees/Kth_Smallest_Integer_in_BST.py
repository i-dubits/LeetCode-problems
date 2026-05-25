
from typing import Optional
from trees_utils import TreeNode, list_to_tree

class Solution:

    ans = 0
    cnt = 0
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        # self.inOrderTr(root, k)
        self.inOrderTrV2(root, k, 0)

        return self.ans

    def inOrderTr(self, root: TreeNode, k) -> None:

        if root is None:
            return

        self.inOrderTr(root.left, k)
        self.cnt += 1
        if self.cnt == k:
            self.ans = root.val

        self.inOrderTr(root.right, k)

    def inOrderTrV2(self, root: TreeNode, k, cnt_curr) -> int:

        if root is None:
            return cnt_curr

        cnt_curr = self.inOrderTrV2(root.left, k, cnt_curr)
        cnt_curr += 1
        if cnt_curr == k:
            self.ans = root.val

        cnt_curr = self.inOrderTrV2(root.right, k, cnt_curr)

        return cnt_curr



def full_pipeline(root, k):
    sol = Solution()
    tree = list_to_tree(root)
    res = sol.kthSmallest(tree, k)
    return res


root, k = [2,1,3], 1
print( full_pipeline(root, k) )


str_list = [
    [[2,1,3], 1],
    [[4,3,5,2,"null"], 4],

]

for str_curr in str_list:
    print( full_pipeline(*str_curr) )