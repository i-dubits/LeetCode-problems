class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def display(self):
        '''https://stackoverflow.com/questions/34012886/print-binary-tree-level-by-level-in-python'''
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.val
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.val
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.val
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.val
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


# tree is written string by string in list
def build_tree(lst):
    if not lst:
        return None
    root = TreeNode(lst[0])
    queue = [root]
    is_left_child = True  # Flag to alternate between left and right children

    for value in lst[1:]:
        current_node = queue[0]  # Always work with the first node in the queue
        if value is not None:
            new_node = TreeNode(value)
            if is_left_child:
                current_node.left = new_node
            else:
                current_node.right = new_node
            queue.append(new_node)  # Add this new node to the queue

        if not is_left_child:
            # If we just attached a right child, it's time to move to the next node in the queue
            queue.pop(0)

        # Flip the flag to alternate between attaching left and right children
        is_left_child = not is_left_child

    return root


class Solution:
    def rightSideView(self, root):
        if root == None:
            return []

        arr_prev = []
        arr_prev.append(root)
        arr_curr = []
        level = 1
        res = []
        res.append(root.val)
        while len(arr_prev) != 0:
            while len(arr_prev) != 0:
                curr = arr_prev.pop(0)
                if curr.left is not None:
                    arr_curr.append(curr.left)
                if curr.right is not None:
                    arr_curr.append(curr.right)
            if arr_curr != []:
                res.append(arr_curr[-1].val)
            arr_prev = arr_curr.copy()
            arr_curr = []
            level += 1

        return res


# lst = [1,2,3,None,5,None,4]
lst = [1, None, 3]
# lst = [1,2,3,None,5,6,None,4]
root = build_tree(lst)
root.display()
sol = Solution()
res = sol.rightSideView(root)
print(res)
