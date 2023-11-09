from math import floor
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) == 1:
            return 0

        min_price = prices[0]
        max_profit = 0

        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)

        return max_profit



# Example 1
prices = [7,1,5,3,6,4]

s = Solution()
print(s.maxProfit(prices))


# Example 2
prices = [7,6,4,3,1]

s = Solution()
print(s.maxProfit(prices))

# Example 3
prices = [4,1,2]

s = Solution()
print(s.maxProfit(prices))

# Example 4
prices = [3,3]

s = Solution()
print(s.maxProfit(prices))
