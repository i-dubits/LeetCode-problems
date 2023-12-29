#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://leetcode.com/problems/top-k-frequent-words/

from IPython.core.debugger import set_trace

import heapq

class Node(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val

    def __lt__(self, other):
        return self.val < other.val

class Solution:
    def topKFrequent(self, words, k):
        
        my_dict = {}
        
        for word in words:
            if word in my_dict:
                my_dict[word] -= 1
            else:
                my_dict[word] = -1
        
        #set_trace()
        node_array = [Node(k,v) for k,v in my_dict.items()]
        heapq.heapify(node_array)
        
        str_list = []
        curr_node =  heapq.heappop(node_array)
        curr_str, curr_freq = curr_node.key, curr_node.val
        
        repeat_length = 0
        subset = []
        subset.append(curr_str)
        counter = 0
        while counter != k:
            
            if node_array != []:
                curr_node = heapq.heappop(node_array)
                if curr_freq == curr_node.val:
                    repeat_length += 1
                    subset.append(curr_node.key)
                else:
                    subset = sorted(subset)
                    str_list.extend(subset)
                    subset = []
                    repeat_length = 0
                    curr_freq = curr_node.val
                    subset.append(curr_node.key)
                    counter += 1
            else:
                break

        
        if  subset != []:
            str_list.extend(sorted(subset))
        return str_list[:k]
                    
def full_pipeline(words, k):
    sol = Solution()
    str_list = sol.topKFrequent(words, k)
    print(str_list)
    return str_list
    
    
words = ["the","day","is","sunny","the","the","the","sunny","is","is"]; k = 4
full_pipeline(words, k)    
    
            
         
        
                