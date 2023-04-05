#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def swap(l1, i, j):
    tmp = l1[i]
    l1[i] = l1[j]
    l1[j] = tmp

def ins_sort(l1):
    
    if len(l1) in [0, 1]:
        return l1
    
    for i in range(1, len(l1)):
        j = i - 1
        while j >= 0 and l1[j] > l1[j+1]:
            swap(l1, j, j+1)
            j -= 1
    
    return l1


def test_ins_sort():
    # Test empty list
    assert ins_sort([]) == []

    # Test list with one element
    assert ins_sort([1]) == [1]

    # Test list with two elements
    assert ins_sort([2, 1]) == [1, 2]

    # Test list with three elements
    assert ins_sort([3, 2, 1]) == [1, 2, 3]

    # Test list with repeated elements
    assert ins_sort([5, 2, 8, 2, 5]) == [2, 2, 5, 5, 8]

    # Test list with negative numbers
    assert ins_sort([-3, 0, 4, -1, 2]) == [-3, -1, 0, 2, 4]

    # Test list already sorted
    assert ins_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    # Test list in reverse order
    assert ins_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]    