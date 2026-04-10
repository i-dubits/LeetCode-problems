
from typing import Optional, List
from trees_utils import TreeNode, list_to_tree


class Solution:

    def __init__(self):
        self.val_to_node = {}

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.p = p
        self.q = q

        self.path_p = self.find(root, p.val, [])
        self.path_q = self.find(root, q.val, [])


        # self.path_p = self.path_p[::-1]
        # self.path_q = self.path_q[::-1]

        # [node.val for node in self.path_p]
        ans = -1
        ind_1, ind_2 = 0, 0
        while ind_1 < len(self.path_p) and ind_2 < len(self.path_q):
            if self.path_p[ind_1].val == self.path_q[ind_2].val:
                ans = self.path_p[ind_1]
            ind_1 += 1
            ind_2 += 1

        return ans

    def find(self, root, target_val, path: list[int]) -> List[int]:
        path_final = []

        def dfs(root, target_val, path):
            nonlocal path_final
            if root is None:
                return

            path.append(root)
            if root.val == target_val:
                path_final = path[:]
                return

            dfs(root.left, target_val, path)
            dfs(root.right, target_val, path)
            path.pop()
            return

        dfs(root, target_val, [])
        return path_final


    def populate_map(self, root):
        if root is None:
            return
        self.val_to_node[root.val] = root
        self.populate_map(root.left)
        self.populate_map(root.right)

def full_pipeline(p):
    sol = Solution()
    root, p, q = p[0], p[1], p[2]
    root = list_to_tree(root)
    sol.populate_map(root)
    p_node = sol.val_to_node[p]
    q_node = sol.val_to_node[q]
    res = sol.lowestCommonAncestor(root, p_node, q_node)
    # res.display()
    return res.val

# root = [[5,3,4,2,1], 1, 2]
root = [[5,3,4,2,1,"null",9,"null",11,10,12], 3, 12]
print( full_pipeline(root) )


str_list = [
    [[5,3,4,2,1], 1, 2],
    [[5,3,4,2,1,"null",9,"null",11,10,12], 3, 12],
]

for str_curr in str_list:
    print( full_pipeline(str_curr) )