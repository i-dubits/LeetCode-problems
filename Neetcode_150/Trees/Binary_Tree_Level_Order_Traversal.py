from typing import Optional, List
from trees_utils import TreeNode, list_to_tree

from collections import deque


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        queue = deque()
        if not root:
            return ans
        queue.append(root)

        while queue:
            level_list = []
            init_q_len = len(queue)
            for i in range(init_q_len):
                curr_node = queue.popleft()
                level_list.append(curr_node.val)
                if curr_node.left is not None:
                    queue.append(curr_node.left)
                if curr_node.right is not None:
                    queue.append(curr_node.right)

            ans.append(level_list)

        return ans



def full_pipeline(root):
    sol = Solution()
    root = list_to_tree(root)
    res = sol.levelOrder(root)
    # print(res)
    return res


# root = [1,2,3,4,5,6,7]
root = []
print( full_pipeline(root) )


str_list = [
    [1,2,3,4,5,6,7],
    [1],
    []
]

for str_curr in str_list:
    print( full_pipeline(str_curr) )