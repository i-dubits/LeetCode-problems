#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from IPython.core.debugger import set_trace


from random import randint 

def swap(l1, i, j):
    tmp = l1[i]
    l1[i] = l1[j]
    l1[j] = tmp


def pivot_arange(arr, left, right):
    piv_indx = randint(left, right)
    #piv_indx = (left + right) // 2
    pivot = arr[piv_indx]
    i = left
    j = right
    
    while i <= j:
        
        while i < right+1:
            if arr[i] >= pivot:
                break
            i+=1
            
        while j > left:
            if arr[j] <= pivot:
                break
            j-=1
            
        if i >= j:
            break
        swap(arr, i, j)
        i+=1
        j-=1
    
    return j

def quick_sort(arr, left, right):
    if left + 1 <= right: 
        mid = pivot_arange(arr, left, right)
        quick_sort(arr, left, mid)
        quick_sort(arr, mid+1, right)
        
    


def test_quick_sort(sort_method):
    # Test empty list
    assert sort_method([]) == []

    # Test list with one element
    assert sort_method([1]) == [1]

    # Test list with two elements
    assert sort_method([2, 1]) == [1, 2]

    # Test list with three elements
    assert sort_method([3, 2, 1]) == [1, 2, 3]

    # Test list with repeated elements
    assert sort_method([5, 2, 8, 2, 5]) == [2, 2, 5, 5, 8]

    # Test list with negative numbers
    assert sort_method([-3, 0, 4, -1, 2]) == [-3, -1, 0, 2, 4]

    # Test list already sorted
    assert sort_method([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    # Test list in reverse order
    assert sort_method([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]    