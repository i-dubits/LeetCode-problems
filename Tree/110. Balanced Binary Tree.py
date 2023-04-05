#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from IPython.core.debugger import set_trace

# https://leetcode.com/problems/symmetric-tree/description/

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

class Solution:
    
    def __init__(self):
        self.answ = 1
        self.depth_list = []

    def isBalanced(self, root) -> bool:
        if root == None:
            return 1
        else:
            self.treeLoop(root)
        
        return self.answ 
    
    def treeSetDepth(self, curr):
        #set_trace()
        self.depth_list.append(curr.depth)
        if curr.left != None:
            curr.left.depth = curr.depth + 1
            self.treeSetDepth(curr.left)
        if curr.right != None:
            curr.right.depth = curr.depth + 1
            self.treeSetDepth(curr.right)
            
    def treeDepth(self, curr):
        
        init_depth = curr.depth
        vert_queue = []
        depth_list = []
        vert_queue.append(curr)
        
        while vert_queue != []:
            curr_vert = vert_queue.pop(0)
            depth_list.append(curr_vert.depth - init_depth)
            
            if(curr_vert.left != None):
                vert_queue.append(curr_vert.left)
                
            if(curr_vert.right != None):
                vert_queue.append(curr_vert.right)
                
        return depth_list
    
class Solution_2:
    
    def __init__(self):
        self.answ = 1

    def isBalanced(self, root) -> bool:
        if root == None:
            return 1
        else:
            res = self.treeLoop(root)
        
        if res == -1:
            return 0
        else:
            return 1

    def treeLoop(self, curr):
        
        #set_trace()
        if curr == None:
            return 0
        if curr != None:
            l_h = self.treeLoop(curr.left)
            l_r = self.treeLoop(curr.right)
            
            if abs(l_h - l_r) > 1 or l_h == -1 or l_r == -1:
                return -1
            
            return 1 + max(l_h, l_r)
        

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
                i+=1
                if i < len(l1):
                    
                    if l1[i] != 'null':
                        curr_node.right = TreeNode(l1[i])
                        node_queue.append(curr_node.right)
                else:
                    break
                i+=1

                
    return head
                
                
    
def tree_loop(p):
    
    if p.left == None and p.right == None:
        print('leaf')
        
    if p.left != None:
        tree_loop(p.left)

    if p.right != None:
        tree_loop(p.right)

def full_pipeline(p):
    
    sol = Solution_2()
    p_tree = list_to_tree(p)
    res = sol.isBalanced(p_tree)
    print(res)
    return res

