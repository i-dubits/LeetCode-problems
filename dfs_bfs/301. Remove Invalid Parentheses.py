#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import defaultdict

from IPython.core.debugger import set_trace
import networkx as nx
import matplotlib.pyplot as plt

from collections import deque

import time

t1 = time.time()

queue = deque()
#curr_string = "()())()"
#curr_string = "(((k()(("
#curr_string = "(a)())()"
curr_string = "()(((((((()"
curr_string = "()((((((()l("

queue.append(curr_string)

def is_valid(string):
    
    if string == '':
        return True
    
    counter_right = 0   # (
    counter_left = 0    # )
    
    for i in range(len(string)):
        if string[i] == '(':
            counter_right += 1
            counter_left -= 1
            
        elif string[i] == ')':
            counter_right -= 1
            if counter_right < 0:
                return False
            
            counter_left += 1
    
    if counter_right == counter_left:
        return True
    
    else:
        return False

answ = set()
answ_len = 1000
all_strings = set()

if is_valid(curr_string):
   answ.add(curr_string)
   
else:
    while queue and len(curr_string) > 0:
        #set_trace()
        curr_string = queue.popleft()
        if answ and len(curr_string) < answ_len:
            break
        for i in range(len(curr_string)):
            if curr_string[i] == '(' or curr_string[i] == ')':
                new_string = curr_string[:i] + curr_string[i+1:]
                #print(new_string)
                if is_valid(new_string):
                   answ.add(new_string)
                   answ_len = len(new_string)
                
                if new_string != '' and new_string not in all_strings:
                    queue.append(new_string)
                    all_strings.add(new_string)
                  
            else:
                if is_valid(curr_string):
                   answ.add(curr_string)
                   answ_len = len(curr_string)
             
           
print(list(answ))
        
                    
t2 = time.time()

print(t2-t1)















