#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from IPython.core.debugger import set_trace

def binary_search(arr, target):

    l = -1
    r = len(arr)
    
    #set_trace()
    while l != r - 1:
        m = (l + r) // 2
        if arr[m] < target:
            l = m
        else:
            r = m
    return r