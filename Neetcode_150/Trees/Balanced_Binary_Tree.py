
from typing import Optional
from trees_utils import TreeNode, list_to_tree

class Solution:

    balanced = True

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balRec(root)
        return self.balanced

    def balRec(self, root):
        if root:
            height_l = self.balRec(root.left) + 1
            height_r = self.balRec(root.right) + 1

            diff_b = abs(height_r - height_l)

            if diff_b >= 2:
                self.balanced = False

            return max(height_l, height_r)
        else:
            return 0



def full_pipeline(p):
    sol = Solution()
    tree = list_to_tree(p)
    res = sol.isBalanced(tree)
    # print(res)
    return res


# root = [1,2,3,"null","null",4]
# root = [1,2,3,"null","null",4,"null",5]
root = [1,2,2,3,"null","null",3,4,"null","null",4]
print( full_pipeline(root) )


str_list = [
    [1,2,3,"null","null",4],
    [1,2,3,"null","null",4,"null",5],
    [],
    [1,2,2,3,"null","null",3,4,"null","null",4]
]

for str_curr in str_list:
    print( full_pipeline(str_curr) )