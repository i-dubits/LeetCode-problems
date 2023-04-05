#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# https://leetcode.com/problems/merge-k-sorted-lists/

from __future__ import annotations

from IPython.core.debugger import set_trace

import numpy as np

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

def list_of_lists_to_linked_lists(lst):
    
    if lst == [] or lst == [[]]:
        return None
    
    list_of_lists = []
    for curr in lst:
        list_of_lists.append(list_to_linked_list(curr))
    
    return list_of_lists

def print_linked_list(l1):
    curr = l1
    while curr != None:
        print(curr.val)
        curr = curr.next
        
class Solution:
    def mergeKLists(self, lists) -> [ListNode]:
        if lists == None:
            return None
        if lists == [[]]:
            return None
        
        pointer_list = []
        
        #set_trace()
        pointer_list = [link_list for link_list in lists if link_list != None]
        
        if pointer_list != []:
            min_ind = find_min_indx(pointer_list)
            res_head = ListNode(pointer_list[min_ind].val, None)
            current = res_head        
            pointer_list[min_ind] = pointer_list[min_ind].next
            if pointer_list[min_ind] == None:
                pointer_list.remove(pointer_list[min_ind])
            
            while pointer_list != []:
                #print(pointer_list)
                min_ind = find_min_indx(pointer_list)
                current.next = ListNode(pointer_list[min_ind].val, None)
                current = current.next
                
                pointer_list[min_ind] = pointer_list[min_ind].next
                if pointer_list[min_ind] == None:
                    pointer_list.remove(pointer_list[min_ind])
            return res_head
        else:
            return None
        
        
def find_min_indx(pointer_list):
    #print(pointer_list)
    if pointer_list != []:
        min_index = np.argmin(np.array([curr.val for curr in pointer_list]))
        return min_index
    
    

def full_pipeline(l1):
    
    lnk_l1 = list_of_lists_to_linked_lists(l1)
    
    sol = Solution()
    res = sol.mergeKLists(lnk_l1)
    
    print_linked_list(res)
    
    return res



