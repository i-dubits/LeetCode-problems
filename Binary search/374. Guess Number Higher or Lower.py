#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:    

class Solution:
    def guessNumber(self, n: int) -> int:
        l = -1
        r = n + 1
        m = (l + r) // 2
        while guess(m) != 0:
            if guess(m) == -1:
                r = m
            if guess(m) == 1:
                l = m
            m = (l + r) // 2
            
        return m