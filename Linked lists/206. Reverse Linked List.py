#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/reverse-linked-list/

from __future__ import annotations

from IPython.core.debugger import set_trace

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def list_to_linked_list(lst):
    if not lst:
        return None

    #set_trace()
    head = ListNode(lst[0])
    current_node = head

    for val in lst[1:]:
        new_node = ListNode(val)
        current_node.next = new_node
        current_node = new_node

    return head

def print_linked_list(l1):
    curr = l1
    while curr != None:
        print(curr.val)
        curr = curr.next
        
class Solution:
    def reverseList(self, head: [ListNode]) -> [ListNode]:
      
        my_stack = []
        
        if head == None:
            return head
        if head.next == None:
            return head
          
        
        current = head
        while current != None:     
            my_stack.append(current)
            current = current.next
        
        #set_trace()
        my_stack = my_stack[::-1]
        new_head = my_stack[0]
        current = new_head
        for el in my_stack[1:]:            
            current.next = el
            current = current.next
            
        current.next = None
        return new_head
            
        
def full_pipeline(l1):
    
    lnk_l1 = list_to_linked_list(l1)
    
    sol = Solution()
    res = sol.reverseListRec(lnk_l1)
    
    print_linked_list(res)
    
    return res
        

