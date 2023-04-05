#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 20:16:16 2023

@author: ild
"""

# https://leetcode.com/problems/add-two-numbers/

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
    
    def addTwoNumbers(self, l1: [ListNode], l2: [ListNode]) -> [ListNode]:
        
        #set_trace()
        head = ListNode()
        current_node = head
        
        one_rememb = False
        while l1 != None or l2 != None:
            
            if l1 != None and l2 != None:
                sum_digit = l1.val+l2.val
                if one_rememb:
                    sum_digit += 1
            else:
                sum_digit = l2.val if l1 == None else l1.val
                if one_rememb:
                    sum_digit += 1
            
            if sum_digit < 10:
                current_node.val = sum_digit
                
                if if_make_node(l1, l2):
                    new_node = ListNode()
                    current_node.next = new_node
                    current_node = new_node
                
                one_rememb = False
            elif sum_digit >= 10:
                
                current_node.val = (sum_digit) % 10
                
                if if_make_node(l1, l2):
                    new_node = ListNode()
                    current_node.next = new_node
                    current_node = new_node
                
                one_rememb = True
                
            l1 = l1.next if l1 != None else None
            l2 = l2.next if l2 != None else None
        
        if one_rememb:
            new_node = ListNode(1)
            current_node.next = new_node
        
        return head
    

def if_make_node(l1, l2):
    
    if l1 != None:
        if l1.next != None:
            return True
    if l2 != None:
        if l2.next != None:
            return True
    return False
    
def full_pipeline(l1, l2):
    
    lnk_l1 = list_to_linked_list(l1)
    lnk_l2 = list_to_linked_list(l2)
    
    sol = Solution()
    res = sol.addTwoNumbers(lnk_l1, lnk_l2)
    
    print_linked_list(res)
    
    return res
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


    
    
