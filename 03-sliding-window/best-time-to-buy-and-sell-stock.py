"""
Problem  Name: Best Time to Buy and Sell Stock
NeetCode Link: https://neetcode.io/problems/buy-and-sell-crypto/question
LeetCode Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description

Time  Complexity: O(n)
Space Complexity: O(1)

Platform Sync: Class/Method/Variable names & signatures may need minor adjustments
               to match platform-specific requirements.
"""

# ───────────
# SOLUTION 1:
# ───────────
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left_idx = 0
        right_idx = left_idx + 1

        max_profit = 0

        while right_idx < len(prices):
            curr_profit = prices[right_idx] - prices[left_idx]

            max_profit = max(max_profit, curr_profit)

            if prices[left_idx] > prices[right_idx]:
                left_idx = right_idx

            right_idx += 1

        return max_profit

# ───────────
# SOLUTION 2:
# ───────────
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        curr_min = prices[0]

        for price in range(len(prices)):
            curr_profit = prices[price] - curr_min

            max_profit = max(max_profit, curr_profit)

            curr_min = min(curr_min, prices[price])

        return max_profit