#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from IPython.core.debugger import set_trace

class Solution:
    def isValid(self, s: str) -> bool:
        my_stack = []
        
        dict_op = {']':'[', '}':'{', ')':'('}
        
        for char in s:            
            
            if char in ['[', '{', '(']:
                my_stack.append(char)            
            
            elif char in [']', '}', ')']:
                if my_stack != []:
                    char_op = my_stack.pop()
                    if dict_op[char] == char_op:
                        continue
                return False
        if my_stack == []:
            return True
        else:
            return False
    
 
def full_pipeline(my_str):
    
    sol = Solution()
    res = sol.isValid(my_str)
    print(res)
    return res