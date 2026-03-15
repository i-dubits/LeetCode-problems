
from typing import Optional, List
from trees_utils import TreeNode, list_to_tree

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.target = targetSum
        self.ans = []
        if root is None:
            return []
        self.pathRec(root, [], 0)

        return self.ans

    def pathRec(self, root:TreeNode, path:list, curr_sum:int):

        path.append(root.val)
        curr_sum += root.val
        if root.left is None and root.right is None:
            if curr_sum == self.target:
                self.ans.append(path.copy())

        if root.left is not None:
            self.pathRec(root.left, path, curr_sum)
        if root.right is not None:
            self.pathRec(root.right, path, curr_sum)

        path.pop()



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
    [[1,2], 1],
    [[0,1,1], 1],
]

for str_curr in str_list:
    print( full_pipeline(str_curr) )