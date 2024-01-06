#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if len(prices) <= 1:
            return 0
                    
        cand_buy = prices[0]
        cand_sell = -1_000_000
        
        res_diff = 0
        
        for i in range(1, len(prices)):
            if prices[i] > cand_buy:
                cand_sell = max(cand_sell, prices[i])
            elif prices[i] < cand_buy:
                res_diff = max(res_diff, cand_sell - cand_buy)
                cand_buy = min(cand_buy, prices[i])
                cand_sell = -1_000_000
                
        res_diff = max(res_diff, cand_sell - cand_buy)
        return res_diff if res_diff > 0 else 0
    
#prices = [7,1,5,3,6,4]
#prices = [7,6,4,3,1]
prices = [2,4,1]

sol = Solution()

print(sol.maxProfit(prices))