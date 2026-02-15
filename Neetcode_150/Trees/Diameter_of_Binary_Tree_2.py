
from typing import Optional
from trees_utils import TreeNode, list_to_tree

class Solution:

    max_path = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diamRec(root)
        return self.max_path

    def diamRec(self, root) -> int:
        if root:
            depth_l = self.diamRec(root.left) + 1
            depth_r = self.diamRec(root.right) + 1

            local_ans = depth_l + depth_r
            self.max_path = max(self.max_path, local_ans)

            return max(depth_r, depth_l)

        else:
            return -1





def full_pipeline(p):
    sol = Solution()
    tree = list_to_tree(p)
    res = sol.diameterOfBinaryTree(tree)
    # print(res)
    return res


root = [1,"null",2,3,4,5]
# root = [1,2,3]
print( full_pipeline(root) )


str_list = [
    [1,"null",2,3,4,5],
    [1,2,3],
]

for str_curr in str_list:
    print( full_pipeline(str_curr) )