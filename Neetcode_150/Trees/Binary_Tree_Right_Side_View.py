from typing import Optional, List
from trees_utils import TreeNode, list_to_tree
from collections import deque


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        ans = []
        if not root:
            return ans

        queue = deque()
        queue.append(root)

        while queue:
            ans.append(queue[-1].val)

            for i in range(len(queue)):
                curr_node = queue.popleft()

                if curr_node.left is not None:
                    queue.append(curr_node.left)
                if curr_node.right is not None:
                    queue.append(curr_node.right)

        return ans


def full_pipeline(root):
    sol = Solution()
    root = list_to_tree(root)
    res = sol.rightSideView(root)
    return res


root = []
# root = [1,2,3,"null",4,"null",5]
print( full_pipeline(root) )


str_list = [
    [1,2,3,"null",4,"null",5],
    [1,2,3,4,"null","null","null",5],
    [1,"null",2],
    []
]

for str_curr in str_list:
    print( full_pipeline(str_curr) )