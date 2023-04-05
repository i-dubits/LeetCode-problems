#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/linked-list-cycle

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
    # first solution
    def hasCycle(self, head:ListNode) -> bool:
        marked = set()
        current = head
        if current == None:
            return False
        while(current.next != None):           
            if current in marked:
                return True
            else:
                marked.add(current)
            
            current = current.next
        return False
    
    # second solution
    def hasCycleTwoPointers(self, head:ListNode) -> bool:
        '''https://en.wikipedia.org/wiki/Cycle_detection#Floyd's_tortoise_and_hare'''
        
        tort = head
        hare = head

        if tort == None:
            return False
        
        if tort.next == None:
            return False
        
        while(tort.next != None and hare.next != None):
            if hare.next.next == None:
                break
            tort = tort.next
            hare = hare.next.next
            if tort == hare:
                return True
        return False
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    