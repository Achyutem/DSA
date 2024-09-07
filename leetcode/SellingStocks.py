# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
class Solution:
    def maxProfit(self, prices):
        l, r = 0, 1

        max_profit = 0
        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
                r += 1
            else:
                profit = prices[r] - prices[l]

                if profit > max_profit:
                    max_profit = profit

                r += 1

        return max_profit
