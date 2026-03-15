
from typing import Optional, List
from trees_utils import TreeNode, list_to_tree

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.target = targetSum
        self.ans = list()

        if root is None:
            return []

        self.pathRec(root, 0, ())

        ans_list = [list(tuple_curr) for tuple_curr in self.ans]

        if len(ans_list) == 1 and len(ans_list[0]) == 0:
            return []
        return ans_list

    def pathRec(self, root, curr_sum, curr_path:tuple):

        curr_sum += root.val
        curr_path = curr_path + (root.val,)

        if root.left is None and root.right is None:
            if curr_sum == self.target:
                self.ans.append(curr_path)
            return

        if root.left is not None:
            self.pathRec(root.left, curr_sum, curr_path)
        if root.right is not None:
            self.pathRec(root.right, curr_sum, curr_path)




def full_pipeline(p):
    sol = Solution()
    tree = list_to_tree(p[0])
    res = sol.pathSum(tree, p[1])
    return res


# root = [[5,4,8,11,"null",13,4,7,2,"null","null",5,1], 22]
# root = [[1,2], 1]
root = [[0,1,1], 1]
print( full_pipeline(root) )


str_list = [
    [[5,4,8,11,"null",13,4,7,2,"null","null",5,1], 22],
    [[1,2,3], 5],
    [[1,2], 0],
]

for str_curr in str_list:
    print( full_pipeline(str_curr) )