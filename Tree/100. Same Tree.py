#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from IPython.core.debugger import set_trace

# https://leetcode.com/problems/same-tree/

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
    
    
    def loopTree(self, p, q):
        #set_trace()
        if p == None and q == None:
            return

        if (p != None and q == None) or (p == None and q != None):
            self.answ = 0
            return

        if p.left == None and p.right == None and q.left == None and q.right == None:
            if p.val != q.val:
                self.answ = 0
            return

        if (p.left != None and q.left == None) or (p.left == None and q.left != None):
            self.answ = 0
            return
        
        if (p.right != None and q.right == None) or (p.right == None and q.right != None):
            self.answ = 0
            return

        if p.left != None and q.left != None:
            if p.val != q.val:
                self.answ = 0
                return
            else:
                self.loopTree(p.left, q.left)
        
        if p.right != None and q.right != None:
            if p.val != q.val:
                self.answ = 0
                return
            else:
                self.loopTree(p.right, q.right)

        if (p.left != None and q.left == None) or (p.left == None and q.left != None):
            self.answ = 0
            return

        if (p.right != None and q.right == None) or (p.right == None and q.right != None):
            self.answ = 0
            return        
    
    def isSameTree(self, p, q) -> bool:
        self.loopTree(p, q)
        return self.answ

class Solution_2:
        
    def isSameTree(self, p, q) -> bool:
        
        if p == None and q == None:
            return 1
        
        if (p != None and q == None) or (p == None and q != None):
            return 0
        
        if p.val != q.val:
            return 0
        
        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
    
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
        
        #set_trace()
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

def full_pipeline(p, q):
    
    sol = Solution()
    p_tree = list_to_tree(p)
    q_tree = list_to_tree(q)
    res = sol.isSameTree(p_tree, q_tree)
    print(res)
    return res

