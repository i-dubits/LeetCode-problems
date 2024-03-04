# Definition for a binary tree node.

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
def list_to_tree(l1):
    head = []
    level = 0
    if l1 == []:
        return head
    else:
        head = TreeNode(l1[0])
        curr_node = head
        node_queue = []
        node_queue.append(curr_node)

        # set_trace()
        i = 1
        while i < len(l1):

            for curr_node in node_queue:
                curr_node = node_queue.pop(0)
                if i < len(l1):

                    if l1[i] != 'null':
                        curr_node.left = TreeNode(l1[i])
                        node_queue.append(curr_node.left)
                else:
                    break
                i += 1
                if i < len(l1):

                    if l1[i] != 'null':
                        curr_node.right = TreeNode(l1[i])
                        node_queue.append(curr_node.right)
                else:
                    break
                i += 1

    return head

class Solution:
    def invertTree(self, root):
        if root == []:
            return root

        self.root_new = TreeNode(root.val)
        self.doInvert(root, self.root_new)
        return self.root_new

    def doInvert(self, old, new):
        if old is not None:
            new.right = TreeNode(old.left.val) if old.left else None
            self.doInvert(old.left, new.right)
            new.left = TreeNode(old.right.val) if old.right else None
            self.doInvert(old.right, new.left)


l1 = [4,2,7,1,3,6,9]
# l1 = []
head = list_to_tree(l1)
#head.display()

sol = Solution()
root_new = sol.invertTree(head)
root_new.display()
